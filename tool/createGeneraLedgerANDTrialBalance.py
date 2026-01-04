import csv
import os

"""
说明:
    这个是通过InvoiceSmartLink_withoutOCR软件生成的 仕訳帳 继续生成　総勘定元帳 和　試算表的
运行方法:
    python createGeneraLedgerANDTrialBalance.py
    然后输入 仕訳帳 的地址即可
打包:
    pyinstaller --onefile --icon=cGLATB.ico --name=createGeneraLedgerANDTrialBalance createGeneraLedgerANDTrialBalance.py

"""

def create_general_ledger_from_csv(input_csv):
    ledger = {}
    date_part = None

    with open(input_csv, mode='r', encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if date_part is None:
                date_part = row['日付'][:6].replace('-', '')

            if row['借方科目'] not in ledger:
                ledger[row['借方科目']] = []
            if row['貸方科目'] not in ledger:
                ledger[row['貸方科目']] = []

            # 将借方科目的记录存储到字典中，并在借方列记录金额
            ledger[row['借方科目']].append({
                '日付': row['日付'],
                '借方': row['金額'],  # 借方金额
                '貸方': '',  # 貸方为空
                '伝票番号': row['伝票番号'],
                '概要': row['概要']  # 追加概要项目
            })
            # 将貸方科目的记录存储到字典中，并在貸方列记录金额
            ledger[row['貸方科目']].append({
                '日付': row['日付'],
                '借方': '',  # 借方为空
                '貸方': row['金額'],  # 貸方金额
                '伝票番号': row['伝票番号'],
                '概要': row['概要']  # 追加概要项目
            })

    output_files = []
    for account, entries in ledger.items():
        # 添加一个检查account是否为空的条件，如果为空则跳过
        if not account:
            continue
        output_file_name = f"{account}_{date_part}.csv"
        output_file_path = os.path.join("総勘定元帳and試算表", output_file_name)
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        with open(output_file_path, mode='w', encoding='utf-8-sig', newline='') as output_csv:
            writer = csv.DictWriter(output_csv, fieldnames=['日付', '借方', '貸方', '伝票番号', '概要'])
            writer.writeheader()
            writer.writerows(entries)
        output_files.append(output_file_name)
        print(f"ファイルが作成されました: {output_file_path}")

    return output_files, date_part

def clean_amount(amount):
    return float(amount.replace('¥', '').replace(',', ''))

def generate_trial_balance_from_ledgers(ledger_files, date_part):
    trial_balance = {}
    for ledger_file in ledger_files:
        with open(ledger_file, mode='r', encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                account_name = os.path.basename(ledger_file).split('_')[0]
                debit_amount = row['借方']
                credit_amount = row['貸方']

                if account_name not in trial_balance:
                    trial_balance[account_name] = {'借方': 0.0, '貸方': 0.0}

                if debit_amount:
                    trial_balance[account_name]['借方'] += clean_amount(debit_amount)
                if credit_amount:
                    trial_balance[account_name]['貸方'] += clean_amount(credit_amount)

    output_file_path = f"総勘定元帳and試算表/試算表_{date_part}.csv"
    with open(output_file_path, mode='w', encoding='utf-8-sig', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['科目', '借方', '貸方'])  # 添加表头

        total_debit = 0.0  # 初始化借方总和
        total_credit = 0.0  # 初始化贷方总和

        for account, amounts in trial_balance.items():
            # 只保留非零的借方和贷方金额
            debit_total = amounts['借方'] if amounts['借方'] != 0 else ''
            credit_total = amounts['貸方'] if amounts['貸方'] != 0 else ''
            writer.writerow([account, debit_total, credit_total])

            # 累加借方和贷方金额
            if isinstance(amounts['借方'], (float, int)):
                total_debit += amounts['借方']
            if isinstance(amounts['貸方'], (float, int)):
                total_credit += amounts['貸方']

        # 写入借方和贷方总和
        writer.writerow(['合計', total_debit if total_debit else '', total_credit if total_credit else ''])

    print(f"試算表已生成: {output_file_path}")

if __name__ == "__main__":
    # 先创建総勘定元帳
    input_file_name = input("请输入CSV文件名（例如：仕訳帳.csv）: ")
    input_file_name = input_file_name.strip()  # 去除前后空白字符
    input_file_name = input_file_name.replace('\u202a', '')  # 去除特殊字符
    ledger_files, date_part = create_general_ledger_from_csv(input_file_name)

    # 然后生成试算表
    ledger_files = [os.path.join("総勘定元帳and試算表", file) for file in ledger_files]  # 构造完整路径
    generate_trial_balance_from_ledgers(ledger_files, date_part)
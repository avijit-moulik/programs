import tabula
import pandas as pd


def pdf_to_excel(pdfp,excelp):
    dfs= tabula.read_pdf(pdfp,pages='all',multiple_tables=True)
    df=pd.concat(dfs,ignore_index=True)
    df.to_excel(excelp,index=False)
    
if __name__ == '__main__':
     # Replace 'input.pdf' with your PDF file and 'output.xlsx' with the desired Excel file name
    
    pdfp = 'input.pdf'
    exelp = 'output.pdf'
    
    pdf_to_excel(pdfp,excelp)



'''   Run the script:

bash

python pdf_to_excel.py
'''

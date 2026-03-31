import pandas as pd
import httpx

def get_code(company_name: str) -> dict:
    df = pd.read_csv("data/data_2058.csv", encoding='cp949')
    return df[df['한글 종목명'].apply(lambda x : x.find(company_name) > -1)].to_json()

def get_company_info(company_code: str) -> dict:
    url = f"https://wts-info-api.tossinvest.com/api/v2/stock-infos/A{company_code}/overview"
    rt = httpx.get(url).json()
    return rt['result']['company']

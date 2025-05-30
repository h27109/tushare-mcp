import sys
sys.path.append('..')
from src.apis.macro_china import *

if __name__ == "__main__":
    # 测试日期设置
    test_date = '20250516'  # 测试日期
    test_month = '202504'   # 测试月份
    test_quarter = '2025Q1' # 测试季度
    
    # 测试 shibor 接口（上海银行间同业拆放利率）
    print("测试 shibor 接口:")
    print(shibor_wrapper({
        'start_date': '20240101',
        'end_date': test_date
    }))
    
    # 测试 shibor_quote 接口（Shibor报价数据）
    print("\n测试 shibor_quote 接口:")
    print(shibor_quote_wrapper({
        'date': test_date
    }))
    
    # 测试 shibor_lpr 接口（LPR贷款基础利率）
    print("\n测试 shibor_lpr 接口:")
    print(shibor_lpr_wrapper({
        'start_date': '20240101',
        'end_date': test_date
    }))
    
    # 测试 libor 接口（伦敦同业拆借利率）
    print("\n测试 libor 接口:")
    print(libor_wrapper({
        'date': test_date,
        'curr_type': 'USD'  # 测试美元利率
    }))
    
    # 测试 hibor 接口（香港银行同业拆借利率）
    print("\n测试 hibor 接口:")
    print(hibor_wrapper({
        'date': test_date
    }))
    
    # 测试 cn_gdp 接口（GDP数据）
    print("\n测试 cn_gdp 接口:")
    print(cn_gdp_wrapper({
        'q': test_quarter,
        'fields': 'quarter,gdp,gdp_yoy'
    }))
    
    # 测试 cpi 接口（居民消费价格指数）
    print("\n测试 cpi 接口:")
    print(cpi_wrapper({
        'start_m': '202501',
        'end_m': test_month
    }))
    
    # 测试 ppi 接口（工业生产者出厂价格指数）
    print("\n测试 ppi 接口:")
    print(ppi_wrapper({
        'm': test_month
    }))
    
    # 测试 cn_m 接口（货币供应量）
    print("\n测试 cn_m 接口:")
    print(cn_m_wrapper({
        'm': test_month,
        'fields': 'month,m0,m1,m2'
    }))
    
    # 测试 sf_month 接口（社会融资数据）
    print("\n测试 sf_month 接口:")
    print(sf_month_wrapper({
        'start_m': '202501',
        'end_m': test_month
    }))
    
    # 测试 cn_pmi 接口（采购经理人指数）
    print("\n测试 cn_pmi 接口:")
    print(cn_pmi_wrapper({
        'm': test_month,
        'fields': 'month,pmi010000,pmi010400'  # 测试制造业PMI和生产指数
    })) 
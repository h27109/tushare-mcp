import sys
sys.path.append('..')
from src.apis.macro_international import *

if __name__ == "__main__":
    # 测试日期设置
    test_date = '20250516'  # 测试日期
    test_start_date = '20250101'  # 测试起始日期
    test_end_date = '20250516'    # 测试结束日期
    
    # 测试 us_tycr 接口（美国国债收益率曲线利率）
    print("测试 us_tycr 接口（美国国债收益率曲线利率）:")
    print(us_tycr_wrapper({
        'start_date': test_start_date,
        'end_date': test_end_date,
        'fields': 'm1,y1,y5,y10,y30'  # 测试1月期、1年期、5年期、10年期和30年期收益率
    }))
    
    # 测试 us_trycr 接口（美国国债实际收益率曲线利率）
    print("\n测试 us_trycr 接口（美国国债实际收益率曲线利率）:")
    print(us_trycr_wrapper({
        'date': test_date,
        'fields': 'date,y5,y10,y30'  # 测试5年期、10年期和30年期实际收益率
    }))
    
    # 测试 us_tbr 接口（美国短期国债利率）
    print("\n测试 us_tbr 接口（美国短期国债利率）:")
    print(us_tbr_wrapper({
        'start_date': test_start_date,
        'end_date': test_end_date,
        'fields': 'date,w4_bd,w13_bd,w52_bd'  # 测试4周、13周和52周银行折现收益率
    }))
    
    # 测试 us_tltr 接口（美国国债长期利率）
    print("\n测试 us_tltr 接口（美国国债长期利率）:")
    print(us_tltr_wrapper({
        'start_date': test_start_date,
        'end_date': test_end_date,
        'fields': 'date,ltc,cmt,e_factor'  # 测试所有长期利率指标
    }))
    
    # 测试 us_trltr 接口（美国国债实际长期利率平均值）
    print("\n测试 us_trltr 接口（美国国债实际长期利率平均值）:")
    print(us_trltr_wrapper({
        'start_date': test_start_date,
        'end_date': test_end_date,
        'fields': 'date,ltr_avg'  # 测试实际平均利率
    })) 
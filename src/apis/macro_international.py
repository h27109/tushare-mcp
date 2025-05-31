from .tushare_pro import pro
def us_tycr_wrapper(params: dict):
    """
    美国国债收益率曲线利率（日频）
    接口：us_tycr
    描述：获取美国每日国债收益率曲线利率
    限量：单次最大可获取2000条数据


    输入参数
    名称	类型	必选	描述
    date	str	N	日期 （YYYYMMDD格式，下同）
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    fields	str	N	指定输出字段（e.g. fields='m1,y1'）

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    m1	float	Y	1月期
    m2	float	Y	2月期
    m3	float	Y	3月期
    m4	float	Y	4月期（数据从20221019开始）
    m6	float	Y	6月期
    y1	float	Y	1年期
    y2	float	Y	2年期
    y3	float	Y	3年期
    y5	float	Y	5年期
    y7	float	Y	7年期
    y10	float	Y	10年期
    y20	float	Y	20年期
    y30	float	Y	30年期
    """
    return pro.us_tycr(**params)


def us_trycr_wrapper(params: dict):
    """
    美国国债实际收益率曲线利率
    接口：us_trycr
    描述：国债实际收益率曲线利率
    限量：单次最大可获取2000行数据，可循环获取

    输入参数
    名称	类型	必选	描述
    date	str	N	日期 （YYYYMMDD格式，下同）
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    fields	str	N	指定输出字段

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    y5	float	Y	5年期
    y7	float	Y	7年期
    y10	float	Y	10年期
    y20	float	Y	20年期
    y30	float	Y	30年期
    """
    return pro.us_trycr(**params)

def us_tbr_wrapper(params: dict):
    """
    短期国债利率
    接口：us_tbr
    描述：获取美国短期国债利率数据
    限量：单次最大可获取2000行数据，可循环获取

    输入参数
    名称	类型	必选	描述
    date	str	N	日期
    start_date	str	N	开始日期(YYYYMMDD格式)
    end_date	str	N	结束日期
    fields	str	N	指定输出字段(e.g. fields='w4_bd,w52_ce')

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    w4_bd	float	Y	4周银行折现收益率
    w4_ce	float	Y	4周票面利率
    w8_bd	float	Y	8周银行折现收益率
    w8_ce	float	Y	8周票面利率
    w13_bd	float	Y	13周银行折现收益率
    w13_ce	float	Y	13周票面利率
    w17_bd	float	Y	17周银行折现收益率（数据从20221019开始）
    w17_ce	float	Y	17周票面利率（数据从20221019开始）
    w26_bd	float	Y	26周银行折现收益率
    w26_ce	float	Y	26周票面利率
    w52_bd	float	Y	52周银行折现收益率
    w52_ce	float	Y	52周票面利率
    """
    return pro.us_tbr(**params)

def us_tltr_wrapper(params: dict):
    """
    国债长期利率
    接口：us_tltr
    描述：国债长期利率
    限量：单次最大可获取2000行数据，可循环获取

    输入参数
    名称	类型	必选	描述
    date	str	N	日期
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    fields	str	N	指定字段

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    ltc	float	Y	收益率 LT COMPOSITE (>10 Yrs)
    cmt	float	Y	20年期CMT利率(TREASURY 20-Yr CMT)
    e_factor	float	Y	外推因子EXTRAPOLATION FACTOR
    """
    return pro.us_tltr(**params)

def us_trltr_wrapper(params: dict):
    """
    国债实际长期利率平均值
    接口：us_trltr
    描述：国债实际长期利率平均值
    限量：单次最大可获取2000行数据，可循环获取

    输入参数
    名称	类型	必选	描述
    date	str	N	日期
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    fields	str	N	指定字段

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    ltr_avg	float	Y	实际平均利率LT Real Average (10> Yrs)
    """
    return pro.us_trltr(**params)
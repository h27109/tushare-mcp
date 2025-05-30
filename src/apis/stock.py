from .tushare_pro import pro

# 描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等
def stock_basic_wrapper(params: dict):
    """
    接口：stock_basic，可以通过数据工具调试和查看数据
    描述：获取基础信息数据，包括股票代码、名称、上市日期、退市日期等

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS股票代码
    name	str	N	名称
    market	str	N	市场类别 （主板/创业板/科创板/CDR/北交所）
    list_status	str	N	上市状态 L上市 D退市 P暂停上市，默认是L
    exchange	str	N	交易所 SSE上交所 SZSE深交所 BSE北交所
    is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS代码
    symbol	str	Y	股票代码
    name	str	Y	股票名称
    area	str	Y	地域
    industry	str	Y	所属行业
    fullname	str	N	股票全称
    enname	str	N	英文全称
    cnspell	str	Y	拼音缩写
    market	str	Y	市场类型（主板/创业板/科创板/CDR）
    exchange	str	N	交易所代码
    curr_type	str	N	交易货币
    list_status	str	N	上市状态 L上市 D退市 P暂停上市
    list_date	str	Y	上市日期
    delist_date	str	N	退市日期
    is_hs	str	N	是否沪深港通标的，N否 H沪股通 S深股通
    act_name	str	Y	实控人名称
    act_ent_type	str	Y	实控人企业性质
    """
    df = pro.stock_basic(**params)
    return df

# 描述：获取上市公司基础信息
def stock_company_wrapper(params: dict):
    """
    接口：stock_company
    描述：获取上市公司基础信息

    输入参数
    名称	类型	必须	描述
    ts_code	str	N	股票代码
    exchange	str	N	交易所代码 ，SSE上交所 SZSE深交所 BSE北交所

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	股票代码
    com_name	str	Y	公司全称
    com_id	str	Y	统一社会信用代码
    exchange	str	Y	交易所代码
    chairman	str	Y	法人代表
    manager	str	Y	总经理
    secretary	str	Y	董秘
    reg_capital	float	Y	注册资本(万元)
    setup_date	str	Y	注册日期
    province	str	Y	所在省份
    city	str	Y	所在城市
    introduction	str	N	公司介绍
    website	str	Y	公司主页
    email	str	Y	电子邮件
    office	str	N	办公室
    employees	int	Y	员工人数
    main_business	str	N	主要业务及产品
    business_scope	str	N	经营范围
    """
    df = pro.stock_company(**params)
    return df

# 描述：获取上市公司管理层
def stk_managers_wrapper(params: dict):
    """
    接口：stk_managers
    描述：获取上市公司管理层

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	股票代码，支持单个或多个股票输入
    ann_date	str	N	公告日期（YYYYMMDD格式，下同）
    start_date	str	N	公告开始日期
    end_date	str	N	公告结束日期

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS股票代码
    ann_date	str	Y	公告日期
    name	str	Y	姓名
    gender	str	Y	性别
    lev	str	Y	岗位类别
    title	str	Y	岗位
    edu	str	Y	学历
    national	str	Y	国籍
    birthday	str	Y	出生年月
    begin_date	str	Y	上任日期
    end_date	str	Y	离任日期
    resume	str	N	个人简历
    """
    df = pro.stk_managers(**params) 
    return df

# 描述：获取股票日行情数据，或通过通用行情接口获取数据，包含了前后复权数据
def daily_wrapper(params: dict):
    """
    接口：daily，A股日线行情
    描述：获取股票日行情数据，或通过通用行情接口获取数据，包含了前后复权数据

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	股票代码（支持多个股票同时提取，逗号分隔）
    trade_date	str	N	交易日期（YYYYMMDD）
    start_date	str	N	开始日期(YYYYMMDD)
    end_date	str	N	结束日期(YYYYMMDD)
    注：日期都填YYYYMMDD格式，比如20181010

    输出参数
    名称	类型	描述
    ts_code	str	股票代码
    trade_date	str	交易日期
    open	float	开盘价
    high	float	最高价
    low	float	最低价
    close	float	收盘价
    pre_close	float	昨收价【除权价，前复权】
    change	float	涨跌额
    pct_chg	float	涨跌幅 【基于除权后的昨收计算的涨跌幅：（今收-除权昨收）/除权昨收 】
    vol	float	成交量 （手）
    amount	float	成交额 （千元）
    """
    df = pro.daily(**params)
    return df

# 描述：获取实时日k线行情，支持按股票代码及股票代码通配符一次性提取全部股票实时日k线行情
def rt_k_wrapper(params: dict):
    """
    沪深京实时日线
    接口：rt_k
    描述：获取实时日k线行情，支持按股票代码及股票代码通配符一次性提取全部股票实时日k线行情
    限量：单次最大可提取6000条数据


    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	支持通配符方式，e.g. 6*.SH、301*.SZ、600000.SH
    注：ts_code代码一定要带.SH/.SZ/.BJ后缀

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	股票代码
    name	None	Y	股票名称
    pre_close	float	Y	昨收价
    high	float	Y	最高价
    open	float	Y	开盘价
    low	float	Y	最低价
    close	float	Y	收盘价
    vol	int	Y	成交量（股）
    amount	int	Y	成交金额（元）
    num	int	Y	开盘以来成交笔数
    """
    df = pro.rt_k(**params)
    return df

# 描述：获取A股周线行情
def weekly_wrapper(params: dict):
    """
    接口：weekly
    描述：获取A股周线行情
    限量：单次最大4500行，总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	TS代码
    trade_date	str	N	交易日期 （每周最后一个交易日期，YYYYMMDD格式）
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	股票代码
    trade_date	str	Y	交易日期
    close	float	Y	周收盘价
    open	float	Y	周开盘价
    high	float	Y	周最高价
    low	float	Y	周最低价
    pre_close	float	Y	上一周收盘价
    change	float	Y	周涨跌额
    pct_chg	float	Y	周涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
    vol	float	Y	周成交量
    amount	float	Y	周成交额
    """
    return pro.weekly(**params)

# 描述：获取A股月线数据
def monthly_wrapper(params: dict):
    """
    接口：monthly
    描述：获取A股月线数据
    限量：单次最大4500行，总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	TS代码
    trade_date	str	N	交易日期 （每月最后一个交易日日期，YYYYMMDD格式）
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	股票代码
    trade_date	str	Y	交易日期
    close	float	Y	月收盘价
    open	float	Y	月开盘价
    high	float	Y	月最高价
    low	float	Y	月最低价
    pre_close	float	Y	上月收盘价
    change	float	Y	月涨跌额
    pct_chg	float	Y	月涨跌幅 （未复权，如果是复权请用 通用行情接口 ）
    vol	float	Y	月成交量
    amount	float	Y	月成交额
    """
    return pro.monthly(**params)

# 描述：获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。
def daily_basic_data_wrapper(params: dict):
    """
    每日指标
    接口：daily_basic，可以通过数据工具调试和查看数据。
    更新时间：交易日每日15点～17点之间
    描述：获取全部股票每日重要的基本面指标，可用于选股分析、报表展示等。

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	股票代码
    trade_date	str	N	交易日期
    start_date	str	N	开始日期(YYYYMMDD)
    end_date	str	N	结束日期(YYYYMMDD)
    注：日期都填YYYYMMDD格式，比如20181010

    输出参数

    名称	类型	描述
    ts_code	str	TS股票代码
    trade_date	str	交易日期
    close	float	当日收盘价
    turnover_rate	float	换手率（%）
    turnover_rate_f	float	换手率（自由流通股）
    volume_ratio	float	量比
    pe	float	市盈率（总市值/净利润， 亏损的PE为空）
    pe_ttm	float	市盈率（TTM，亏损的PE为空）
    pb	float	市净率（总市值/净资产）
    ps	float	市销率
    ps_ttm	float	市销率（TTM）
    dv_ratio	float	股息率 （%）
    dv_ttm	float	股息率（TTM）（%）
    total_share	float	总股本 （万股）
    float_share	float	流通股本 （万股）
    free_share	float	自由流通股本 （万）
    total_mv	float	总市值 （万元）
    circ_mv	float	流通市值（万元）
    """
    return pro.daily_basic(**params)


def top10_holders_wrapper(params: dict) :
    """
    前十大股东
    接口：top10_holders
    描述：获取上市公司前十大股东数据，包括持有数量和比例等信息

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	TS代码
    period	str	N	报告期（YYYYMMDD格式，一般为每个季度最后一天）
    ann_date	str	N	公告日期
    start_date	str	N	报告期开始日期
    end_date	str	N	报告期结束日期

    输出参数
    名称	类型	描述
    ts_code	str	TS股票代码
    ann_date	str	公告日期
    end_date	str	报告期
    holder_name	str	股东名称
    hold_amount	float	持有数量（股）
    hold_ratio	float	占总股本比例(%)
    hold_float_ratio	float	占流通股本比例(%)
    hold_change	float	持股变动
    holder_type	str	股东类型
    """
    return pro.top10_holders(**params)

def top10_floatholders_wrapper(params: dict) :
    """
    前十大流通股东
    接口：top10_floatholders
    描述：获取上市公司前十大流通股东数据

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	TS代码
    period	str	N	报告期（YYYYMMDD格式，一般为每个季度最后一天）
    ann_date	str	N	公告日期
    start_date	str	N	报告期开始日期
    end_date	str	N	报告期结束日期
    
    输出参数
    名称	类型	描述
    ts_code	str	TS股票代码
    ann_date	str	公告日期
    end_date	str	报告期
    holder_name	str	股东名称
    hold_amount	float	持有数量（股）
    hold_ratio	float	占总股本比例(%)
    hold_float_ratio	float	占流通股本比例(%)
    hold_change	float	持股变动
    holder_type	str	股东类型
    """
    return pro.top10_floatholders(**params)

def stk_holdernumber_wrapper(params: dict) :
    """
    股东人数
    接口：stk_holdernumber
    描述：获取上市公司股东户数数据，数据不定期公布
    限量：单次最大3000,总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	TS股票代码
    ann_date	str	N	公告日期
    enddate	str	N	截止日期
    start_date	str	N	公告开始日期
    end_date	str	N	公告结束日期

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS股票代码
    ann_date	str	Y	公告日期
    end_date	str	Y	截止日期
    holder_num	int	Y	股东户数
    """
    return pro.stk_holdernumber(**params)

def stock_moneyflow_wrapper(params: dict) :
    """
    个股资金流向
    接口：moneyflow，可以通过数据工具调试和查看数据。
    描述：获取沪深A股票资金流向数据，分析大单小单成交情况，用于判别资金动向，数据开始于2010年。
    限量：单次最大提取6000行记录，总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	股票代码 （股票和时间参数至少输入一个）
    trade_date	str	N	交易日期
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS代码
    trade_date	str	Y	交易日期
    buy_sm_vol	int	Y	小单买入量（手）
    buy_sm_amount	float	Y	小单买入金额（万元）
    sell_sm_vol	int	Y	小单卖出量（手）
    sell_sm_amount	float	Y	小单卖出金额（万元）
    buy_md_vol	int	Y	中单买入量（手）
    buy_md_amount	float	Y	中单买入金额（万元）
    sell_md_vol	int	Y	中单卖出量（手）
    sell_md_amount	float	Y	中单卖出金额（万元）
    buy_lg_vol	int	Y	大单买入量（手）
    buy_lg_amount	float	Y	大单买入金额（万元）
    sell_lg_vol	int	Y	大单卖出量（手）
    sell_lg_amount	float	Y	大单卖出金额（万元）
    buy_elg_vol	int	Y	特大单买入量（手）
    buy_elg_amount	float	Y	特大单买入金额（万元）
    sell_elg_vol	int	Y	特大单卖出量（手）
    sell_elg_amount	float	Y	特大单卖出金额（万元）
    net_mf_vol	int	Y	净流入量（手）
    net_mf_amount	float	Y	净流入额（万元）

    各类别统计规则如下：
    小单：5万以下 中单：5万～20万 大单：20万～100万 特大单：成交额>=100万 ，数据基于主动买卖单统计
    """
    return pro.moneyflow(**params)

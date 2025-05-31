from .tushare_pro import pro

def index_basic_wrapper(params: dict):
    """
    指数基本信息
    接口：index_basic，可以通过数据工具调试和查看数据。
    描述：获取指数基础信息。

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	指数代码
    name	str	N	指数简称
    market	str	N	交易所或服务商(默认SSE)
    publisher	str	N	发布商
    category	str	N	指数类别
    
    输出参数
    名称	类型	描述
    ts_code	str	TS代码
    name	str	简称
    fullname	str	指数全称
    market	str	市场
    publisher	str	发布方
    index_type	str	指数风格
    category	str	指数类别
    base_date	str	基期
    base_point	float	基点
    list_date	str	发布日期
    weight_rule	str	加权方式
    desc	str	描述
    exp_date	str	终止日期
    市场说明(market)

    市场代码	说明
    MSCI	MSCI指数
    CSI	中证指数
    SSE	上交所指数
    SZSE	深交所指数
    CICC	中金指数
    SW	申万指数
    OTH	其他指数
    指数列表

    主题指数
    规模指数
    策略指数
    风格指数
    综合指数
    成长指数
    价值指数
    有色指数
    化工指数
    能源指数
    其他指数
    外汇指数
    基金指数
    商品指数
    债券指数
    行业指数
    贵金属指数
    农副产品指数
    软商品指数
    油脂油料指数
    非金属建材指数
    煤焦钢矿指数
    谷物指数
    """
    return pro.index_basic(**params)

def index_daily_wrapper(params: dict):
    """
    指数日线行情
    接口：index_daily，可以通过数据工具调试和查看数据。
    描述：获取指数每日行情，还可以通过bar接口获取。规则是单次调取最多取8000行记录，可以设置start和end日期补全。指数行情也可以通过通用行情接口获取数据．

    注意：深证成指（399001.SZ）被普遍看作反映深证A股整体表现的大盘，而实际上该指数只包含500只成分股。而各类行情软件上展示的成交量、成交金额是深市所有A股的股票成交情况，如果需要获得与行情软件上一样的成交数据，可以调取深证A指（399107.SZ）。

    输入参数
    名称	类型	必选	描述
    ts_code	str	Y	指数代码，来源指数基础信息接口
    trade_date	str	N	交易日期 （日期格式：YYYYMMDD，下同）
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	描述
    ts_code	str	TS指数代码
    trade_date	str	交易日
    close	float	收盘点位
    open	float	开盘点位
    high	float	最高点位
    low	float	最低点位
    pre_close	float	昨日收盘点
    change	float	涨跌点
    pct_chg	float	涨跌幅（%）
    vol	float	成交量（手）
    amount	float	成交额（千元）
    
    """
    return pro.index_daily(**params)

def index_weekly_wrapper(params: dict):
    """
    指数周线行情
    接口：index_weekly
    描述：获取指数周线行情
    限量：单次最大1000行记录，可分批获取，总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS代码
    trade_date	str	N	交易日期
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS指数代码
    trade_date	str	Y	交易日
    close	float	Y	收盘点位
    open	float	Y	开盘点位
    high	float	Y	最高点位
    low	float	Y	最低点位
    pre_close	float	Y	昨日收盘点
    change	float	Y	涨跌点位
    pct_chg	float	Y	涨跌幅
    vol	float	成交量（手）	
    amount	float	成交额（千元）
    """
    return pro.index_weekly(**params)

def index_monthly_wrapper(params: dict):
    """
    指数月线行情
    接口：index_monthly
    描述：获取指数月线行情,每月更新一次
    限量：单次最大1000行记录,可多次获取,总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS代码
    trade_date	str	N	交易日期
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS指数代码
    trade_date	str	Y	交易日
    close	float	Y	收盘点位
    open	float	Y	开盘点位
    high	float	Y	最高点位
    low	float	Y	最低点位
    pre_close	float	Y	昨日收盘点
    change	float	Y	涨跌点位
    pct_chg	float	Y	涨跌幅
    vol	float	成交量（手）	
    amount	float	成交额（千元）
    """
    return pro.index_monthly(**params)

def index_weight_wrapper(params: dict):
    """
    指数成分和权重
    接口：index_weight
    描述：获取各类指数成分和权重，月度数据 ，建议输入参数里开始日期和结束日分别输入当月第一天和最后一天的日期。
    来源：指数公司网站公开数据

    输入参数
    名称	类型	必选	描述
    index_code	str	Y	指数代码，来源指数基础信息接口
    trade_date	str	N	交易日期（格式YYYYMMDD，下同）
    start_date	str	N	开始日期
    end_date	None	N	结束日期
    
    输出参数
    名称	类型	描述
    index_code	str	指数代码
    con_code	str	成分代码
    trade_date	str	交易日期
    weight	float	权重
    """
    return pro.index_weight(**params)

def index_daily_basic_wrapper(params: dict):
    """
    大盘指数每日指标
    接口：index_dailybasic，可以通过数据工具调试和查看数据。
    描述：目前只提供上证综指，深证成指，上证50，中证500，中小板指，创业板指的每日指标数据

    输入参数
    名称	类型	必选	描述
    trade_date	str	N	交易日期 （格式：YYYYMMDD，比如20181018，下同）
    ts_code	str	N	TS代码
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    注：trade_date，ts_code 至少要输入一个参数，单次限量3000条（即，单一指数单次可提取超过12年历史），总量不限制。

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS代码
    trade_date	str	Y	交易日期
    total_mv	float	Y	当日总市值（元）
    float_mv	float	Y	当日流通市值（元）
    total_share	float	Y	当日总股本（股）
    float_share	float	Y	当日流通股本（股）
    free_share	float	Y	当日自由流通股本（股）
    turnover_rate	float	Y	换手率
    turnover_rate_f	float	Y	换手率(基于自由流通股本)
    pe	float	Y	市盈率
    pe_ttm	float	Y	市盈率TTM
    pb	float	Y	市净率
    """
    return pro.index_dailybasic(**params)

def index_global_wrapper(params: dict):
    """
    国际指数
    接口：index_global，可以通过数据工具调试和查看数据。
    描述：获取国际主要指数日线行情
    限量：单次最大提取4000行情数据，可循环获取，总量不限制

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS指数代码，见下表
    trade_date	str	N	交易日期，YYYYMMDD格式，下同
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    TS指数代码	指数名称
    XIN9	富时中国A50指数 (富时A50)
    HSI	恒生指数
    HKTECH	恒生科技指数
    HKAH	恒生AH股H指数
    DJI	道琼斯工业指数
    SPX	标普500指数
    IXIC	纳斯达克指数
    FTSE	富时100指数
    FCHI	法国CAC40指数
    GDAXI	德国DAX指数
    N225	日经225指数
    KS11	韩国综合指数
    AS51	澳大利亚标普200指数
    SENSEX	印度孟买SENSEX指数
    IBOVESPA	巴西IBOVESPA指数
    RTS	俄罗斯RTS指数
    TWII	台湾加权指数
    CKLSE	马来西亚指数
    SPTSX	加拿大S&P/TSX指数
    CSX5P	STOXX欧洲50指数
    RUT	罗素2000指数

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS指数代码
    trade_date	str	Y	交易日
    open	float	Y	开盘点位
    close	float	Y	收盘点位
    high	float	Y	最高点位
    low	float	Y	最低点位
    pre_close	float	Y	昨日收盘点
    change	float	Y	涨跌点位
    pct_chg	float	Y	涨跌幅
    swing	float	Y	振幅
    vol	float	Y	成交量 （大部分无此项数据）
    amount	float	N	成交额 （大部分无此项数据）
    """
    return pro.index_global(**params)

def index_daily_info_wrapper(params: dict):
    """
    市场交易统计
    接口：daily_info
    描述：获取交易所股票交易统计，包括各板块明细
    限量：单次最大4000，可循环获取，总量不限制

    输入参数
    名称	类型	必选	描述
    trade_date	str	N	交易日期（YYYYMMDD格式，下同）
    ts_code	str	N	板块代码（请参阅下方列表）
    exchange	str	N	股票市场（SH上交所 SZ深交所）
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    板块代码（TS_CODE）	板块名称（TS_NAME）	数据开始日期
    SZ_MARKET	深圳市场	20041231
    SZ_MAIN	深圳主板	20081231
    SZ_A	深圳A股	20080103
    SZ_B	深圳B股	20080103
    SZ_GEM	创业板	20091030
    SZ_SME	中小企业板	20040602
    SZ_FUND	深圳基金市场	20080103
    SZ_FUND_ETF	深圳基金ETF	20080103
    SZ_FUND_LOF	深圳基金LOF	20080103
    SZ_FUND_CEF	深圳封闭基金	20080103
    SZ_FUND_SF	深圳分级基金	20080103
    SZ_BOND	深圳债券	20080103
    SZ_BOND_CN	深圳债券现券	20080103
    SZ_BOND_REP	深圳债券回购	20080103
    SZ_BOND_ABS	深圳债券ABS	20080103
    SZ_BOND_GOV	深圳国债	20080103
    SZ_BOND_ENT	深圳企业债	20080103
    SZ_BOND_COR	深圳公司债	20080103
    SZ_BOND_CB	深圳可转债	20080103
    SZ_WR	深圳权证	20080103
    ----	----	---
    SH_MARKET	上海市场	20190102
    SH_A	上海A股	19910102
    SH_B	上海B股	19920221
    SH_STAR	科创板	20190722
    SH_REP	股票回购	20190102
    SH_FUND	上海基金市场	19901219
    SH_FUND_ETF	上海基金ETF	19901219
    SH_FUND_LOF	上海基金LOF	19901219
    SH_FUND_REP	上海基金回购	19901219
    SH_FUND_CEF	上海封闭式基金	19901219
    SH_FUND_METF	上海交易型货币基金	19901219

    输出参数
    名称	类型	默认显示	描述
    trade_date	str	Y	交易日期
    ts_code	str	Y	市场代码
    ts_name	str	Y	市场名称
    com_count	int	Y	挂牌数
    total_share	float	Y	总股本（亿股）
    float_share	float	Y	流通股本（亿股）
    total_mv	float	Y	总市值（亿元）
    float_mv	float	Y	流通市值（亿元）
    amount	float	Y	交易金额（亿元）
    vol	float	Y	成交量（亿股）
    trans_count	int	Y	成交笔数（万笔）
    pe	float	Y	平均市盈率
    tr	float	Y	换手率（％），注：深交所暂无此列
    exchange	str	Y	交易所（SH上交所 SZ深交所）
    """
    return pro.daily_info(**params)

def sz_daily_info_wrapper(params: dict):
    """
    深圳市场每日交易概况
    接口：sz_daily_info
    描述：获取深圳市场每日交易概况
    限量：单次最大2000，可循环获取，总量不限制
    权限：用户积2000积分可调取， 频次有限制，积分越高每分钟调取频次越高，5000积分以上频次相对较高，积分获取方法请参阅积分获取办法

    输入参数
    名称	类型	必选	描述
    trade_date	str	N	交易日期（YYYYMMDD格式，下同）
    ts_code	str	N	板块代码
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    ts_code主要包括：
    板块代码（TS_CODE）	板块说明	数据开始日期
    股票	深圳市场股票总和	20080102
    主板A股	深圳主板A股情况	20080102
    主板B股	深圳主板B股情况	20080102
    创业板A股	深圳创业板情况	20080102
    基金	深圳市场基金总和	20080102
    ETF	深圳ETF交易情况	20080102
    LOF	深圳LOF交易情况	20080102
    封闭式基金	深圳封闭式基金交易情况	20080102
    基础设施基金	深圳RETIS基金交易情况	20210621
    债券	深圳债券市场总和	20080102
    债券现券	深圳现券交易情况	20080102
    债券回购	深圳债券回购交易情况	20080102
    ABS	深圳ABS交易情况	20080102
    期权	深圳期权总和	20080102

    输出参数
    名称	类型	默认显示	描述
    trade_date	str	Y	
    ts_code	str	Y	市场类型
    count	int	Y	股票个数
    amount	float	Y	成交金额
    vol	None	Y	成交量
    total_share	float	Y	总股本
    total_mv	float	Y	总市值
    float_share	float	Y	流通股票
    float_mv	float	Y	流通市值
    """
    return pro.sz_daily_info(**params)

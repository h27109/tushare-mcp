from .tushare_pro import pro

def fund_basic_wrapper(params: dict):
    """
    公募基金列表
    接口：fund_basic，可以通过数据工具调试和查看数据。
    描述：获取公募基金数据列表，包括场内和场外基金

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	基金代码
    market	str	N	交易市场: E场内 O场外（默认E）
    status	str	N	存续状态 D摘牌 I发行 L上市中
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	基金代码
    name	str	Y	简称
    management	str	Y	管理人
    custodian	str	Y	托管人
    fund_type	str	Y	投资类型
    found_date	str	Y	成立日期
    due_date	str	Y	到期日期
    list_date	str	Y	上市时间
    issue_date	str	Y	发行日期
    delist_date	str	Y	退市日期
    issue_amount	float	Y	发行份额(亿)
    m_fee	float	Y	管理费
    c_fee	float	Y	托管费
    duration_year	float	Y	存续期
    p_value	float	Y	面值
    min_amount	float	Y	起点金额(万元)
    exp_return	float	Y	预期收益率
    benchmark	str	Y	业绩比较基准
    status	str	Y	存续状态D摘牌 I发行 L已上市
    invest_type	str	Y	投资风格
    type	str	Y	基金类型
    trustee	str	Y	受托人
    purc_startdate	str	Y	日常申购起始日
    redm_startdate	str	Y	日常赎回起始日
    market	str	Y	E场内O场外
    """
    return pro.fund_basic(**params)

def fund_company_wrapper():
    """
    公募基金公司
    接口：fund_company
    描述：获取公募基金管理人列表

    输入参数
    无，可提取全部

    输出参数
    名称	类型	默认显示	描述
    name	str	Y	基金公司名称
    shortname	str	Y	简称
    short_enname	str	N	英文缩写
    province	str	Y	省份
    city	str	Y	城市
    address	str	Y	注册地址
    phone	str	Y	电话
    office	str	Y	办公地址
    website	str	Y	公司网址
    chairman	str	Y	法人代表
    manager	str	Y	总经理
    reg_capital	float	Y	注册资本
    setup_date	str	Y	成立日期
    end_date	str	Y	公司终止日期
    employees	float	Y	员工总数
    main_business	str	Y	主要产品及业务
    org_code	str	Y	组织机构代码
    credit_code	str	Y	统一社会信用代码
    """
    return pro.fund_company()

def fund_manager_wrapper(params: dict):
    """
    基金经理
    接口：fund_manager
    描述：获取公募基金经理数据，包括基金经理简历等数据
    限量：单次最大5000，支持分页提取数据

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	基金代码，支持多只基金，逗号分隔
    ann_date	str	N	公告日期，格式：YYYYMMDD
    name	str	N	基金经理姓名
    offset	intint	N	开始行数
    limit	int	N	每页行数

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	基金代码
    ann_date	str	Y	公告日期
    name	str	Y	基金经理姓名
    gender	str	Y	性别
    birth_year	str	Y	出生年份
    edu	str	Y	学历
    nationality	str	Y	国籍
    begin_date	str	Y	任职日期
    end_date	str	Y	离任日期
    resume	str	Y	简历
    """
    return pro.fund_manager(**params)

def fund_share_wrapper(params: dict):
    """
    基金规模数据
    接口：fund_share，可以通过数据工具调试和查看数据。
    描述：获取基金规模数据，包含上海和深圳ETF基金
    限量：单次最大提取2000行数据

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS基金代码
    trade_date	str	N	交易日期
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    market	str	N	市场代码（SH上交所 ，SZ深交所）

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	基金代码，支持多只基金同时提取，用逗号分隔
    trade_date	str	Y	交易（变动）日期，格式YYYYMMDD
    fd_share	float	Y	基金份额（万）
    """
    return pro.fund_share(**params)

def fund_nav_wrapper(params: dict):
    """
    公募基金净值
    接口：fund_nav，可以通过数据工具调试和查看数据。
    描述：获取公募基金净值数据
    积分：用户需要至少2000积分才可以调取，具体请参阅积分获取办法

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS基金代码 （二选一）
    nav_date	str	N	净值日期 （二选一）
    market	str	N	E场内 O场外
    start_date	str	N	净值开始日期
    end_date	str	N	净值结束日期
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS代码
    ann_date	str	Y	公告日期
    nav_date	str	Y	净值日期
    unit_nav	float	Y	单位净值
    accum_nav	float	Y	累计净值
    accum_div	float	Y	累计分红
    net_asset	float	Y	资产净值
    total_netasset	float	Y	合计资产净值
    adj_nav	float	Y	复权单位净值
    """
    return pro.fund_nav(**params)

def fund_div_wrapper(params: dict): 
    """
    公募基金分红
    接口：fund_div
    描述：获取公募基金分红数据

    输入参数
    名称	类型	必选	描述
    ann_date	str	N	公告日（以下参数四选一）
    ex_date	str	N	除息日
    pay_date	str	N	派息日
    ts_code	str	N	基金代码
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS代码
    ann_date	str	Y	公告日期
    imp_anndate	str	Y	分红实施公告日
    base_date	str	Y	分配收益基准日
    div_proc	str	Y	方案进度
    record_date	str	Y	权益登记日
    ex_date	str	Y	除息日
    pay_date	str	Y	派息日
    earpay_date	str	Y	收益支付日
    net_ex_date	str	Y	净值除权日
    div_cash	float	Y	每股派息(元)
    base_unit	float	Y	基准基金份额(万份)
    ear_distr	float	Y	可分配收益(元)
    ear_amount	float	Y	收益分配金额(元)
    account_date	str	Y	红利再投资到账日
    base_year	str	Y	份额基准年度
    """
    return pro.fund_div(**params)

def fund_portfolio_wrapper(params: dict):
    """
    公募基金持仓数据
    接口：fund_portfolio
    描述：获取公募基金持仓数据，季度更新

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	基金代码
    symbol	str	N	股票代码
    ann_date	str	N	公告日期（YYYYMMDD格式）
    period	str	N	季度（每个季度最后一天的日期，比如20131231表示2013年年报）
    start_date	str	N	报告期开始日期（YYYYMMDD格式）
    end_date	str	N	报告期结束日期（YYYYMMDD格式）
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS基金代码
    ann_date	str	Y	公告日期
    end_date	str	Y	截止日期
    symbol	str	Y	股票代码
    mkv	float	Y	持有股票市值(元)
    amount	float	Y	持有股票数量（股）
    stk_mkv_ratio	float	Y	占股票市值比
    stk_float_ratio	float	Y	占流通股本比例
    """
    return pro.fund_portfolio(**params)

def fund_daily_wrapper(params: dict):
    """
    场内基金日线行情
    接口：fund_daily
    描述：获取场内基金日线行情，类似股票日行情，包括ETF行情
    更新：每日收盘后2小时内
    限量：单次最大2000行记录，总量不限制

    复权行情实现参考：
    后复权 = 当日最新价 × 当日复权因子
    前复权 = 当日最新价 ÷ 最新复权因子

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	基金代码
    trade_date	str	N	交易日期(YYYYMMDD格式，下同)
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    
    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	TS代码
    trade_date	str	Y	交易日期
    open	float	Y	开盘价(元)
    high	float	Y	最高价(元)
    low	float	Y	最低价(元)
    close	float	Y	收盘价(元)
    pre_close	float	Y	昨收盘价(元)
    change	float	Y	涨跌额(元)
    pct_chg	float	Y	涨跌幅(%)
    vol	float	Y	成交量(手)
    amount	float	Y	成交额(千元)
    """
    return pro.fund_daily(**params)

def fund_adj_wrapper(params: dict):
    """
    基金复权因子
    接口：fund_adj
    描述：获取基金复权因子，用于计算基金复权行情
    限量：单次最大提取2000行记录，可循环提取，数据总量不限制

    复权行情实现参考：
    后复权 = 当日最新价 × 当日复权因子
    前复权 = 当日最新价 ÷ 最新复权因子

    输入参数
    名称	类型	必选	描述
    ts_code	str	N	TS基金代码（支持多只基金输入）
    trade_date	str	N	交易日期（格式：yyyymmdd，下同）
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    offset	str	N	开始行数
    limit	str	N	最大行数

    输出参数
    名称	类型	默认显示	描述
    ts_code	str	Y	ts基金代码
    trade_date	str	Y	交易日期
    adj_factor	float	Y	复权因子
    """
    return pro.fund_adj(**params)

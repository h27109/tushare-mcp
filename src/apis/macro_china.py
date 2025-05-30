from .tushare_pro import pro

def shibor_wrapper(params: dict):
    """
    Shibor利率数据
    接口：shibor
    描述：shibor利率


    Shibor利率介绍
    上海银行间同业拆放利率（Shanghai Interbank Offered Rate，简称Shibor），以位于上海的全国银行间同业拆借中心为技术平台计算、发布并命名，是由信用等级较高的银行组成报价团自主报出的人民币同业拆出利率计算确定的算术平均利率，是单利、无担保、批发性利率。目前，对社会公布的Shibor品种包括隔夜、1周、2周、1个月、3个月、6个月、9个月及1年。
    Shibor报价银行团现由18家商业银行组成。报价银行是公开市场一级交易商或外汇市场做市商，在中国货币市场上人民币交易相对活跃、信息披露比较充分的银行。中国人民银行成立Shibor工作小组，依据《上海银行间同业拆放利率（Shibor）实施准则》确定和调整报价银行团成员、监督和管理Shibor运行、规范报价行与指定发布人行为。
    全国银行间同业拆借中心受权Shibor的报价计算和信息发布。每个交易日根据各报价行的报价，剔除最高、最低各4家报价，对其余报价进行算术平均计算后，得出每一期限品种的Shibor，并于11:00对外发布。

    输入参数
    名称	类型	必选	描述
    date	str	N	日期 (日期输入格式：YYYYMMDD，下同)
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    on	float	Y	隔夜
    1w	float	Y	1周
    2w	float	Y	2周
    1m	float	Y	1个月
    3m	float	Y	3个月
    6m	float	Y	6个月
    9m	float	Y	9个月
    1y	float	Y	1年
    """
    return pro.shibor(**params)

def shibor_quote_wrapper(params: dict):
    """
    Shibor报价数据
    接口：shibor_quote
    描述：Shibor报价数据
    限量：单次最大4000行数据，总量不限制，可通过设置开始和结束日期分段获取

    输入参数
    名称	类型	必选	描述
    date	str	N	日期 (日期输入格式：YYYYMMDD，下同)
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    bank	str	N	银行名称 （中文名称，例如 农业银行）
    
    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    bank	str	Y	报价银行
    on_b	float	Y	隔夜_Bid
    on_a	float	Y	隔夜_Ask
    1w_b	float	Y	1周_Bid
    1w_a	float	Y	1周_Ask
    2w_b	float	Y	2周_Bid
    2w_a	float	Y	2周_Ask
    1m_b	float	Y	1月_Bid
    1m_a	float	Y	1月_Ask
    3m_b	float	Y	3月_Bid
    3m_a	float	Y	3月_Ask
    6m_b	float	Y	6月_Bid
    6m_a	float	Y	6月_Ask
    9m_b	float	Y	9月_Bid
    9m_a	float	Y	9月_Ask
    1y_b	float	Y	1年_Bid
    1y_a	float	Y	1年_Ask
    """
    return pro.shibor_quote(**params)

def shibor_lpr_wrapper(params: dict):
    """
    LPR贷款基础利率
    接口：shibor_lpr
    描述：LPR贷款基础利率
    限量：单次最大4000(相当于单次可提取18年历史)，总量不限制，可通过设置开始和结束日期分段获取

    LPR介绍
    贷款基础利率（Loan Prime Rate，简称LPR），是基于报价行自主报出的最优贷款利率计算并发布的贷款市场参考利率。目前，对社会公布1年期贷款基础利率。

    LPR报价银行团现由10家商业银行组成。报价银行应符合财务硬约束条件和宏观审慎政策框架要求，系统重要性程度高、市场影响力大、综合实力强，已建立内部收益率曲线和内部转移定价机制，具有较强的自主定价能力，已制定本行贷款基础利率管理办法，以及有利于开展报价工作的其他条件。市场利率定价自律机制依据《贷款基础利率集中报价和发布规则》确定和调整报价行成员，监督和管理贷款基础利率运行，规范报价行与指定发布人行为。

    全国银行间同业拆借中心受权贷款基础利率的报价计算和信息发布。每个交易日根据各报价行的报价，剔除最高、最低各1家报价，对其余报价进行加权平均计算后，得出贷款基础利率报价平均利率，并于11:30对外发布。

    输入参数
    名称	类型	必选	描述
    date	str	N	日期 (日期输入格式：YYYYMMDD，下同)
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    1y	float	Y	1年贷款利率
    5y	float	Y	5年贷款利率
    """
    return pro.shibor_lpr(**params)

def libor_wrapper(params: dict):
    """
    Libor拆借利率
    接口：libor
    描述：Libor拆借利率
    限量：单次最大4000行数据，总量不限制，可通过设置开始和结束日期分段获取

    Libor（London Interbank Offered Rate ），即伦敦同业拆借利率，是指伦敦的第一流银行之间短期资金借贷的利率，是国际金融市场中大多数浮动利率的基础利率。作为银行从市场上筹集资金进行转贷的融资成本，贷款协议中议定的LIBOR通常是由几家指定的参考银行，在规定的时间（一般是伦敦时间上午11：00）报价的平均利率。

    输入参数
    名称	类型	必选	描述
    date	str	N	日期 (日期输入格式：YYYYMMDD，下同)
    start_date	str	N	开始日期
    end_date	str	N	结束日期
    curr_type	str	N	货币代码 (USD美元 EUR欧元 JPY日元 GBP英镑 CHF瑞郎，默认是USD)

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    curr_type	str	Y	货币
    on	float	Y	隔夜
    1w	float	Y	1周
    1m	float	Y	1个月
    2m	float	Y	2个月
    3m	float	Y	3个月
    6m	float	Y	6个月
    12m	float	Y	12个月
    """
    return pro.libor(**params)

def hibor_wrapper(params: dict):
    """
    Hibor利率
    接口：hibor
    描述：Hibor利率
    限量：单次最大4000行数据，总量不限制，可通过设置开始和结束日期分段获取

    HIBOR (Hongkong InterBank Offered Rate)，是香港银行同行业拆借利率。指香港货币市场上，银行与银行之间的一年期以下的短期资金借贷利率，从伦敦同业拆借利率（LIBOR）变化出来的。

    输入参数
    名称	类型	必选	描述
    date	str	N	日期 (日期输入格式：YYYYMMDD，下同)
    start_date	str	N	开始日期
    end_date	str	N	结束日期

    输出参数
    名称	类型	默认显示	描述
    date	str	Y	日期
    on	float	Y	隔夜
    1w	float	Y	1周
    2w	float	Y	2周
    1m	float	Y	1个月
    2m	float	Y	2个月
    3m	float	Y	3个月
    6m	float	Y	6个月
    12m	float	Y	12个月
    """
    return pro.hibor(**params)

def cn_gdp_wrapper(params: dict):
    """
    GDP数据
    接口：cn_gdp
    描述：获取国民经济之GDP数据
    限量：单次最大10000，一次可以提取全部数据

    输入参数
    名称	类型	必选	描述
    q	str	N	季度（2019Q1表示，2019年第一季度）
    start_q	str	N	开始季度
    end_q	str	N	结束季度
    fields	str	N	指定输出字段（e.g. fields='quarter,gdp,gdp_yoy'）

    输出参数
    名称	类型	默认显示	描述
    quarter	str	Y	季度
    gdp	float	Y	GDP累计值（亿元）
    gdp_yoy	float	Y	当季同比增速（%）
    pi	float	Y	第一产业累计值（亿元）
    pi_yoy	float	Y	第一产业同比增速（%）
    si	float	Y	第二产业累计值（亿元）
    si_yoy	float	Y	第二产业同比增速（%）
    ti	float	Y	第三产业累计值（亿元）
    ti_yoy	float	Y	第三产业同比增速（%）
    """
    return pro.cn_gdp(**params)

def cpi_wrapper(params: dict):
    """
    居民消费价格指数
    接口：cn_cpi
    描述：获取CPI居民消费价格数据，包括全国、城市和农村的数据
    限量：单次最大5000行，一次可以提取全部数据

    输入参数
    名称	类型	必选	描述
    m	str	N	月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔
    start_m	str	N	开始月份
    end_m	str	N	结束月份

    输出参数
    名称	类型	默认显示	描述
    month	str	Y	月份YYYYMM
    nt_val	float	Y	全国当月值
    nt_yoy	float	Y	全国同比（%）
    nt_mom	float	Y	全国环比（%）
    nt_accu	float	Y	全国累计值
    town_val	float	Y	城市当月值
    town_yoy	float	Y	城市同比（%）
    town_mom	float	Y	城市环比（%）
    town_accu	float	Y	城市累计值
    cnt_val	float	Y	农村当月值
    cnt_yoy	float	Y	农村同比（%）
    cnt_mom	float	Y	农村环比（%）
    cnt_accu	float	Y	农村累计值
    """
    return pro.cn_cpi(**params)

def ppi_wrapper(params: dict):
    """
    工业生产者出厂价格指数
    接口：cn_ppi
    描述：获取PPI工业生产者出厂价格指数数据
    限量：单次最大5000，一次可以提取全部数据
    权限：用户600积分可以使用，具体请参阅积分获取办法

    输入参数

    名称	类型	必选	描述
    m	str	N	月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔
    start_m	str	N	开始月份
    end_m	str	N	结束月份
    输出参数

    名称	类型	默认显示	描述
    month	str	Y	月份YYYYMM
    ppi_yoy	float	Y	PPI：全部工业品：当月同比
    ppi_mp_yoy	float	Y	PPI：生产资料：当月同比
    ppi_mp_qm_yoy	float	Y	PPI：生产资料：采掘业：当月同比
    ppi_mp_rm_yoy	float	Y	PPI：生产资料：原料业：当月同比
    ppi_mp_p_yoy	float	Y	PPI：生产资料：加工业：当月同比
    ppi_cg_yoy	float	Y	PPI：生活资料：当月同比
    ppi_cg_f_yoy	float	Y	PPI：生活资料：食品类：当月同比
    ppi_cg_c_yoy	float	Y	PPI：生活资料：衣着类：当月同比
    ppi_cg_adu_yoy	float	Y	PPI：生活资料：一般日用品类：当月同比
    ppi_cg_dcg_yoy	float	Y	PPI：生活资料：耐用消费品类：当月同比
    ppi_mom	float	Y	PPI：全部工业品：环比
    ppi_mp_mom	float	Y	PPI：生产资料：环比
    ppi_mp_qm_mom	float	Y	PPI：生产资料：采掘业：环比
    ppi_mp_rm_mom	float	Y	PPI：生产资料：原料业：环比
    ppi_mp_p_mom	float	Y	PPI：生产资料：加工业：环比
    ppi_cg_mom	float	Y	PPI：生活资料：环比
    ppi_cg_f_mom	float	Y	PPI：生活资料：食品类：环比
    ppi_cg_c_mom	float	Y	PPI：生活资料：衣着类：环比
    ppi_cg_adu_mom	float	Y	PPI：生活资料：一般日用品类：环比
    ppi_cg_dcg_mom	float	Y	PPI：生活资料：耐用消费品类：环比
    ppi_accu	float	Y	PPI：全部工业品：累计同比
    ppi_mp_accu	float	Y	PPI：生产资料：累计同比
    ppi_mp_qm_accu	float	Y	PPI：生产资料：采掘业：累计同比
    ppi_mp_rm_accu	float	Y	PPI：生产资料：原料业：累计同比
    ppi_mp_p_accu	float	Y	PPI：生产资料：加工业：累计同比
    ppi_cg_accu	float	Y	PPI：生活资料：累计同比
    ppi_cg_f_accu	float	Y	PPI：生活资料：食品类：累计同比
    ppi_cg_c_accu	float	Y	PPI：生活资料：衣着类：累计同比
    ppi_cg_adu_accu	float	Y	PPI：生活资料：一般日用品类：累计同比
    ppi_cg_dcg_accu	float	Y	PPI：生活资料：耐用消费品类：累计同比
    """
    return pro.cn_ppi(**params)

def cn_m_wrapper(params: dict):
    """
    货币供应量
    接口：cn_m
    描述：获取货币供应量之月度数据
    限量：单次最大5000，一次可以提取全部数据

    输入参数
    名称	类型	必选	描述
    m	str	N	月度（202001表示，2020年1月）
    start_m	str	N	开始月度
    end_m	str	N	结束月度
    fields	str	N	指定输出字段（e.g. fields='month,m0,m1,m2'）
    
    输出参数
    名称	类型	默认显示	描述
    month	str	Y	月份YYYYMM
    m0	float	Y	M0（亿元）
    m0_yoy	float	Y	M0同比（%）
    m0_mom	float	Y	M0环比（%）
    m1	float	Y	M1（亿元）
    m1_yoy	float	Y	M1同比（%）
    m1_mom	float	Y	M1环比（%）
    m2	float	Y	M2（亿元）
    m2_yoy	float	Y	M2同比（%）
    m2_mom	float	Y	M2环比（%）
    """
    return pro.cn_m(**params)

def sf_month_wrapper(params: dict):
    """
    社融数据（月度）
    接口：sf_month
    描述：获取月度社会融资数据
    限量：单次最大2000条数据，可循环提取

    输入参数
    名称	类型	必选	描述
    m	str	N	月份（YYYYMM，下同），支持多个月份同时输入，逗号分隔
    start_m	str	N	开始月份
    end_m	str	N	结束月份

    输出参数
    名称	类型	默认显示	描述
    month	str	Y	月度
    inc_month	float	Y	社融增量当月值（亿元）
    inc_cumval	float	Y	社融增量累计值（亿元）
    stk_endval	float	Y	社融存量期末值（万亿元）
    """
    return pro.sf_month(**params)

def cn_pmi_wrapper(params: dict):
    """
    采购经理人指数
    接口：cn_pmi
    描述：采购经理人指数
    限量：单次最大2000，一次可以提取全部数据

    输入参数
    名称	类型	必选	描述
    m	str	N	月度（202401表示，2024年1月）
    start_m	str	N	开始月度
    end_m	str	N	结束月度（e.g. fields='month,pmi010000,pmi010400'）
    
    输出参数
    名称	类型	默认显示	描述
    month	str	N	月份YYYYMM
    pmi010000	float	N	制造业PMI
    pmi010100	float	N	制造业PMI:企业规模/大型企业
    pmi010200	float	N	制造业PMI:企业规模/中型企业
    pmi010300	float	N	制造业PMI:企业规模/小型企业
    pmi010400	float	N	制造业PMI:构成指数/生产指数
    pmi010401	float	N	制造业PMI:构成指数/生产指数:企业规模/大型企业
    pmi010402	float	N	制造业PMI:构成指数/生产指数:企业规模/中型企业
    pmi010403	float	N	制造业PMI:构成指数/生产指数:企业规模/小型企业
    pmi010500	float	N	制造业PMI:构成指数/新订单指数
    pmi010501	float	N	制造业PMI:构成指数/新订单指数:企业规模/大型企业
    pmi010502	float	N	制造业PMI:构成指数/新订单指数:企业规模/中型企业
    pmi010503	float	N	制造业PMI:构成指数/新订单指数:企业规模/小型企业
    pmi010600	float	N	制造业PMI:构成指数/供应商配送时间指数
    pmi010601	float	N	制造业PMI:构成指数/供应商配送时间指数:企业规模/大型企业
    pmi010602	float	N	制造业PMI:构成指数/供应商配送时间指数:企业规模/中型企业
    pmi010603	float	N	制造业PMI:构成指数/供应商配送时间指数:企业规模/小型企业
    pmi010700	float	N	制造业PMI:构成指数/原材料库存指数
    pmi010701	float	N	制造业PMI:构成指数/原材料库存指数:企业规模/大型企业
    pmi010702	float	N	制造业PMI:构成指数/原材料库存指数:企业规模/中型企业
    pmi010703	float	N	制造业PMI:构成指数/原材料库存指数:企业规模/小型企业
    pmi010800	float	N	制造业PMI:构成指数/从业人员指数
    pmi010801	float	N	制造业PMI:构成指数/从业人员指数:企业规模/大型企业
    pmi010802	float	N	制造业PMI:构成指数/从业人员指数:企业规模/中型企业
    pmi010803	float	N	制造业PMI:构成指数/从业人员指数:企业规模/小型企业
    pmi010900	float	N	制造业PMI:其他/新出口订单
    pmi011000	float	N	制造业PMI:其他/进口
    pmi011100	float	N	制造业PMI:其他/采购量
    pmi011200	float	N	制造业PMI:其他/主要原材料购进价格
    pmi011300	float	N	制造业PMI:其他/出厂价格
    pmi011400	float	N	制造业PMI:其他/产成品库存
    pmi011500	float	N	制造业PMI:其他/在手订单
    pmi011600	float	N	制造业PMI:其他/生产经营活动预期
    pmi011700	float	N	制造业PMI:分行业/装备制造业
    pmi011800	float	N	制造业PMI:分行业/高技术制造业
    pmi011900	float	N	制造业PMI:分行业/基础原材料制造业
    pmi012000	float	N	制造业PMI:分行业/消费品制造业
    pmi020100	float	N	非制造业PMI:商务活动
    pmi020101	float	N	非制造业PMI:商务活动:分行业/建筑业
    pmi020102	float	N	非制造业PMI:商务活动:分行业/服务业业
    pmi020200	float	N	非制造业PMI:新订单指数
    pmi020201	float	N	非制造业PMI:新订单指数:分行业/建筑业
    pmi020202	float	N	非制造业PMI:新订单指数:分行业/服务业
    pmi020300	float	N	非制造业PMI:投入品价格指数
    pmi020301	float	N	非制造业PMI:投入品价格指数:分行业/建筑业
    pmi020302	float	N	非制造业PMI:投入品价格指数:分行业/服务业
    pmi020400	float	N	非制造业PMI:销售价格指数
    pmi020401	float	N	非制造业PMI:销售价格指数:分行业/建筑业
    pmi020402	float	N	非制造业PMI:销售价格指数:分行业/服务业
    pmi020500	float	N	非制造业PMI:从业人员指数
    pmi020501	float	N	非制造业PMI:从业人员指数:分行业/建筑业
    pmi020502	float	N	非制造业PMI:从业人员指数:分行业/服务业
    pmi020600	float	N	非制造业PMI:业务活动预期指数
    pmi020601	float	N	非制造业PMI:业务活动预期指数:分行业/建筑业
    pmi020602	float	N	非制造业PMI:业务活动预期指数:分行业/服务业
    pmi020700	float	N	非制造业PMI:新出口订单
    pmi020800	float	N	非制造业PMI:在手订单
    pmi020900	float	N	非制造业PMI:存货
    pmi021000	float	N	非制造业PMI:供应商配送时间
    pmi030000	float	N	中国综合PMI:产出指数
    """
    return pro.cn_pmi(**params)
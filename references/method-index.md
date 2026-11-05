# Pandadata Method Index

Generated from `api-docs.md`. Use line numbers with `sed -n '<line>,+120p' references/api-docs.md`, or run `python scripts/search_api_docs.py --method <method>`.

Total methods: 323

SDK 1.0.6 directly exports 323 of these documented methods.
All indexed methods are exported; server availability still depends on the service and account.



| Category | Section | Method | Summary | API docs line |
|---|---|---|---|---:|
| 交易工具 | 交易日历 | `get_trade_cal` | 获取交易日历 | 10 |
| 交易工具 | 某一日期前第 n 个交易日 | `get_prev_trade_date` | 获取指定日期的前第n个交易日 | 72 |
| 交易工具 | 最新交易日 | `get_last_trade_date` | 获取最新交易日 | 112 |
| 交易工具 | 合约特殊处理数据 | `get_stock_status_change` | 获取合约特殊处理数据 | 148 |
| 交易工具 | 指定日期的在售股票列表 | `get_trade_list` | 获取指定日期的在售股票列表 | 195 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily` | 获取A股日线数据 | 434 |
| A股数据 | 沪深股票行情数据 | `get_stock_rt_daily` | 获取A股当日日线 | 507 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily_pre` | 获取A股前复权日线数据 | 750 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily_post` | 获取A股后复权日线数据 | 822 |
| A股数据 | 沪深股票行情数据 | `get_stock_min` | 获取A股分钟线 | 894 |
| A股数据 | 沪深股票行情数据 | `get_stock_rt_min` | 获取A股当日分钟线 | 1147 |
| A股数据 | 概念基础数据 | `get_concept_list` | 获取概念列表 | 1256 |
| A股数据 | 概念基础数据 | `get_concept_constituents` | 获取概念成分股 | 1295 |
| A股数据 | 市场参考数据 | `get_stock_detail` | 获取股票基本信息 | 1407 |
| A股数据 | 市场参考数据 | `get_index_detail` | 获取指数基本信息 | 1465 |
| A股数据 | 行业基础数据 | `get_industry_constituents` | 获取行业成分股数据 | 1713 |
| A股数据 | 行业基础数据 | `get_industry_detail` | 获取行业基本信息数据 | 1764 |
| A股数据 | 行业基础数据 | `get_stock_industry` | 获取指定股票所属的行业信息 | 1839 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_daily` | 获取指数日线 | 1887 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_min` | 获取指数分钟线 | 1952 |
| A股数据 | 指数基础数据 | `get_index_weights` | 获取指数权重信息数据 | 2207 |
| A股数据 | 指数基础数据 | `get_index_indicator` | 获取指数估值指标数据 | 2451 |
| A股数据 | 市场交易与资金数据 | `get_lhb_list` | 获取股票龙虎榜数据 | 2698 |
| A股数据 | 市场交易与资金数据 | `get_lhb_detail` | 获取股票龙虎榜明细数据 | 2925 |
| A股数据 | 市场交易与资金数据 | `get_margin` | 获取融资融券信息 | 2991 |
| A股数据 | 市场交易与资金数据 | `get_hsgt_hold` | 获取沪深股通持股信息 | 3060 |
| A股数据 | 公司行为 | `get_investor_activity` | 获取A股合约投资者关系活动 | 3106 |
| A股数据 | 公司行为 | `get_restricted_list` | 获取股票限售解禁明细数据 | 3150 |
| A股数据 | 公司行为 | `get_repurchase` | 获取回购数据 | 3203 |
| A股数据 | 公司行为 | `get_holder_count` | 获取股东数量 | 3268 |
| A股数据 | 公司行为 | `get_top_holders` | 获取A股股东信息 | 3317 |
| A股数据 | 公司行为 | `get_block_trade` | 获取A股大宗交易信息 | 3386 |
| A股数据 | 公司行为 | `get_share_float` | 获取股票股本数据 | 3434 |
| A股数据 | 公司行为 | `get_stock_dividend` | 获取股票分红信息 | 3641 |
| A股数据 | 公司行为 | `get_stock_split` | 获取股票拆分数据 | 3688 |
| A股数据 | 公司行为 | `get_stock_cash_dividend` | 获取股票现金分红数据 | 3734 |
| A股数据 | 公司行为 | `get_stock_dividend_amount` | 获取股票分红总额数据 | 3785 |
| A股数据 | 公司行为 | `get_stock_private_placement` | 获取股票定向增发数据 | 3833 |
| A股数据 | 公司行为 | `get_stock_allotment` | 获取股票配股信息 | 3883 |
| A股数据 | 公司行为 | `get_stock_disclosure_date` | 获取上市A股定期报告预披露数据 | 3933 |
| A股数据 | 公司行为 | `get_stock_status_over_allotment` | 获取超额配售权实施情况数据 | 3984 |
| A股数据 | 公司行为 | `get_stock_litigation_arbitration` | 获取上市公司诉讼仲裁数据 | 4041 |
| A股数据 | 公司行为 | `get_stock_csrc_approval` | 获取证监会批文数据 | 4103 |
| A股数据 | 公司行为 | `get_stock_competitor_information` | 获取竞争企业信息数据 | 4153 |
| A股数据 | 公司行为 | `get_stock_intermediary_information` | 获取中介情况信息表数据 | 4201 |
| A股数据 | 公司行为 | `get_stock_rela_party_trans` | 上市公司关联交易 | 4251 |
| A股数据 | 公司行为 | `get_cumu_guarantee` | 获取累计担保信息 | 4318 |
| A股数据 | 公司行为 | `get_stock_material_contract` | 获取上市公司重大合同数据 | 4396 |
| A股数据 | 公司行为 | `get_investor_brief_detail` | 获取投资者简报详情 | 4474 |
| A股数据 | 公司行为 | `get_investor_brief_qa` | 获取投资者简报问答 | 4719 |
| A股数据 | 公司行为 | `get_stock_equity_illegal` | 获取股权违规信息 | 4966 |
| A股数据 | 股东行为 | `get_stock_pledge` | 获取A股公司股权质押 | 5220 |
| A股数据 | 股东行为 | `get_stock_pledge_stat` | 获取股票质押信息统计 | 5478 |
| A股数据 | 股东行为 | `get_stock_shareholder_change` | 获取股东增减持计划 | 5723 |
| A股数据 | 股东行为 | `get_stock_equity_placard` | 获取被举牌公司明细 | 5984 |
| A股数据 | 业绩预告 | `get_fina_forecast` | 获取业绩预告数据 | 6047 |
| A股数据 | 财务三表、财务快报 | `get_fina_performance` | 获取财务快报数据 | 6104 |
| A股数据 | 财务三表、财务快报 | `get_fina_reports` | 获取财务季度报告 | 6187 |
| A股数据 | 财务三表、财务快报 | `get_audit_opinion` | 获取财务报告审计意见 | 6273 |
| A股数据 | 股东结构 | `get_stock_equity_nature` | 获取个股企业性质 | 6327 |
| 期货数据 | 期货行情数据 | `get_future_daily` | 获取期货日线 | 6570 |
| 期货数据 | 期货行情数据 | `get_future_daily_post` | 获取期货后复权数据 | 6644 |
| 期货数据 | 期货行情数据 | `get_future_min` | 获取期货分钟线 | 6734 |
| 期货数据 | 期货基本信息 | `get_future_detail` | 获取期货基本信息 | 6995 |
| 期货数据 | 期货主力合约信息 | `get_future_dominant` | 获取期货主力合约数据 | 7056 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg` | 获取席位净持仓保证金数据 | 7114 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netposi_rank` | 获取期货商品净持仓多空榜单数据 | 7357 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg_change` | 获取席位净持仓保证金变化数据 | 7586 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_grade` | 获取席位评级数据 | 7829 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_totlmarg` | 获取席位总持仓保证金数据 | 7890 |
| 期货数据 | 期货 DeepView 数据 | `get_future_basis` | 获取期货基差数据 | 8133 |
| 期货数据 | 期货 DeepView 数据 | `get_future_warehouse_receipt` | 获取期货仓单数据 | 8194 |
| 期货数据 | 期货 DeepView 数据 | `get_future_net_flow` | 获取期货净资金流列表 | 8255 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_indicators` | 获取期货龙虎比、牛熊线 | 8302 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_variety_profit` | 获取期货席位的商品盈亏数据 | 8371 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_posi` | 获取期货商品持仓数据 | 8426 |
| 期货数据 | 期货 DeepView 数据 | `get_future_symbol_posi` | 获取期货合约持仓数据 | 8484 |
| 期货数据 | 期货 DeepView 数据 | `get_future_ls_ratio` | 获取期货合约多空比数据 | 8541 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netcap_change` | 获取期货合约净持仓市值变化数据 | 8780 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_rank` | 获取期货合约龙虎比、牛熊线排行 | 9022 |
| 期货数据 | 期货 DeepView 数据 | `get_future_term_structure` | 获取期货期限结构数据 | 9273 |
| 期货数据 | 期货 DeepView 数据 | `get_future_inventory` | 获取期货库存数据 | 9315 |
| 期货数据 | 期货 DeepView 数据 | `get_future_calendar_arbitrage` | 获取期货跨期套利数据 | 9357 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_spread` | 获取期货自由价差数据 | 9400 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_ratio` | 获取期货自由价比数据 | 9443 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_oi_value` | 获取期货席位合约的总持仓市值 | 9486 |
| 期货数据 | 期货 DeepView 数据 | `get_future_nonbroker_net` | 获取期货非期货公司净持仓 | 9533 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit` | 获取期货席位盈亏数据 | 9576 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_flow_daily` | 获取期货席位每日大资金流动数据 | 9621 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_ls_ratio` | 获取期货席位多空比数据 | 9671 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_loss_rank` | 获取期货席位亏损排行数据 | 9717 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit_rank` | 获取期货席位盈利排行数据 | 9758 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_build_process` | 获取期货席位建仓过程数据 | 9799 |
| 期货数据 | 期货 DeepView 数据 | `get_future_trader_quote` | 获取期货现货贸易商报价数据 | 10046 |
| 期货数据 | 期货 DeepView 数据 | `get_future_virtual_ratio` | 获取期货虚实盘比数据 | 10290 |
| 期货数据 | 期货 DeepView 数据 | `get_future_spot_profit` | 获取期货利润数据 | 10333 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_mcap` | 获取期货品种持仓市值数据 | 10377 |
| 期货数据 | 期货 DeepView 数据 | `get_future_dominant_corr` | 获取期货主力合约涨跌幅相关性 | 10418 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_pool` | 获取期货多头空头合约池 | 10456 |
| 期权数据 | 期权基本信息 | `get_option_detail` | 获取期权基本信息 | 10509 |
| 期权数据 | 期权基本信息 | `get_option_underlying_detail` | 获取期权品种信息 | 10764 |
| 期权数据 | 期权基本信息 | `get_option_exercise` | 获取期权行权交收信息 | 10819 |
| 期权数据 | 期权基本信息 | `get_option_static` | 获取期权每日盘前静态数据 | 10864 |
| 期权数据 | 期权日线行情 | `get_option_daily` | 获取期权日线数据 | 10944 |
| 期权数据 | 期权日线行情 | `get_option_spot_market` | 获取期权现货日行情 | 11196 |
| 期权数据 | 期权波动率数据 | `get_option_implied_volatility` | 获取期权隐含波动率 | 11274 |
| 期权数据 | 期权波动率数据 | `get_option_underlying_volatility` | 获取期权标的历史波动率 | 11315 |
| 期权数据 | 期权波动率数据 | `get_option_risk_indicators` | 获取期权风险指标 | 11442 |
| 量化因子数据 | 回测因子 | `get_factor` | 获取回测因子 | 11496 |
| 量化因子数据 | 复权因子 | `get_adj_factor` | 获取复权因子 | 11579 |
| 港美股 | 行情数据 | `get_hk_daily` | 获取港股日线数据 | 11628 |
| 港美股 | 行情数据 | `get_us_daily` | 获取美股日线数据 | 11894 |
| 港美股 | 港股股票基础信息 | `get_hk_detail` | 获取港股的基本信息 | 12150 |
| 港美股 | 美股股票基础信息 | `get_us_detail` | 获取美股的基本信息 | 12215 |
| 港美股 | 港股公司事件 | `get_stock_dividend_event` | 获取股票分红相关的事件 | 12277 |
| 港美股 | 港股公司事件 | `get_stock_market_event` | 获取市场活动相关的事件 | 12327 |
| 港美股 | 港股公司事件 | `get_stock_meeting_event` | 获取公司会议相关的事件 | 12573 |
| 港美股 | 港股公司事件 | `get_stock_financial_event` | 获取财务披露相关的事件 | 12819 |
| 港美股 | 港股公司事件 | `get_stock_ir_event` | 获取投资者关系活动相关的事件 | 13065 |
| 港美股 | 美股公司事件 | `get_stock_dividend_activity` | 获取股票分红相关的事件 | 13313 |
| 港美股 | 美股公司事件 | `get_stock_market_activity` | 获取市场活动相关的事件 | 13363 |
| 港美股 | 美股公司事件 | `get_stock_meeting_activity` | 获取公司会议相关的事件 | 13609 |
| 港美股 | 美股公司事件 | `get_stock_financial_activity` | 获取财务披露相关的事件 | 13855 |
| 港美股 | 美股公司事件 | `get_stock_ir_activity` | 获取投资者关系活动相关的事件 | 14101 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_concentration` | 获取公司投资者集中度 | 14349 |
| 港美股 | 港股股东与投资者 | `get_stock_top20_concentration` | 获取公司前20投资者集中度 | 14589 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_ranking` | 获取公司投资者排行 | 14829 |
| 港美股 | 港股股东与投资者 | `get_stock_insider_trade` | 获取公司内部人交易活动 | 15075 |
| 港美股 | 港股股东与投资者 | `get_stock_shareholder_holding` | 获取公司股东持股报告 | 15142 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_centralization` | 获取公司投资者集中度 | 15209 |
| 港美股 | 美股股东与投资者 | `get_stock_top20_centralization` | 获取公司前20投资者集中度 | 15449 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_leaderboard` | 获取公司投资者排行 | 15689 |
| 港美股 | 美股股东与投资者 | `get_stock_insider_transaction` | 获取公司内部人交易活动 | 15935 |
| 港美股 | 美股股东与投资者 | `get_stock_shareholder_report` | 获取公司股东持股报告 | 16066 |
| 港美股 | 港股核心数据 | `get_stock_industry_median` | 获取公司最新行业中位统计数据 | 16143 |
| 港美股 | 港股核心数据 | `get_stock_pv_indicator` | 获取公司最新价量指标数据 | 16584 |
| 港美股 | 美股核心数据 | `get_stock_sector_median` | 获取公司最新行业中位统计数据 | 16848 |
| 港美股 | 美股核心数据 | `get_stock_pv_metric` | 获取公司最新价量指标数据 | 17289 |
| 港美股 | 港股一致预期数据 | `get_stock_ncycl_consensus` | 获取非周期性指标一致预期 | 17553 |
| 港美股 | 港股一致预期数据 | `get_stock_recommendation_consensus` | 获取买卖建议一致预期 | 17797 |
| 港美股 | 美股一致预期数据 | `get_stock_ncycl_estimate` | 获取非周期性指标一致预期 | 18046 |
| 港美股 | 美股一致预期数据 | `get_stock_recommendation_estimate` | 获取买卖建议一致预期 | 18290 |
| 港美股 | 港股财务数据 | `get_stock_operating_indicator` | 获取公司标准化营运指标 | 18539 |
| 港美股 | 港股财务数据 | `get_stock_mktfin_indicator` | 获取公司最新市场财务统计指标 | 18791 |
| 港美股 | 港股财务数据 | `get_fina_statement` | 获取财务季度报告 | 19173 |
| 港美股 | 美股财务数据 | `get_stock_operating_metric` | 获取公司标准化营运指标 | 19223 |
| 港美股 | 美股财务数据 | `get_stock_mktfin_metric` | 获取公司最新市场财务统计指标 | 19475 |
| 港美股 | 美股财务数据 | `get_fina_ex` | 获取财务季度报告 | 19857 |
| 宏观数据 | 宏观指标基础信息 | `get_macro_detail` | 宏观指标列表 | 19909 |
| 宏观数据 | 中国宏观指标 | `get_macro_na` | 中国宏观-国民经济核算 | 20165 |
| 宏观数据 | 中国宏观指标 | `get_macro_in` | 中国宏观-工业 | 20208 |
| 宏观数据 | 中国宏观指标 | `get_macro_ci` | 中国宏观-景气指数 | 20251 |
| 宏观数据 | 中国宏观指标 | `get_macro_pi` | 中国宏观-价格指数 | 20293 |
| 宏观数据 | 中国宏观指标 | `get_macro_fa` | 中国宏观-固定资产投资 | 20335 |
| 宏观数据 | 中国宏观指标 | `get_macro_fi` | 中国宏观-财政 | 20377 |
| 宏观数据 | 中国宏观指标 | `get_macro_mb` | 中国宏观-货币与银行 | 20419 |
| 宏观数据 | 中国宏观指标 | `get_macro_ir` | 中国宏观-利率汇率 | 20462 |
| 宏观数据 | 中国宏观指标 | `get_macro_fe` | 中国宏观-对外经济 | 20505 |
| 宏观数据 | 中国宏观指标 | `get_macro_dt` | 中国宏观-国内贸易 | 20547 |
| 宏观数据 | 中国宏观指标 | `get_macro_ew` | 中国宏观-就业与工资 | 20590 |
| 宏观数据 | 中国宏观指标 | `get_macro_li` | 中国宏观-人民生活 | 20633 |
| 宏观数据 | 中国宏观指标 | `get_macro_pr` | 中国宏观-人口与资源 | 20676 |
| 宏观数据 | 中国宏观指标 | `get_macro_se` | 中国宏观-科教体卫 | 20718 |
| 宏观数据 | 中国宏观指标 | `get_macro_sm` | 中国宏观-证券市场 | 20762 |
| 宏观数据 | 中国宏观指标 | `get_macro_pm` | 中国宏观-区域宏观 | 20805 |
| 宏观数据 | 国际宏观指标 | `get_macro_gb` | 宏观行业-国际宏观 | 20851 |
| 宏观数据 | 宏观行业数据 | `get_macro_ag` | 宏观行业-农林牧渔 | 20896 |
| 宏观数据 | 宏观行业数据 | `get_macro_en` | 宏观行业-能源 | 20939 |
| 宏观数据 | 宏观行业数据 | `get_macro_ch` | 宏观行业-化工 | 20982 |
| 宏观数据 | 宏观行业数据 | `get_macro_st` | 宏观行业-钢铁 | 21025 |
| 宏观数据 | 宏观行业数据 | `get_macro_nf` | 宏观行业-有色金属 | 21069 |
| 宏观数据 | 宏观行业数据 | `get_macro_bm` | 宏观行业-建材 | 21111 |
| 宏观数据 | 宏观行业数据 | `get_macro_au` | 宏观行业-汽车 | 21153 |
| 宏观数据 | 宏观行业数据 | `get_macro_me` | 宏观行业-机械设备 | 21195 |
| 宏观数据 | 宏观行业数据 | `get_macro_ee` | 宏观行业-电子电器 | 21238 |
| 宏观数据 | 宏观行业数据 | `get_macro_tm` | 宏观行业-TMT | 21281 |
| 宏观数据 | 宏观行业数据 | `get_macro_fb` | 宏观行业-食品饮料 | 21323 |
| 宏观数据 | 宏观行业数据 | `get_macro_te` | 宏观行业-纺织服装 | 21366 |
| 宏观数据 | 宏观行业数据 | `get_macro_pp` | 宏观行业-造纸印刷 | 21408 |
| 宏观数据 | 宏观行业数据 | `get_macro_ph` | 宏观行业-医药生物 | 21450 |
| 宏观数据 | 宏观行业数据 | `get_macro_ut` | 宏观行业-公用事业 | 21493 |
| 宏观数据 | 宏观行业数据 | `get_macro_tr` | 宏观行业-交通运输 | 21536 |
| 宏观数据 | 宏观行业数据 | `get_macro_rc` | 宏观行业-房地产及建筑业 | 21579 |
| 宏观数据 | 宏观行业数据 | `get_macro_th` | 宏观行业-旅游酒店 | 21622 |
| 宏观数据 | 宏观行业数据 | `get_macro_ce` | 宏观行业-文教体娱及工艺品 | 21664 |
| 宏观数据 | 宏观行业数据 | `get_macro_wr` | 宏观行业-批发零售业 | 21706 |
| 宏观数据 | 宏观行业数据 | `get_macro_fs` | 宏观行业-金融保险业 | 21748 |
| 宏观数据 | 宏观行业数据 | `get_macro_is` | 宏观行业-行业综合 | 21791 |
| 宏观数据 | 宏观特色数据 | `get_macro_ec` | 宏观特色数据-线上电商数据 | 21836 |
| 宏观数据 | 宏观特色数据 | `get_macro_md` | 宏观特色数据-医药数据 | 21878 |
| 宏观数据 | 宏观特色数据 | `get_macro_eh` | 宏观特色数据-能化数据 | 21920 |
| 宏观数据 | 宏观特色数据 | `get_macro_ad` | 宏观特色数据-汽车数据 | 21963 |
| 宏观数据 | 宏观特色数据 | `get_macro_ha` | 宏观特色数据-家电数据 | 22005 |
| 宏观数据 | 宏观特色数据 | `get_macro_of` | 宏观特色数据-线下商超数据 | 22047 |
| 宏观数据 | 宏观特色数据 | `get_macro_rb` | 宏观特色数据-招聘数据 | 22089 |
| 宏观数据 | 宏观特色数据 | `get_macro_re` | 宏观特色数据-房地产数据 | 22132 |
| 宏观数据 | 宏观特色数据 | `get_macro_ed` | 宏观特色数据-电子数据 | 22175 |
| 宏观数据 | 宏观特色数据 | `get_macro_ep` | 宏观特色数据-电新数据 | 22217 |
| 宏观数据 | 宏观特色数据 | `get_macro_ar` | 宏观特色数据-农业数据 | 22260 |
| 宏观数据 | 宏观特色数据 | `get_macro_cm` | 宏观特色数据-大宗数据 | 22303 |
| 宏观数据 | 宏观经济日历 | `get_macro_cal` | 宏观经济日历 | 22348 |
| 宏观数据 | 宏观经济日历信息 | `get_macro_cal_info` | 宏观经济日历信息 | 22419 |
| 宏观数据 | 宏观经济日历配置 | `get_macro_cal_config` | 宏观经济日历配置 | 22471 |
| 基金数据 | 基金基础数据 | `get_fund_detail` | 获取基金基本信息 | 22515 |
| 基金数据 | 基金行情数据 | `get_fund_daily` | 获取场内基金日行情数据 | 22825 |
| 基金数据 | 基金行情数据 | `get_fund_daily_post` | 获取场内基金后复权日行情数据 | 22936 |
| 基金数据 | 基金行情数据 | `get_fund_daily_pre` | 获取场内基金前复权日行情数据 | 23142 |
| 基金数据 | ETF数据 | `get_fund_etf_cr_limits` | 获取ETF申赎限制数据 | 23350 |
| 基金数据 | ETF数据 | `get_fund_etf_cr_net` | 获取ETF净申赎数据 | 23422 |
| 基金数据 | ETF数据 | `get_fund_etf_constituents` | 获取ETF基金申赎清单成分券信息 | 23499 |
| 基金数据 | ETF数据 | `get_fund_etf_cr` | 获取ETF基金申赎清单数据 | 23569 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_dividend` | 获取优先股分红 | 23647 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_trading` | 获取优先股成交统计信息 | 23725 |
| 优先股数据 | 优先股数据 | `get_stock_issuer_credit_rating` | 获取优先股发行主体信用评级 | 23792 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_rating` | 获取优先股评级情况 | 23861 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_shares` | 获取优先股股本 | 23913 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_placement` | 获取优先股配售结果 | 23979 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_detail` | 获取优先股基本资料 | 24043 |
| SDK 1.0.4 补充接口 | - | `get_adj_factor_hk` | 获取港股自研复权因子数据 | 24156 |
| SDK 1.0.4 补充接口 | - | `get_factor_exposure_style` | 获取 CNE 风格因子暴露宽表 | 24182 |
| SDK 1.0.4 补充接口 | - | `get_factor_hk` | 获取港股因子数据（服务端 /hkMarket/getFactorHk） | 24215 |
| SDK 1.0.4 补充接口 | - | `get_fund_etf_dividend` | 获取ETF基金分红 | 24253 |
| SDK 1.0.4 补充接口 | - | `get_fund_etf_listing` | 获取ETF上市信息 | 24287 |
| SDK 1.0.4 补充接口 | - | `get_fund_etf_split` | 获取ETF拆分和折算 | 24320 |
| SDK 1.0.4 补充接口 | - | `get_fund_etf_suspend` | 获取ETF停复牌数据 | 24357 |
| SDK 1.0.4 补充接口 | - | `get_fund_min` | 获取ETF分钟线 | 24391 |
| SDK 1.0.4 补充接口 | - | `get_future_detail_all` | 兼容名称，等同 get_future_detail | 24431 |
| SDK 1.0.4 补充接口 | - | `get_future_market_post` | 获取期货后复权数据 | 24478 |
| SDK 1.0.4 补充接口 | - | `get_hk_daily_post` | 获取港股自研后复权日线数据。start_date、end_date 必填 | 24522 |
| SDK 1.0.4 补充接口 | - | `get_hk_daily_pre` | 获取港股自研前复权日线数据。start_date、end_date 必填 | 24547 |
| SDK 1.0.4 补充接口 | - | `get_hk_detail_all` | 获取港股全量基本信息（只读根 part-0.parquet，无 date） | 24572 |
| SDK 1.0.4 补充接口 | - | `get_hk_index_constituents` | 获取港股指数成分数据 | 24602 |
| SDK 1.0.4 补充接口 | - | `get_hk_index_daily` | 获取港股指数日线数据 | 24647 |
| SDK 1.0.4 补充接口 | - | `get_hk_index_detail` | 获取港股指数基本信息 | 24689 |
| SDK 1.0.4 补充接口 | - | `get_index_component` | 获取港股指数成分股数据 | 24726 |
| SDK 1.0.4 补充接口 | - | `get_index_constituent` | 获取美股指数成分股数据 | 24763 |
| SDK 1.0.4 补充接口 | - | `get_index_detail_all` | 兼容名称，等同 get_index_detail | 24799 |
| SDK 1.0.4 补充接口 | - | `get_index_weights_day` | 查询 `index_weights_ex`，参数和返回合同与 `get_index_weights` 一致 | 24845 |
| SDK 1.0.4 补充接口 | - | `get_macro_or` | 宏观特色数据-其他 | 24871 |
| SDK 1.0.4 补充接口 | - | `get_market_data` | get_market_data | 24913 |
| SDK 1.0.4 补充接口 | - | `get_market_min_data` | get_market_min_data | 24941 |
| SDK 1.0.4 补充接口 | - | `get_oversea_stock_list` | 获取日线中有行情的港美股代码列表 | 24969 |
| SDK 1.0.4 补充接口 | - | `get_st_list` | 获取股票逐日 ST 状态 | 25005 |
| SDK 1.0.4 补充接口 | - | `get_stock_competitor` | 兼容名称，等同 get_stock_competitor_information | 25030 |
| SDK 1.0.4 补充接口 | - | `get_stock_detail_all` | 兼容名称，等同 get_stock_detail | 25074 |
| SDK 1.0.4 补充接口 | - | `get_stock_flow` | 获取股票资金流入流出 | 25120 |
| SDK 1.0.4 补充接口 | - | `get_stock_intermediary` | 兼容名称，等同 get_stock_intermediary_information | 25163 |
| SDK 1.0.4 补充接口 | - | `get_stock_min_post` | 获取 A 股后复权分钟线；参数校验与 get_stock_min 一致 | 25210 |
| SDK 1.0.4 补充接口 | - | `get_stock_min_pre` | 获取 A 股前复权分钟线；参数校验与 get_stock_min 一致 | 25237 |
| SDK 1.0.4 补充接口 | - | `get_stock_monthly` | 获取A股月线行情数据 | 25264 |
| SDK 1.0.4 补充接口 | - | `get_stock_over_allotment` | 兼容名称，等同 get_stock_status_over_allotment | 25313 |
| SDK 1.0.4 补充接口 | - | `get_stock_related_party` | 兼容名称，等同 get_stock_rela_party_trans | 25366 |
| SDK 1.0.4 补充接口 | - | `get_stock_weekly` | 获取A股周线行情数据 | 25393 |
| SDK 1.0.4 补充接口 | - | `get_suspended_list` | 获取股票逐日停牌状态 | 25442 |
| SDK 1.0.4 补充接口 | - | `get_us_daily_post` | 获取美股自研后复权日线数据。start_date、end_date 必填 | 25467 |
| SDK 1.0.4 补充接口 | - | `get_us_daily_pre` | 获取美股自研前复权日线数据。start_date、end_date 必填 | 25492 |
| SDK 1.0.4 补充接口 | - | `get_us_detail_all` | 获取美股全量基本信息（只读根 part-0.parquet，无 date） | 25517 |
| SDK 1.0.4 补充接口 | - | `get_us_index_constituents` | 获取美股指数成分数据 | 25547 |
| SDK 1.0.4 补充接口 | - | `get_us_index_daily` | 获取美股指数日线数据 | 25592 |
| SDK 1.0.4 补充接口 | - | `get_us_index_detail` | 获取美股指数基本信息 | 25634 |
| SDK 1.0.4 补充接口 | - | `get_us_min` | 获取美股分钟线数据 | 25671 |
| SDK 1.0.6 补充接口 | - | `get_bond_cash_flow` | 获取债券现金流（bond_cash_flow） | 25706 |
| SDK 1.0.6 补充接口 | - | `get_bond_conv_basic` | 获取可转债发行基本资料（bond_conv_basic） | 25737 |
| SDK 1.0.6 补充接口 | - | `get_bond_conv_call_exec` | 获取可转债赎回执行（bond_conv_call_exec） | 25768 |
| SDK 1.0.6 补充接口 | - | `get_bond_conv_call_progress` | 获取可转债赎回进展（bond_conv_call_progress） | 25799 |
| SDK 1.0.6 补充接口 | - | `get_bond_conv_price_change` | 获取可转债转股价变动（bond_conv_price_change） | 25830 |
| SDK 1.0.6 补充接口 | - | `get_bond_conv_term` | 获取可转债转股条款（bond_conv_term） | 25861 |
| SDK 1.0.6 补充接口 | - | `get_bond_coupon` | 获取债券票面利率（bond_coupon） | 25892 |
| SDK 1.0.6 补充接口 | - | `get_bond_daily` | 获取债券日行情（bond_daily） | 25923 |
| SDK 1.0.6 补充接口 | - | `get_bond_option` | 获取债券选择权（bond_option） | 25954 |
| SDK 1.0.6 补充接口 | - | `get_factor_style_covariance` | 获取计算版因子协方差矩阵 (factor_style_covariance) | 25985 |
| SDK 1.0.6 补充接口 | - | `get_factor_style_residual` | 获取 CNEX 股票残差风险与收益 (factor_style_residual) | 26015 |
| SDK 1.0.6 补充接口 | - | `get_factor_style_return` | 获取 CNEX 因子日度收益 (factor_style_return) | 26043 |
| SDK 1.0.6 补充接口 | - | `get_fund_asset_allocation` | 获取基金资产配置 | 26071 |
| SDK 1.0.6 补充接口 | - | `get_fund_asset_allocation_detail` | 获取基金资产配置细分 | 26107 |
| SDK 1.0.6 补充接口 | - | `get_fund_bond_distribution` | 获取基金券种分布 | 26144 |
| SDK 1.0.6 补充接口 | - | `get_fund_bond_style` | 获取偏债基金风格特征 | 26180 |
| SDK 1.0.6 补充接口 | - | `get_fund_category_changes` | 获取基金持仓分类变动 | 26219 |
| SDK 1.0.6 补充接口 | - | `get_fund_holding_detail` | 获取基金持仓明细 | 26255 |
| SDK 1.0.6 补充接口 | - | `get_fund_index_category` | 获取基金指数分类 | 26294 |
| SDK 1.0.6 补充接口 | - | `get_fund_industry_allocation` | 获取基金行业配置 | 26330 |
| SDK 1.0.6 补充接口 | - | `get_fund_investment_style` | 获取基金投资风格 | 26369 |
| SDK 1.0.6 补充接口 | - | `get_fund_nav` | 获取基金历史净值（含收益率） | 26407 |
| SDK 1.0.6 补充接口 | - | `get_fund_nav_deviation` | 获取基金资产净值偏离情况 | 26445 |
| SDK 1.0.6 补充接口 | - | `get_fund_performance_metrics` | 获取基金业绩指标 | 26482 |
| SDK 1.0.6 补充接口 | - | `get_fund_stock_portfolio_change` | 获取基金股票投资组合变动 | 26517 |
| SDK 1.0.6 补充接口 | - | `get_fund_stock_style` | 获取偏股基金风格特征 | 26555 |
| SDK 1.0.6 补充接口 | - | `get_fund_stock_trade` | 获取基金股票交易信息 | 26592 |
| SDK 1.0.6 补充接口 | - | `get_future_second` | 获取期货次主力合约数据 | 26628 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_daily` | 获取港股ETF日线数据 | 26669 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_detail` | 获取港股ETF基本信息-按日快照（只读 stock_symbol_hk_etf_daily，month=YYYYMM 分区） | 26715 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_detail_all` | 获取港股ETF基本信息 | 26755 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_dividend_event` | 获取港股ETF分红相关的事件 | 26796 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_investor_concentration` | 获取港股ETF投资者集中度 | 26840 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_investor_ranking` | 获取港股ETF投资者排行 | 26878 |
| SDK 1.0.6 补充接口 | - | `get_hk_etf_top20_concentration` | 获取港股ETF前20投资者集中度 | 26919 |
| SDK 1.0.6 补充接口 | - | `get_option_commodity_rank` | 获取商品期权持仓排名 | 26957 |
| SDK 1.0.6 补充接口 | - | `get_option_margin` | 获取期权保证金 | 26997 |
| SDK 1.0.6 补充接口 | - | `get_option_trade_rank` | 获取期权期货公司交易排名 | 27034 |
| SDK 1.0.6 补充接口 | - | `get_option_trade_stats` | 获取期权交易信息 | 27073 |
| SDK 1.0.6 补充接口 | - | `get_option_underlying_exercise` | 获取期权标的行权信息 | 27114 |
| SDK 1.0.6 补充接口 | - | `get_option_variety_rank` | 获取期权品种成交排名 | 27151 |
| SDK 1.0.6 补充接口 | - | `get_rf_rate` | 获取币种与无风险利率 (rf_rate) | 27191 |
| SDK 1.0.6 补充接口 | - | `get_stock_ipo_first_day` | 获取 IPO 上市首日表现数据（stock_ipo_first_day） | 27218 |
| SDK 1.0.6 补充接口 | - | `get_stock_ipo_issuance` | 获取股票首次上市信息数据（stock_ipo_issuance，含北交所） | 27261 |
| SDK 1.0.6 补充接口 | - | `get_stock_ipo_listing` | 获取新股上市数据（stock_ipo_listing） | 27304 |
| SDK 1.0.6 补充接口 | - | `get_stock_ipo_offline_bid` | 获取新股网下询价明细数据（stock_ipo_offline_bid，仅沪深，不含北交所） | 27347 |
| SDK 1.0.6 补充接口 | - | `get_stock_ipo_offline_placing` | 获取新股网下发行配售结果数据（stock_ipo_offline_placing，仅沪深，不含北交所） | 27394 |
| SDK 1.0.6 补充接口 | - | `get_stock_ipo_offline_stat` | 获取网下配售统计数据（stock_ipo_offline_stat，仅沪深，不含北交所） | 27441 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_daily` | 获取美股ETF日线数据 | 27488 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_detail` | 获取美股ETF基本信息-按日快照（只读 stock_symbol_us_etf_daily，month=YYYYMM 分区） | 27534 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_detail_all` | 获取美股ETF基本信息 | 27574 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_dividend_activity` | 获取美股ETF分红相关的事件 | 27615 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_investor_centralization` | 获取美股ETF投资者集中度 | 27659 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_investor_leaderboard` | 获取美股ETF投资者排行 | 27697 |
| SDK 1.0.6 补充接口 | - | `get_us_etf_top20_centralization` | 获取美股ETF前20投资者集中度 | 27738 |
| SDK 1.0.6 补充接口 | - | `get_us_short_interest` | 获取美股空头（Short Interest）数据 | 27776 |
| SDK 1.0.6 补充接口 | - | `get_us_warrant_daily` | 获取美股轮证warrant日线数据 | 27819 |
| SDK 1.0.6 补充接口 | - | `get_us_warrant_detail` | 获取美股轮证warrant基本信息-按日快照（只读 stock_symbol_us_warrant_daily，month=YYYYMM 分区） | 27865 |
| SDK 1.0.6 补充接口 | - | `get_us_warrant_detail_all` | 获取美股轮证warrant基本信息 | 27905 |
| SDK 1.0.6 补充接口 | - | `get_us_warrant_investor_centralization` | 获取美股轮证warrant投资者集中度 | 27946 |
| SDK 1.0.6 补充接口 | - | `get_us_warrant_investor_leaderboard` | 获取美股轮证warrant投资者排行 | 27984 |
| SDK 1.0.6 补充接口 | - | `get_us_warrant_top20_centralization` | 获取美股轮证warrant前20投资者集中度 | 28025 |

# Pandadata Method Index

Generated from `api-docs.md`. Use line numbers with `sed -n '<line>,+120p' references/api-docs.md`, or run `python scripts/search_api_docs.py --method <method>`.

Total methods: 218

| Category | Section | Method | Summary | API docs line |
|---|---|---|---|---:|
| 交易工具 | 交易日历 | `get_trade_cal` | 获取交易日历 | 7 |
| 交易工具 | 某一日期前第 n 个交易日 | `get_prev_trade_date` | 获取指定日期的前第n个交易日 | 70 |
| 交易工具 | 最新交易日 | `get_last_trade_date` | 获取最新交易日 | 111 |
| 交易工具 | 合约特殊处理数据 | `get_stock_status_change` | 获取合约特殊处理数据 | 148 |
| 交易工具 | 指定日期的在售股票列表 | `get_trade_list` | 获取指定日期的在售股票列表 | 196 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily` | 获取A股日线数据 | 436 |
| A股数据 | 沪深股票行情数据 | `get_stock_rt_daily` | 获取A股当日日线 | 510 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily_pre` | 获取A股前复权日线数据 | 754 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily_post` | 获取A股后复权日线数据 | 827 |
| A股数据 | 沪深股票行情数据 | `get_stock_min` | 获取A股分钟线 | 900 |
| A股数据 | 沪深股票行情数据 | `get_stock_rt_min` | 获取A股当日分钟线 | 1154 |
| A股数据 | 概念基础数据 | `get_concept_list` | 获取概念列表 | 1264 |
| A股数据 | 概念基础数据 | `get_concept_constituents` | 获取概念成分股 | 1304 |
| A股数据 | 市场参考数据 | `get_stock_detail` | 获取股票基本信息 | 1415 |
| A股数据 | 市场参考数据 | `get_index_detail` | 获取指数基本信息 | 1473 |
| A股数据 | 行业基础数据 | `get_industry_constituents` | 获取行业成分股数据 | 1721 |
| A股数据 | 行业基础数据 | `get_industry_detail` | 获取行业基本信息数据 | 1771 |
| A股数据 | 行业基础数据 | `get_stock_industry` | 获取指定股票所属的行业信息 | 1845 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_daily` | 获取指数日线 | 1892 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_min` | 获取指数分钟线 | 1958 |
| A股数据 | 指数基础数据 | `get_index_weights` | 获取指数权重信息数据 | 2214 |
| A股数据 | 指数基础数据 | `get_index_indicator` | 获取指数估值指标数据 | 2459 |
| A股数据 | 市场交易与资金数据 | `get_lhb_list` | 获取股票龙虎榜数据 | 2707 |
| A股数据 | 市场交易与资金数据 | `get_lhb_detail` | 获取股票龙虎榜明细数据 | 2935 |
| A股数据 | 市场交易与资金数据 | `get_margin` | 获取融资融券信息 | 3002 |
| A股数据 | 市场交易与资金数据 | `get_hsgt_hold` | 获取沪深股通持股信息 | 3072 |
| A股数据 | 公司行为 | `get_investor_activity` | 获取A股合约投资者关系活动 | 3119 |
| A股数据 | 公司行为 | `get_restricted_list` | 获取股票限售解禁明细数据 | 3164 |
| A股数据 | 公司行为 | `get_repurchase` | 获取回购数据 | 3218 |
| A股数据 | 公司行为 | `get_holder_count` | 获取股东数量 | 3284 |
| A股数据 | 公司行为 | `get_top_holders` | 获取A股股东信息 | 3334 |
| A股数据 | 公司行为 | `get_block_trade` | 获取A股大宗交易信息 | 3404 |
| A股数据 | 公司行为 | `get_share_float` | 获取股票股本数据 | 3453 |
| A股数据 | 公司行为 | `get_stock_dividend` | 获取股票分红信息 | 3661 |
| A股数据 | 公司行为 | `get_stock_split` | 获取股票拆分数据 | 3708 |
| A股数据 | 公司行为 | `get_stock_cash_dividend` | 获取股票现金分红数据 | 3754 |
| A股数据 | 公司行为 | `get_stock_dividend_amount` | 获取股票分红总额数据 | 3805 |
| A股数据 | 公司行为 | `get_stock_private_placement` | 获取股票定向增发数据 | 3853 |
| A股数据 | 公司行为 | `get_stock_allotment` | 获取股票配股信息 | 3903 |
| A股数据 | 公司行为 | `get_stock_disclosure_date` | 获取上市A股定期报告预披露数据 | 3953 |
| A股数据 | 公司行为 | `get_stock_over_allotment` | 获取超额配售权实施情况数据 | 4003 |
| A股数据 | 公司行为 | `get_stock_litigation_arbitration` | 获取上市公司诉讼仲裁数据 | 4059 |
| A股数据 | 公司行为 | `get_stock_csrc_approval` | 获取证监会批文数据 | 4120 |
| A股数据 | 公司行为 | `get_stock_competitor` | 获取竞争企业信息数据 | 4169 |
| A股数据 | 公司行为 | `get_stock_intermediary` | 获取中介情况信息表数据 | 4216 |
| A股数据 | 公司行为 | `get_stock_related_party` | 上市公司关联交易 | 4265 |
| A股数据 | 公司行为 | `get_cumu_guarantee` | 获取累计担保信息 | 4331 |
| A股数据 | 公司行为 | `get_stock_material_contract` | 获取上市公司重大合同数据 | 4408 |
| A股数据 | 公司行为 | `get_investor_brief_detail` | 获取投资者简报详情 | 4485 |
| A股数据 | 公司行为 | `get_investor_brief_qa` | 获取投资者简报问答 | 4729 |
| A股数据 | 公司行为 | `get_stock_equity_illegal` | 获取股权违规信息 | 4975 |
| A股数据 | 股东行为 | `get_stock_pledge` | 获取A股公司股权质押 | 5230 |
| A股数据 | 股东行为 | `get_stock_pledge_stat` | 获取股票质押信息统计 | 5489 |
| A股数据 | 股东行为 | `get_stock_shareholder_change` | 获取股东增减持计划 | 5735 |
| A股数据 | 股东行为 | `get_stock_equity_placard` | 获取被举牌公司明细 | 5997 |
| A股数据 | 业绩预告 | `get_fina_forecast` | 获取业绩预告数据 | 6061 |
| A股数据 | 财务三表、财务快报 | `get_fina_performance` | 获取财务快报数据 | 6119 |
| A股数据 | 财务三表、财务快报 | `get_fina_reports` | 获取财务季度报告 | 6203 |
| A股数据 | 财务三表、财务快报 | `get_audit_opinion` | 获取财务报告审计意见 | 6290 |
| A股数据 | 股东结构 | `get_stock_equity_nature` | 获取个股企业性质 | 6345 |
| 期货数据 | 期货行情数据 | `get_future_daily` | 获取期货日线 | 6589 |
| 期货数据 | 期货行情数据 | `get_future_daily_post` | 获取期货后复权数据 | 6664 |
| 期货数据 | 期货行情数据 | `get_future_min` | 获取期货分钟线 | 6755 |
| 期货数据 | 期货基本信息 | `get_future_detail` | 获取期货基本信息 | 7017 |
| 期货数据 | 期货主力合约信息 | `get_future_dominant` | 获取期货主力合约数据 | 7078 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg` | 获取席位净持仓保证金数据 | 7137 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netposi_rank` | 获取期货商品净持仓多空榜单数据 | 7381 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg_change` | 获取席位净持仓保证金变化数据 | 7611 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_grade` | 获取席位评级数据 | 7855 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_totlmarg` | 获取席位总持仓保证金数据 | 7917 |
| 期货数据 | 期货 DeepView 数据 | `get_future_basis` | 获取期货基差数据 | 8161 |
| 期货数据 | 期货 DeepView 数据 | `get_future_warehouse_receipt` | 获取期货仓单数据 | 8223 |
| 期货数据 | 期货 DeepView 数据 | `get_future_net_flow` | 获取期货净资金流列表 | 8285 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_indicators` | 获取期货龙虎比、牛熊线 | 8333 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_variety_profit` | 获取期货席位的商品盈亏数据 | 8403 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_posi` | 获取期货商品持仓数据 | 8459 |
| 期货数据 | 期货 DeepView 数据 | `get_future_symbol_posi` | 获取期货合约持仓数据 | 8518 |
| 期货数据 | 期货 DeepView 数据 | `get_future_ls_ratio` | 获取期货合约多空比数据 | 8576 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netcap_change` | 获取期货合约净持仓市值变化数据 | 8816 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_rank` | 获取期货合约龙虎比、牛熊线排行 | 9059 |
| 期货数据 | 期货 DeepView 数据 | `get_future_term_structure` | 获取期货期限结构数据 | 9311 |
| 期货数据 | 期货 DeepView 数据 | `get_future_inventory` | 获取期货库存数据 | 9353 |
| 期货数据 | 期货 DeepView 数据 | `get_future_calendar_arbitrage` | 获取期货跨期套利数据 | 9395 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_spread` | 获取期货自由价差数据 | 9439 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_ratio` | 获取期货自由价比数据 | 9483 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_oi_value` | 获取期货席位合约的总持仓市值 | 9527 |
| 期货数据 | 期货 DeepView 数据 | `get_future_nonbroker_net` | 获取期货非期货公司净持仓 | 9574 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit` | 获取期货席位盈亏数据 | 9617 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_flow_daily` | 获取期货席位每日大资金流动数据 | 9662 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_ls_ratio` | 获取期货席位多空比数据 | 9711 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_loss_rank` | 获取期货席位亏损排行数据 | 9757 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit_rank` | 获取期货席位盈利排行数据 | 9799 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_build_process` | 获取期货席位建仓过程数据 | 9841 |
| 期货数据 | 期货 DeepView 数据 | `get_future_trader_quote` | 获取期货现货贸易商报价数据 | 10089 |
| 期货数据 | 期货 DeepView 数据 | `get_future_virtual_ratio` | 获取期货虚实盘比数据 | 10334 |
| 期货数据 | 期货 DeepView 数据 | `get_future_spot_profit` | 获取期货利润数据 | 10378 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_mcap` | 获取期货品种持仓市值数据 | 10423 |
| 期货数据 | 期货 DeepView 数据 | `get_future_dominant_corr` | 获取期货主力合约涨跌幅相关性 | 10465 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_pool` | 获取期货多头空头合约池 | 10504 |
| 期权数据 | 期权基本信息 | `get_option_detail` | 获取期权基本信息 | 10557 |
| 期权数据 | 期权基本信息 | `get_option_underlying_detail` | 获取期权品种信息 | 10813 |
| 期权数据 | 期权基本信息 | `get_option_exercise` | 获取期权行权交收信息 | 10869 |
| 期权数据 | 期权基本信息 | `get_option_static` | 获取期权每日盘前静态数据 | 10913 |
| 期权数据 | 期权日线行情 | `get_option_daily` | 获取期权日线数据 | 10992 |
| 期权数据 | 期权日线行情 | `get_option_spot_market` | 获取期权现货日行情 | 11243 |
| 期权数据 | 期权波动率数据 | `get_option_implied_volatility` | 获取期权隐含波动率 | 11320 |
| 期权数据 | 期权波动率数据 | `get_option_underlying_volatility` | 获取期权标的历史波动率 | 11362 |
| 期权数据 | 期权波动率数据 | `get_option_risk_indicators` | 获取期权风险指标 | 11490 |
| 量化因子数据 | 回测因子 | `get_factor` | 获取回测因子 | 11543 |
| 量化因子数据 | 复权因子 | `get_adj_factor` | 获取复权因子 | 11627 |
| 港美股 | 行情数据 | `get_hk_daily` | 获取港股日线数据 | 11677 |
| 港美股 | 行情数据 | `get_us_daily` | 获取美股日线数据 | 11943 |
| 港美股 | 港股股票基础信息 | `get_hk_detail` | 获取港股的基本信息 | 12200 |
| 港美股 | 美股股票基础信息 | `get_us_detail` | 获取美股的基本信息 | 12265 |
| 港美股 | 港股公司事件 | `get_stock_dividend_event` | 获取股票分红相关的事件 | 12327 |
| 港美股 | 港股公司事件 | `get_stock_market_event` | 获取市场活动相关的事件 | 12378 |
| 港美股 | 港股公司事件 | `get_stock_meeting_event` | 获取公司会议相关的事件 | 12625 |
| 港美股 | 港股公司事件 | `get_stock_financial_event` | 获取财务披露相关的事件 | 12872 |
| 港美股 | 港股公司事件 | `get_stock_ir_event` | 获取投资者关系活动相关的事件 | 13119 |
| 港美股 | 美股公司事件 | `get_stock_dividend_activity` | 获取股票分红相关的事件 | 13368 |
| 港美股 | 美股公司事件 | `get_stock_market_activity` | 获取市场活动相关的事件 | 13419 |
| 港美股 | 美股公司事件 | `get_stock_meeting_activity` | 获取公司会议相关的事件 | 13666 |
| 港美股 | 美股公司事件 | `get_stock_financial_activity` | 获取财务披露相关的事件 | 13913 |
| 港美股 | 美股公司事件 | `get_stock_ir_activity` | 获取投资者关系活动相关的事件 | 14160 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_concentration` | 获取公司投资者集中度 | 14409 |
| 港美股 | 港股股东与投资者 | `get_stock_top20_concentration` | 获取公司前20投资者集中度 | 14650 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_ranking` | 获取公司投资者排行 | 14891 |
| 港美股 | 港股股东与投资者 | `get_stock_insider_trade` | 获取公司内部人交易活动 | 15138 |
| 港美股 | 港股股东与投资者 | `get_stock_shareholder_holding` | 获取公司股东持股报告 | 15206 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_centralization` | 获取公司投资者集中度 | 15274 |
| 港美股 | 美股股东与投资者 | `get_stock_top20_centralization` | 获取公司前20投资者集中度 | 15515 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_leaderboard` | 获取公司投资者排行 | 15756 |
| 港美股 | 美股股东与投资者 | `get_stock_insider_transaction` | 获取公司内部人交易活动 | 16003 |
| 港美股 | 美股股东与投资者 | `get_stock_shareholder_report` | 获取公司股东持股报告 | 16135 |
| 港美股 | 港股核心数据 | `get_stock_industry_median` | 获取公司最新行业中位统计数据 | 16213 |
| 港美股 | 港股核心数据 | `get_stock_pv_indicator` | 获取公司最新价量指标数据 | 16655 |
| 港美股 | 美股核心数据 | `get_stock_sector_median` | 获取公司最新行业中位统计数据 | 16920 |
| 港美股 | 美股核心数据 | `get_stock_pv_metric` | 获取公司最新价量指标数据 | 17362 |
| 港美股 | 港股一致预期数据 | `get_stock_ncycl_consensus` | 获取非周期性指标一致预期 | 17627 |
| 港美股 | 港股一致预期数据 | `get_stock_recommendation_consensus` | 获取买卖建议一致预期 | 17872 |
| 港美股 | 美股一致预期数据 | `get_stock_ncycl_estimate` | 获取非周期性指标一致预期 | 18122 |
| 港美股 | 美股一致预期数据 | `get_stock_recommendation_estimate` | 获取买卖建议一致预期 | 18367 |
| 港美股 | 港股财务数据 | `get_stock_operating_indicator` | 获取公司标准化营运指标 | 18617 |
| 港美股 | 港股财务数据 | `get_stock_mktfin_indicator` | 获取公司最新市场财务统计指标 | 18870 |
| 港美股 | 港股财务数据 | `get_fina_statement` | 获取财务季度报告 | 19253 |
| 港美股 | 美股财务数据 | `get_stock_operating_metric` | 获取公司标准化营运指标 | 19304 |
| 港美股 | 美股财务数据 | `get_stock_mktfin_metric` | 获取公司最新市场财务统计指标 | 19557 |
| 港美股 | 美股财务数据 | `get_fina_ex` | 获取财务季度报告 | 19940 |
| 宏观数据 | 宏观指标基础信息 | `get_macro_detail` | 宏观指标列表 | 19993 |
| 宏观数据 | 中国宏观指标 | `get_macro_na` | 中国宏观-国民经济核算 | 20250 |
| 宏观数据 | 中国宏观指标 | `get_macro_in` | 中国宏观-工业 | 20294 |
| 宏观数据 | 中国宏观指标 | `get_macro_ci` | 中国宏观-景气指数 | 20338 |
| 宏观数据 | 中国宏观指标 | `get_macro_pi` | 中国宏观-价格指数 | 20381 |
| 宏观数据 | 中国宏观指标 | `get_macro_fa` | 中国宏观-固定资产投资 | 20424 |
| 宏观数据 | 中国宏观指标 | `get_macro_fi` | 中国宏观-财政 | 20467 |
| 宏观数据 | 中国宏观指标 | `get_macro_mb` | 中国宏观-货币与银行 | 20510 |
| 宏观数据 | 中国宏观指标 | `get_macro_ir` | 中国宏观-利率汇率 | 20554 |
| 宏观数据 | 中国宏观指标 | `get_macro_fe` | 中国宏观-对外经济 | 20598 |
| 宏观数据 | 中国宏观指标 | `get_macro_dt` | 中国宏观-国内贸易 | 20641 |
| 宏观数据 | 中国宏观指标 | `get_macro_ew` | 中国宏观-就业与工资 | 20685 |
| 宏观数据 | 中国宏观指标 | `get_macro_li` | 中国宏观-人民生活 | 20729 |
| 宏观数据 | 中国宏观指标 | `get_macro_pr` | 中国宏观-人口与资源 | 20773 |
| 宏观数据 | 中国宏观指标 | `get_macro_se` | 中国宏观-科教体卫 | 20816 |
| 宏观数据 | 中国宏观指标 | `get_macro_sm` | 中国宏观-证券市场 | 20861 |
| 宏观数据 | 中国宏观指标 | `get_macro_pm` | 中国宏观-区域宏观 | 20905 |
| 宏观数据 | 国际宏观指标 | `get_macro_gb` | 宏观行业-国际宏观 | 20952 |
| 宏观数据 | 宏观行业数据 | `get_macro_ag` | 宏观行业-农林牧渔 | 20998 |
| 宏观数据 | 宏观行业数据 | `get_macro_en` | 宏观行业-能源 | 21042 |
| 宏观数据 | 宏观行业数据 | `get_macro_ch` | 宏观行业-化工 | 21086 |
| 宏观数据 | 宏观行业数据 | `get_macro_st` | 宏观行业-钢铁 | 21130 |
| 宏观数据 | 宏观行业数据 | `get_macro_nf` | 宏观行业-有色金属 | 21175 |
| 宏观数据 | 宏观行业数据 | `get_macro_bm` | 宏观行业-建材 | 21218 |
| 宏观数据 | 宏观行业数据 | `get_macro_au` | 宏观行业-汽车 | 21261 |
| 宏观数据 | 宏观行业数据 | `get_macro_me` | 宏观行业-机械设备 | 21304 |
| 宏观数据 | 宏观行业数据 | `get_macro_ee` | 宏观行业-电子电器 | 21348 |
| 宏观数据 | 宏观行业数据 | `get_macro_tm` | 宏观行业-TMT | 21392 |
| 宏观数据 | 宏观行业数据 | `get_macro_fb` | 宏观行业-食品饮料 | 21435 |
| 宏观数据 | 宏观行业数据 | `get_macro_te` | 宏观行业-纺织服装 | 21479 |
| 宏观数据 | 宏观行业数据 | `get_macro_pp` | 宏观行业-造纸印刷 | 21522 |
| 宏观数据 | 宏观行业数据 | `get_macro_ph` | 宏观行业-医药生物 | 21565 |
| 宏观数据 | 宏观行业数据 | `get_macro_ut` | 宏观行业-公用事业 | 21609 |
| 宏观数据 | 宏观行业数据 | `get_macro_tr` | 宏观行业-交通运输 | 21653 |
| 宏观数据 | 宏观行业数据 | `get_macro_rc` | 宏观行业-房地产及建筑业 | 21697 |
| 宏观数据 | 宏观行业数据 | `get_macro_th` | 宏观行业-旅游酒店 | 21741 |
| 宏观数据 | 宏观行业数据 | `get_macro_ce` | 宏观行业-文教体娱及工艺品 | 21784 |
| 宏观数据 | 宏观行业数据 | `get_macro_wr` | 宏观行业-批发零售业 | 21827 |
| 宏观数据 | 宏观行业数据 | `get_macro_fs` | 宏观行业-金融保险业 | 21870 |
| 宏观数据 | 宏观行业数据 | `get_macro_is` | 宏观行业-行业综合 | 21914 |
| 宏观数据 | 宏观特色数据 | `get_macro_ec` | 宏观特色数据-线上电商数据 | 21960 |
| 宏观数据 | 宏观特色数据 | `get_macro_md` | 宏观特色数据-医药数据 | 22003 |
| 宏观数据 | 宏观特色数据 | `get_macro_eh` | 宏观特色数据-能化数据 | 22046 |
| 宏观数据 | 宏观特色数据 | `get_macro_ad` | 宏观特色数据-汽车数据 | 22090 |
| 宏观数据 | 宏观特色数据 | `get_macro_ha` | 宏观特色数据-家电数据 | 22133 |
| 宏观数据 | 宏观特色数据 | `get_macro_of` | 宏观特色数据-线下商超数据 | 22176 |
| 宏观数据 | 宏观特色数据 | `get_macro_rb` | 宏观特色数据-招聘数据 | 22219 |
| 宏观数据 | 宏观特色数据 | `get_macro_re` | 宏观特色数据-房地产数据 | 22263 |
| 宏观数据 | 宏观特色数据 | `get_macro_ed` | 宏观特色数据-电子数据 | 22307 |
| 宏观数据 | 宏观特色数据 | `get_macro_ep` | 宏观特色数据-电新数据 | 22350 |
| 宏观数据 | 宏观特色数据 | `get_macro_ar` | 宏观特色数据-农业数据 | 22394 |
| 宏观数据 | 宏观特色数据 | `get_macro_cm` | 宏观特色数据-大宗数据 | 22438 |
| 宏观数据 | 宏观经济日历 | `get_macro_cal` | 宏观经济日历 | 22484 |
| 宏观数据 | 宏观经济日历信息 | `get_macro_cal_info` | 宏观经济日历信息 | 22555 |
| 宏观数据 | 宏观经济日历配置 | `get_macro_cal_config` | 宏观经济日历配置 | 22607 |
| 基金数据 | 基金基础数据 | `get_fund_detail` | 获取基金基本信息 | 22651 |
| 基金数据 | 基金行情数据 | `get_fund_daily` | 获取基金日行情数据 | 22960 |
| 基金数据 | 基金行情数据 | `get_fund_daily_post` | 获取基金后复权日行情数据 | 23070 |
| 基金数据 | 基金行情数据 | `get_fund_daily_pre` | 获取基金前复权日行情数据 | 23275 |
| 基金数据 | ETF数据 | `get_fund_etf_cr_limits` | 获取ETF申赎限制数据 | 23482 |
| 基金数据 | ETF数据 | `get_fund_etf_cr_net` | 获取ETF净申赎数据 | 23553 |
| 基金数据 | ETF数据 | `get_fund_etf_constituents` | 获取ETF基金申赎清单成分券信息 | 23629 |
| 基金数据 | ETF数据 | `get_fund_etf_cr` | 获取ETF基金申赎清单数据 | 23698 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_dividend` | 获取优先股分红 | 23775 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_trading` | 获取优先股成交统计信息 | 23852 |
| 优先股数据 | 优先股数据 | `get_stock_issuer_credit_rating` | 获取优先股发行主体信用评级 | 23918 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_rating` | 获取优先股评级情况 | 23986 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_shares` | 获取优先股股本 | 24037 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_placement` | 获取优先股配售结果 | 24102 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_detail` | 获取优先股基本资料 | 24165 |

# Pandadata Method Index

Generated from `api-docs.md`. Use line numbers with `sed -n '<line>,+120p' references/api-docs.md`, or run `python scripts/search_api_docs.py --method <method>`.

Total methods: 185

| Category | Section | Method | Summary | API docs line |
|---|---|---|---|---:|
| 交易工具 | 交易日历 | `get_trade_cal` | 获取交易日历 | 7 |
| 交易工具 | 某一日期前第 n 个交易日 | `get_prev_trade_date` | 获取指定日期的前第n个交易日 | 70 |
| 交易工具 | 最新交易日 | `get_last_trade_date` | 获取最新交易日 | 111 |
| 交易工具 | 合约特殊处理数据 | `get_stock_status_change` | 获取合约特殊处理数据 | 148 |
| 交易工具 | 指定日期的在售股票列表 | `get_trade_list` | 获取指定日期的在售股票列表 | 197 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily` | 获取A股日线数据 | 437 |
| A股数据 | 沪深股票行情数据 | `get_stock_rt_daily` | 获取A股实时日线数据 | 511 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily_pre` | 获取A股前复权日线数据 | 755 |
| A股数据 | 沪深股票行情数据 | `get_stock_daily_post` | 获取A股后复权日线数据 | 828 |
| A股数据 | 沪深股票行情数据 | `get_stock_min` | 获取A股分钟线 | 901 |
| A股数据 | 沪深股票行情数据 | `get_stock_rt_min` | 获取当日A股分钟线数据 | 1156 |
| A股数据 | 概念基础数据 | `get_concept_list` | 获取概念列表 | 1266 |
| A股数据 | 概念基础数据 | `get_concept_constituents` | 获取概念成分股 | 1306 |
| A股数据 | 市场参考数据 | `get_stock_detail` | 获取股票基本信息 | 1417 |
| A股数据 | 市场参考数据 | `get_index_detail` | 获取指数基本信息 | 1475 |
| A股数据 | 行业基础数据 | `get_industry_constituents` | 获取行业成分股数据 | 1723 |
| A股数据 | 行业基础数据 | `get_industry_detail` | 获取行业基本信息数据 | 1773 |
| A股数据 | 行业基础数据 | `get_stock_industry` | 获取指定股票所属的行业信息 | 1844 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_daily` | 获取指数日线 | 1891 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_min` | 获取指数分钟线 | 1957 |
| A股数据 | 指数基础数据 | `get_index_weights` | 获取指数权重信息数据 | 2213 |
| A股数据 | 指数基础数据 | `get_index_indicator` | 获取指数估值指标数据 | 2458 |
| A股数据 | 市场交易与资金数据 | `get_lhb_list` | 获取股票龙虎榜数据 | 2706 |
| A股数据 | 市场交易与资金数据 | `get_lhb_detail` | 获取股票龙虎榜明细数据 | 2934 |
| A股数据 | 市场交易与资金数据 | `get_margin` | 获取融资融券信息 | 3001 |
| A股数据 | 市场交易与资金数据 | `get_hsgt_hold` | 获取沪深股通持股信息 | 3071 |
| A股数据 | 公司行为 | `get_investor_activity` | 获取A股合约投资者关系活动 | 3118 |
| A股数据 | 公司行为 | `get_restricted_list` | 获取股票限售解禁明细数据 | 3163 |
| A股数据 | 公司行为 | `get_repurchase` | 获取回购数据 | 3217 |
| A股数据 | 公司行为 | `get_holder_count` | 获取股东数量 | 3283 |
| A股数据 | 公司行为 | `get_top_holders` | 获取A股股东信息 | 3333 |
| A股数据 | 公司行为 | `get_block_trade` | 获取A股大宗交易信息 | 3403 |
| A股数据 | 公司行为 | `get_share_float` | 获取股票股本数据 | 3452 |
| A股数据 | 公司行为 | `get_stock_dividend` | 获取股票分红信息 | 3660 |
| A股数据 | 公司行为 | `get_stock_split` | 获取股票拆分数据 | 3707 |
| A股数据 | 公司行为 | `get_stock_cash_dividend` | 获取股票现金分红数据 | 3753 |
| A股数据 | 公司行为 | `get_stock_dividend_amount` | 获取股票分红总额数据 | 3804 |
| A股数据 | 公司行为 | `get_stock_private_placement` | 获取股票定向增发数据 | 3852 |
| A股数据 | 公司行为 | `get_stock_allotment` | 获取股票配股信息 | 3902 |
| A股数据 | 股东行为 | `get_stock_pledge` | 获取A股公司股权质押 | 3954 |
| A股数据 | 股东行为 | `get_stock_pledge_stat` | 获取股票质押信息统计 | 4213 |
| A股数据 | 股东行为 | `get_stock_shareholder_change` | 获取股东增减持计划 | 4459 |
| A股数据 | 业绩预告 | `get_fina_forecast` | 获取业绩预告数据 | 4723 |
| A股数据 | 财务三表、财务快报 | `get_fina_performance` | 获取财务快报数据 | 4781 |
| A股数据 | 财务三表、财务快报 | `get_fina_reports` | 获取财务季度报告 | 4865 |
| A股数据 | 财务三表、财务快报 | `get_audit_opinion` | 获取财务报告审计意见 | 4952 |
| 期货数据 | 期货行情数据 | `get_future_daily` | 获取期货日线 | 5009 |
| 期货数据 | 期货行情数据 | `get_future_daily_post` | 获取期货后复权数据 | 5084 |
| 期货数据 | 期货行情数据 | `get_future_min` | 获取期货分钟线 | 5150 |
| 期货数据 | 期货基本信息 | `get_future_detail` | 获取期货基本信息 | 5412 |
| 期货数据 | 期货主力合约信息 | `get_future_dominant` | 获取期货主力合约数据 | 5473 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg` | 获取席位净持仓保证金数据 | 5533 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netposi_rank` | 获取期货商品净持仓多空榜单数据 | 5777 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg_change` | 获取席位净持仓保证金变化数据 | 6007 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_grade` | 获取席位评级数据 | 6251 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_totlmarg` | 获取席位总持仓保证金数据 | 6313 |
| 期货数据 | 期货 DeepView 数据 | `get_future_basis` | 获取期货基差数据 | 6557 |
| 期货数据 | 期货 DeepView 数据 | `get_future_warehouse_receipt` | 获取期货仓单数据 | 6619 |
| 期货数据 | 期货 DeepView 数据 | `get_future_net_flow` | 获取期货净资金流列表 | 6681 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_indicators` | 获取期货龙虎比、牛熊线 | 6729 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_variety_profit` | 获取期货席位的商品盈亏数据 | 6799 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_posi` | 获取期货商品持仓数据 | 6855 |
| 期货数据 | 期货 DeepView 数据 | `get_future_symbol_posi` | 获取期货合约持仓数据 | 6914 |
| 期货数据 | 期货 DeepView 数据 | `get_future_ls_ratio` | 获取期货合约多空比数据 | 6972 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netcap_change` | 获取期货合约净持仓市值变化数据 | 7212 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_rank` | 获取期货合约龙虎比、牛熊线排行 | 7455 |
| 期货数据 | 期货 DeepView 数据 | `get_future_term_structure` | 获取期货期限结构数据 | 7707 |
| 期货数据 | 期货 DeepView 数据 | `get_future_inventory` | 获取期货库存数据 | 7749 |
| 期货数据 | 期货 DeepView 数据 | `get_future_calendar_arbitrage` | 获取期货跨期套利数据 | 7791 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_spread` | 获取期货自由价差数据 | 7835 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_ratio` | 获取期货自由价比数据 | 7879 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_oi_value` | 获取期货席位合约的总持仓市值 | 7923 |
| 期货数据 | 期货 DeepView 数据 | `get_future_nonbroker_net` | 获取期货非期货公司净持仓 | 7970 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit` | 获取期货席位盈亏数据 | 8013 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_flow_daily` | 获取期货席位每日大资金流动数据 | 8058 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_ls_ratio` | 获取期货席位多空比数据 | 8107 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_loss_rank` | 获取期货席位亏损排行数据 | 8153 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit_rank` | 获取期货席位盈利排行数据 | 8195 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_build_process` | 获取期货席位建仓过程数据 | 8237 |
| 期货数据 | 期货 DeepView 数据 | `get_future_trader_quote` | 获取期货现货贸易商报价数据 | 8485 |
| 期货数据 | 期货 DeepView 数据 | `get_future_virtual_ratio` | 获取期货虚实盘比数据 | 8730 |
| 期货数据 | 期货 DeepView 数据 | `get_future_spot_profit` | 获取期货利润数据 | 8774 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_mcap` | 获取期货品种持仓市值数据 | 8819 |
| 期货数据 | 期货 DeepView 数据 | `get_future_dominant_corr` | 获取期货主力合约涨跌幅相关性 | 8861 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_pool` | 获取期货多头空头合约池 | 8900 |
| 期权数据 | 期权基本信息 | `get_option_detail` | 获取期权基本信息 | 8953 |
| 期权数据 | 期权基本信息 | `get_option_underlying_detail` | 获取期权品种信息 | 9209 |
| 期权数据 | 期权日线行情 | `get_option_daily` | 获取期权日线数据 | 9267 |
| 期权数据 | 期权波动率数据 | `get_option_implied_volatility` | 获取期权隐含波动率 | 9520 |
| 期权数据 | 期权波动率数据 | `get_option_underlying_volatility` | 获取期权标的历史波动率 | 9562 |
| 量化因子数据 | 回测因子 | `get_factor` | 获取回测因子 | 9694 |
| 量化因子数据 | 复权因子 | `get_adj_factor` | 获取复权因子 | 9779 |
| 港美股 | 行情数据 | `get_hk_daily` | 获取港股日线数据 | 9829 |
| 港美股 | 行情数据 | `get_us_daily` | 获取美股日线数据 | 10096 |
| 港美股 | 港股股票基础信息 | `get_hk_detail` | 获取港股的基本信息 | 10347 |
| 港美股 | 美股股票基础信息 | `get_us_detail` | 获取美股的基本信息 | 10413 |
| 港美股 | 港股公司事件 | `get_stock_dividend_event` | 获取股票分红相关的事件 | 10477 |
| 港美股 | 港股公司事件 | `get_stock_market_event` | 获取市场活动相关的事件 | 10528 |
| 港美股 | 港股公司事件 | `get_stock_meeting_event` | 获取公司会议相关的事件 | 10774 |
| 港美股 | 港股公司事件 | `get_stock_financial_event` | 获取财务披露相关的事件 | 11020 |
| 港美股 | 港股公司事件 | `get_stock_ir_event` | 获取投资者关系活动相关的事件 | 11266 |
| 港美股 | 美股公司事件 | `get_stock_dividend_activity` | 获取股票分红相关的事件 | 11514 |
| 港美股 | 美股公司事件 | `get_stock_market_activity` | 获取市场活动相关的事件 | 11760 |
| 港美股 | 美股公司事件 | `get_stock_meeting_activity` | 获取公司会议相关的事件 | 12006 |
| 港美股 | 美股公司事件 | `get_stock_financial_activity` | 获取财务披露相关的事件 | 12252 |
| 港美股 | 美股公司事件 | `get_stock_ir_activity` | 获取投资者关系活动相关的事件 | 12498 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_concentration` | 获取公司投资者集中度 | 12746 |
| 港美股 | 港股股东与投资者 | `get_stock_top20_concentration` | 获取公司前20投资者集中度 | 12987 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_ranking` | 获取公司投资者排行 | 13228 |
| 港美股 | 港股股东与投资者 | `get_stock_insider_trade` | 获取公司内部人交易活动 | 13475 |
| 港美股 | 港股股东与投资者 | `get_stock_shareholder_holding` | 获取公司股东持股报告 | 13543 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_centralization` | 获取公司投资者集中度 | 13611 |
| 港美股 | 美股股东与投资者 | `get_stock_top20_centralization` | 获取公司前20投资者集中度 | 13852 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_leaderboard` | 获取公司投资者排行 | 14093 |
| 港美股 | 美股股东与投资者 | `get_stock_insider_transaction` | 获取公司内部人交易活动 | 14340 |
| 港美股 | 美股股东与投资者 | `get_stock_shareholder_report` | 获取公司股东持股报告 | 14472 |
| 港美股 | 港股核心数据 | `get_stock_industry_median` | 获取公司最新行业中位统计数据 | 14550 |
| 港美股 | 港股核心数据 | `get_stock_pv_indicator` | 获取公司最新价量指标数据 | 14992 |
| 港美股 | 美股核心数据 | `get_stock_sector_median` | 获取公司最新行业中位统计数据 | 15257 |
| 港美股 | 美股核心数据 | `get_stock_pv_metric` | 获取公司最新价量指标数据 | 15699 |
| 港美股 | 港股一致预期数据 | `get_stock_ncycl_consensus` | 获取非周期性指标一致预期 | 15964 |
| 港美股 | 港股一致预期数据 | `get_stock_recommendation_consensus` | 获取买卖建议一致预期 | 16209 |
| 港美股 | 美股一致预期数据 | `get_stock_ncycl_estimate` | 获取非周期性指标一致预期 | 16459 |
| 港美股 | 美股一致预期数据 | `get_stock_recommendation_estimate` | 获取买卖建议一致预期 | 16704 |
| 港美股 | 港股财务与市场因子 | `get_stock_operating_indicator` | 获取公司标准化营运指标 | 16954 |
| 港美股 | 港股财务与市场因子 | `get_stock_mktfin_indicator` | 获取公司最新市场财务统计指标 | 17207 |
| 港美股 | 港股财务与市场因子 | `get_fina_statement` | 获取财务季度报告 | 17590 |
| 港美股 | 美股财务与市场因子 | `get_stock_operating_metric` | 获取公司标准化营运指标 | 17641 |
| 港美股 | 美股财务与市场因子 | `get_stock_mktfin_metric` | 获取公司最新市场财务统计指标 | 17894 |
| 港美股 | 美股财务与市场因子 | `get_fina_ex` | 获取财务季度报告 | 18277 |
| 宏观数据 | 宏观指标基础信息 | `get_macro_detail` | 宏观指标列表 | 18330 |
| 宏观数据 | 中国宏观指标 | `get_macro_na` | 中国宏观-国民经济核算 | 18587 |
| 宏观数据 | 中国宏观指标 | `get_macro_in` | 中国宏观-工业 | 18631 |
| 宏观数据 | 中国宏观指标 | `get_macro_ci` | 中国宏观-景气指数 | 18675 |
| 宏观数据 | 中国宏观指标 | `get_macro_pi` | 中国宏观-价格指数 | 18718 |
| 宏观数据 | 中国宏观指标 | `get_macro_fa` | 中国宏观-固定资产投资 | 18761 |
| 宏观数据 | 中国宏观指标 | `get_macro_fi` | 中国宏观-财政 | 18804 |
| 宏观数据 | 中国宏观指标 | `get_macro_mb` | 中国宏观-货币与银行 | 18847 |
| 宏观数据 | 中国宏观指标 | `get_macro_ir` | 中国宏观-利率汇率 | 18891 |
| 宏观数据 | 中国宏观指标 | `get_macro_fe` | 中国宏观-对外经济 | 18935 |
| 宏观数据 | 中国宏观指标 | `get_macro_dt` | 中国宏观-国内贸易 | 18978 |
| 宏观数据 | 中国宏观指标 | `get_macro_ew` | 中国宏观-就业与工资 | 19022 |
| 宏观数据 | 中国宏观指标 | `get_macro_li` | 中国宏观-人民生活 | 19066 |
| 宏观数据 | 中国宏观指标 | `get_macro_pr` | 中国宏观-人口与资源 | 19110 |
| 宏观数据 | 中国宏观指标 | `get_macro_se` | 中国宏观-科教体卫 | 19153 |
| 宏观数据 | 中国宏观指标 | `get_macro_sm` | 中国宏观-证券市场 | 19198 |
| 宏观数据 | 中国宏观指标 | `get_macro_pm` | 中国宏观-区域宏观 | 19242 |
| 宏观数据 | 国际宏观指标 | `get_macro_gb` | 宏观行业-国际宏观 | 19289 |
| 宏观数据 | 宏观行业数据 | `get_macro_ag` | 宏观行业-农林牧渔 | 19335 |
| 宏观数据 | 宏观行业数据 | `get_macro_en` | 宏观行业-能源 | 19379 |
| 宏观数据 | 宏观行业数据 | `get_macro_ch` | 宏观行业-化工 | 19423 |
| 宏观数据 | 宏观行业数据 | `get_macro_st` | 宏观行业-钢铁 | 19467 |
| 宏观数据 | 宏观行业数据 | `get_macro_nf` | 宏观行业-有色金属 | 19512 |
| 宏观数据 | 宏观行业数据 | `get_macro_bm` | 宏观行业-建材 | 19555 |
| 宏观数据 | 宏观行业数据 | `get_macro_au` | 宏观行业-汽车 | 19598 |
| 宏观数据 | 宏观行业数据 | `get_macro_me` | 宏观行业-机械设备 | 19641 |
| 宏观数据 | 宏观行业数据 | `get_macro_ee` | 宏观行业-电子电器 | 19685 |
| 宏观数据 | 宏观行业数据 | `get_macro_tm` | 宏观行业-TMT | 19729 |
| 宏观数据 | 宏观行业数据 | `get_macro_fb` | 宏观行业-食品饮料 | 19772 |
| 宏观数据 | 宏观行业数据 | `get_macro_te` | 宏观行业-纺织服装 | 19816 |
| 宏观数据 | 宏观行业数据 | `get_macro_pp` | 宏观行业-造纸印刷 | 19859 |
| 宏观数据 | 宏观行业数据 | `get_macro_ph` | 宏观行业-医药生物 | 19902 |
| 宏观数据 | 宏观行业数据 | `get_macro_ut` | 宏观行业-公用事业 | 19946 |
| 宏观数据 | 宏观行业数据 | `get_macro_tr` | 宏观行业-交通运输 | 19990 |
| 宏观数据 | 宏观行业数据 | `get_macro_rc` | 宏观行业-房地产及建筑业 | 20034 |
| 宏观数据 | 宏观行业数据 | `get_macro_th` | 宏观行业-旅游酒店 | 20078 |
| 宏观数据 | 宏观行业数据 | `get_macro_ce` | 宏观行业-文教体娱及工艺品 | 20121 |
| 宏观数据 | 宏观行业数据 | `get_macro_wr` | 宏观行业-批发零售业 | 20164 |
| 宏观数据 | 宏观行业数据 | `get_macro_fs` | 宏观行业-金融保险业 | 20207 |
| 宏观数据 | 宏观行业数据 | `get_macro_is` | 宏观行业-行业综合 | 20251 |
| 宏观数据 | 宏观特色数据 | `get_macro_ec` | 宏观特色数据-线上电商数据 | 20297 |
| 宏观数据 | 宏观特色数据 | `get_macro_md` | 宏观特色数据-医药数据 | 20340 |
| 宏观数据 | 宏观特色数据 | `get_macro_eh` | 宏观特色数据-能化数据 | 20383 |
| 宏观数据 | 宏观特色数据 | `get_macro_ad` | 宏观特色数据-汽车数据 | 20427 |
| 宏观数据 | 宏观特色数据 | `get_macro_ha` | 宏观特色数据-家电数据 | 20470 |
| 宏观数据 | 宏观特色数据 | `get_macro_of` | 宏观特色数据-线下商超数据 | 20513 |
| 宏观数据 | 宏观特色数据 | `get_macro_rb` | 宏观特色数据-招聘数据 | 20556 |
| 宏观数据 | 宏观特色数据 | `get_macro_re` | 宏观特色数据-房地产数据 | 20600 |
| 宏观数据 | 宏观特色数据 | `get_macro_ed` | 宏观特色数据-电子数据 | 20644 |
| 宏观数据 | 宏观特色数据 | `get_macro_ep` | 宏观特色数据-电新数据 | 20687 |
| 宏观数据 | 宏观特色数据 | `get_macro_ar` | 宏观特色数据-农业数据 | 20731 |
| 宏观数据 | 宏观特色数据 | `get_macro_cm` | 宏观特色数据-大宗数据 | 20775 |
| 宏观数据 | 宏观经济日历 | `get_macro_cal` | 宏观经济日历 | 20821 |
| 宏观数据 | 宏观经济日历信息 | `get_macro_cal_info` | 宏观经济日历信息 | 20892 |
| 宏观数据 | 宏观经济日历配置 | `get_macro_cal_config` | 宏观经济日历配置 | 20944 |


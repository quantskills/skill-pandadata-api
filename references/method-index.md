# Pandadata Method Index

Generated from `api-docs.md`. Use line numbers with `sed -n '<line>,+120p' references/api-docs.md`, or run `python scripts/search_api_docs.py --method <method>`.

Total methods: 218

SDK 0.0.12 directly exports 201 of these documented methods.
The following documented gateway methods are not exported by the SDK:

`get_cumu_guarantee`, `get_investor_brief_detail`, `get_investor_brief_qa`, `get_stock_csrc_approval`, `get_stock_disclosure_date`, `get_stock_equity_illegal`, `get_stock_equity_nature`, `get_stock_equity_placard`, `get_stock_issuer_credit_rating`, `get_stock_litigation_arbitration`, `get_stock_material_contract`, `get_stock_preferred_detail`, `get_stock_preferred_dividend`, `get_stock_preferred_placement`, `get_stock_preferred_rating`, `get_stock_preferred_shares`, `get_stock_preferred_trading`

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
| A股数据 | 市场参考数据 | `get_stock_detail` | 获取股票基本信息 | 1417 |
| A股数据 | 市场参考数据 | `get_index_detail` | 获取指数基本信息 | 1475 |
| A股数据 | 行业基础数据 | `get_industry_constituents` | 获取行业成分股数据 | 1723 |
| A股数据 | 行业基础数据 | `get_industry_detail` | 获取行业基本信息数据 | 1773 |
| A股数据 | 行业基础数据 | `get_stock_industry` | 获取指定股票所属的行业信息 | 1847 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_daily` | 获取指数日线 | 1894 |
| A股数据 | 指数行情（上交所&深交所） | `get_index_min` | 获取指数分钟线 | 1960 |
| A股数据 | 指数基础数据 | `get_index_weights` | 获取指数权重信息数据 | 2216 |
| A股数据 | 指数基础数据 | `get_index_indicator` | 获取指数估值指标数据 | 2461 |
| A股数据 | 市场交易与资金数据 | `get_lhb_list` | 获取股票龙虎榜数据 | 2709 |
| A股数据 | 市场交易与资金数据 | `get_lhb_detail` | 获取股票龙虎榜明细数据 | 2937 |
| A股数据 | 市场交易与资金数据 | `get_margin` | 获取融资融券信息 | 3004 |
| A股数据 | 市场交易与资金数据 | `get_hsgt_hold` | 获取沪深股通持股信息 | 3074 |
| A股数据 | 公司行为 | `get_investor_activity` | 获取A股合约投资者关系活动 | 3121 |
| A股数据 | 公司行为 | `get_restricted_list` | 获取股票限售解禁明细数据 | 3166 |
| A股数据 | 公司行为 | `get_repurchase` | 获取回购数据 | 3220 |
| A股数据 | 公司行为 | `get_holder_count` | 获取股东数量 | 3286 |
| A股数据 | 公司行为 | `get_top_holders` | 获取A股股东信息 | 3336 |
| A股数据 | 公司行为 | `get_block_trade` | 获取A股大宗交易信息 | 3406 |
| A股数据 | 公司行为 | `get_share_float` | 获取股票股本数据 | 3455 |
| A股数据 | 公司行为 | `get_stock_dividend` | 获取股票分红信息 | 3663 |
| A股数据 | 公司行为 | `get_stock_split` | 获取股票拆分数据 | 3711 |
| A股数据 | 公司行为 | `get_stock_cash_dividend` | 获取股票现金分红数据 | 3758 |
| A股数据 | 公司行为 | `get_stock_dividend_amount` | 获取股票分红总额数据 | 3810 |
| A股数据 | 公司行为 | `get_stock_private_placement` | 获取股票定向增发数据 | 3859 |
| A股数据 | 公司行为 | `get_stock_allotment` | 获取股票配股信息 | 3910 |
| A股数据 | 公司行为 | `get_stock_disclosure_date` | 获取上市A股定期报告预披露数据 | 3961 |
| A股数据 | 公司行为 | `get_stock_status_over_allotment` | 获取超额配售权实施情况数据 | 4011 |
| A股数据 | 公司行为 | `get_stock_litigation_arbitration` | 获取上市公司诉讼仲裁数据 | 4067 |
| A股数据 | 公司行为 | `get_stock_csrc_approval` | 获取证监会批文数据 | 4128 |
| A股数据 | 公司行为 | `get_stock_competitor_information` | 获取竞争企业信息数据 | 4177 |
| A股数据 | 公司行为 | `get_stock_intermediary_information` | 获取中介情况信息表数据 | 4224 |
| A股数据 | 公司行为 | `get_stock_rela_party_trans` | 上市公司关联交易 | 4273 |
| A股数据 | 公司行为 | `get_cumu_guarantee` | 获取累计担保信息 | 4339 |
| A股数据 | 公司行为 | `get_stock_material_contract` | 获取上市公司重大合同数据 | 4416 |
| A股数据 | 公司行为 | `get_investor_brief_detail` | 获取投资者简报详情 | 4493 |
| A股数据 | 公司行为 | `get_investor_brief_qa` | 获取投资者简报问答 | 4737 |
| A股数据 | 公司行为 | `get_stock_equity_illegal` | 获取股权违规信息 | 4983 |
| A股数据 | 股东行为 | `get_stock_pledge` | 获取A股公司股权质押 | 5238 |
| A股数据 | 股东行为 | `get_stock_pledge_stat` | 获取股票质押信息统计 | 5497 |
| A股数据 | 股东行为 | `get_stock_shareholder_change` | 获取股东增减持计划 | 5743 |
| A股数据 | 股东行为 | `get_stock_equity_placard` | 获取被举牌公司明细 | 6005 |
| A股数据 | 业绩预告 | `get_fina_forecast` | 获取业绩预告数据 | 6069 |
| A股数据 | 财务三表、财务快报 | `get_fina_performance` | 获取财务快报数据 | 6127 |
| A股数据 | 财务三表、财务快报 | `get_fina_reports` | 获取财务季度报告 | 6211 |
| A股数据 | 财务三表、财务快报 | `get_audit_opinion` | 获取财务报告审计意见 | 6298 |
| A股数据 | 股东结构 | `get_stock_equity_nature` | 获取个股企业性质 | 6353 |
| 期货数据 | 期货行情数据 | `get_future_daily` | 获取期货日线 | 6597 |
| 期货数据 | 期货行情数据 | `get_future_daily_post` | 获取期货后复权数据 | 6672 |
| 期货数据 | 期货行情数据 | `get_future_min` | 获取期货分钟线 | 6763 |
| 期货数据 | 期货基本信息 | `get_future_detail` | 获取期货基本信息 | 7025 |
| 期货数据 | 期货主力合约信息 | `get_future_dominant` | 获取期货主力合约数据 | 7086 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg` | 获取席位净持仓保证金数据 | 7145 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netposi_rank` | 获取期货商品净持仓多空榜单数据 | 7389 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_netmarg_change` | 获取席位净持仓保证金变化数据 | 7619 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_grade` | 获取席位评级数据 | 7863 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_totlmarg` | 获取席位总持仓保证金数据 | 7925 |
| 期货数据 | 期货 DeepView 数据 | `get_future_basis` | 获取期货基差数据 | 8169 |
| 期货数据 | 期货 DeepView 数据 | `get_future_warehouse_receipt` | 获取期货仓单数据 | 8231 |
| 期货数据 | 期货 DeepView 数据 | `get_future_net_flow` | 获取期货净资金流列表 | 8293 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_indicators` | 获取期货龙虎比、牛熊线 | 8341 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_variety_profit` | 获取期货席位的商品盈亏数据 | 8411 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_posi` | 获取期货商品持仓数据 | 8467 |
| 期货数据 | 期货 DeepView 数据 | `get_future_symbol_posi` | 获取期货合约持仓数据 | 8526 |
| 期货数据 | 期货 DeepView 数据 | `get_future_ls_ratio` | 获取期货合约多空比数据 | 8584 |
| 期货数据 | 期货 DeepView 数据 | `get_future_netcap_change` | 获取期货合约净持仓市值变化数据 | 8824 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_rank` | 获取期货合约龙虎比、牛熊线排行 | 9067 |
| 期货数据 | 期货 DeepView 数据 | `get_future_term_structure` | 获取期货期限结构数据 | 9319 |
| 期货数据 | 期货 DeepView 数据 | `get_future_inventory` | 获取期货库存数据 | 9362 |
| 期货数据 | 期货 DeepView 数据 | `get_future_calendar_arbitrage` | 获取期货跨期套利数据 | 9405 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_spread` | 获取期货自由价差数据 | 9449 |
| 期货数据 | 期货 DeepView 数据 | `get_future_free_ratio` | 获取期货自由价比数据 | 9493 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_oi_value` | 获取期货席位合约的总持仓市值 | 9537 |
| 期货数据 | 期货 DeepView 数据 | `get_future_nonbroker_net` | 获取期货非期货公司净持仓 | 9585 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit` | 获取期货席位盈亏数据 | 9629 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_flow_daily` | 获取期货席位每日大资金流动数据 | 9675 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_ls_ratio` | 获取期货席位多空比数据 | 9726 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_loss_rank` | 获取期货席位亏损排行数据 | 9773 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_profit_rank` | 获取期货席位盈利排行数据 | 9815 |
| 期货数据 | 期货 DeepView 数据 | `get_broker_build_process` | 获取期货席位建仓过程数据 | 9857 |
| 期货数据 | 期货 DeepView 数据 | `get_future_trader_quote` | 获取期货现货贸易商报价数据 | 10105 |
| 期货数据 | 期货 DeepView 数据 | `get_future_virtual_ratio` | 获取期货虚实盘比数据 | 10350 |
| 期货数据 | 期货 DeepView 数据 | `get_future_spot_profit` | 获取期货利润数据 | 10394 |
| 期货数据 | 期货 DeepView 数据 | `get_future_variety_mcap` | 获取期货品种持仓市值数据 | 10439 |
| 期货数据 | 期货 DeepView 数据 | `get_future_dominant_corr` | 获取期货主力合约涨跌幅相关性 | 10481 |
| 期货数据 | 期货 DeepView 数据 | `get_future_contract_pool` | 获取期货多头空头合约池 | 10520 |
| 期权数据 | 期权基本信息 | `get_option_detail` | 获取期权基本信息 | 10574 |
| 期权数据 | 期权基本信息 | `get_option_underlying_detail` | 获取期权品种信息 | 10830 |
| 期权数据 | 期权基本信息 | `get_option_exercise` | 获取期权行权交收信息 | 10886 |
| 期权数据 | 期权基本信息 | `get_option_static` | 获取期权每日盘前静态数据 | 10930 |
| 期权数据 | 期权日线行情 | `get_option_daily` | 获取期权日线数据 | 11009 |
| 期权数据 | 期权日线行情 | `get_option_spot_market` | 获取期权现货日行情 | 11260 |
| 期权数据 | 期权波动率数据 | `get_option_implied_volatility` | 获取期权隐含波动率 | 11337 |
| 期权数据 | 期权波动率数据 | `get_option_underlying_volatility` | 获取期权标的历史波动率 | 11379 |
| 期权数据 | 期权波动率数据 | `get_option_risk_indicators` | 获取期权风险指标 | 11507 |
| 量化因子数据 | 回测因子 | `get_factor` | 获取回测因子 | 11560 |
| 量化因子数据 | 复权因子 | `get_adj_factor` | 获取复权因子 | 11644 |
| 港美股 | 行情数据 | `get_hk_daily` | 获取港股日线数据 | 11694 |
| 港美股 | 行情数据 | `get_us_daily` | 获取美股日线数据 | 11960 |
| 港美股 | 港股股票基础信息 | `get_hk_detail` | 获取港股的基本信息 | 12217 |
| 港美股 | 美股股票基础信息 | `get_us_detail` | 获取美股的基本信息 | 12282 |
| 港美股 | 港股公司事件 | `get_stock_dividend_event` | 获取股票分红相关的事件 | 12344 |
| 港美股 | 港股公司事件 | `get_stock_market_event` | 获取市场活动相关的事件 | 12395 |
| 港美股 | 港股公司事件 | `get_stock_meeting_event` | 获取公司会议相关的事件 | 12642 |
| 港美股 | 港股公司事件 | `get_stock_financial_event` | 获取财务披露相关的事件 | 12889 |
| 港美股 | 港股公司事件 | `get_stock_ir_event` | 获取投资者关系活动相关的事件 | 13136 |
| 港美股 | 美股公司事件 | `get_stock_dividend_activity` | 获取股票分红相关的事件 | 13385 |
| 港美股 | 美股公司事件 | `get_stock_market_activity` | 获取市场活动相关的事件 | 13436 |
| 港美股 | 美股公司事件 | `get_stock_meeting_activity` | 获取公司会议相关的事件 | 13683 |
| 港美股 | 美股公司事件 | `get_stock_financial_activity` | 获取财务披露相关的事件 | 13930 |
| 港美股 | 美股公司事件 | `get_stock_ir_activity` | 获取投资者关系活动相关的事件 | 14177 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_concentration` | 获取公司投资者集中度 | 14426 |
| 港美股 | 港股股东与投资者 | `get_stock_top20_concentration` | 获取公司前20投资者集中度 | 14667 |
| 港美股 | 港股股东与投资者 | `get_stock_investor_ranking` | 获取公司投资者排行 | 14908 |
| 港美股 | 港股股东与投资者 | `get_stock_insider_trade` | 获取公司内部人交易活动 | 15155 |
| 港美股 | 港股股东与投资者 | `get_stock_shareholder_holding` | 获取公司股东持股报告 | 15223 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_centralization` | 获取公司投资者集中度 | 15291 |
| 港美股 | 美股股东与投资者 | `get_stock_top20_centralization` | 获取公司前20投资者集中度 | 15532 |
| 港美股 | 美股股东与投资者 | `get_stock_investor_leaderboard` | 获取公司投资者排行 | 15773 |
| 港美股 | 美股股东与投资者 | `get_stock_insider_transaction` | 获取公司内部人交易活动 | 16020 |
| 港美股 | 美股股东与投资者 | `get_stock_shareholder_report` | 获取公司股东持股报告 | 16152 |
| 港美股 | 港股核心数据 | `get_stock_industry_median` | 获取公司最新行业中位统计数据 | 16230 |
| 港美股 | 港股核心数据 | `get_stock_pv_indicator` | 获取公司最新价量指标数据 | 16672 |
| 港美股 | 美股核心数据 | `get_stock_sector_median` | 获取公司最新行业中位统计数据 | 16937 |
| 港美股 | 美股核心数据 | `get_stock_pv_metric` | 获取公司最新价量指标数据 | 17379 |
| 港美股 | 港股一致预期数据 | `get_stock_ncycl_consensus` | 获取非周期性指标一致预期 | 17644 |
| 港美股 | 港股一致预期数据 | `get_stock_recommendation_consensus` | 获取买卖建议一致预期 | 17889 |
| 港美股 | 美股一致预期数据 | `get_stock_ncycl_estimate` | 获取非周期性指标一致预期 | 18139 |
| 港美股 | 美股一致预期数据 | `get_stock_recommendation_estimate` | 获取买卖建议一致预期 | 18384 |
| 港美股 | 港股财务数据 | `get_stock_operating_indicator` | 获取公司标准化营运指标 | 18634 |
| 港美股 | 港股财务数据 | `get_stock_mktfin_indicator` | 获取公司最新市场财务统计指标 | 18887 |
| 港美股 | 港股财务数据 | `get_fina_statement` | 获取财务季度报告 | 19270 |
| 港美股 | 美股财务数据 | `get_stock_operating_metric` | 获取公司标准化营运指标 | 19321 |
| 港美股 | 美股财务数据 | `get_stock_mktfin_metric` | 获取公司最新市场财务统计指标 | 19574 |
| 港美股 | 美股财务数据 | `get_fina_ex` | 获取财务季度报告 | 19957 |
| 宏观数据 | 宏观指标基础信息 | `get_macro_detail` | 宏观指标列表 | 20010 |
| 宏观数据 | 中国宏观指标 | `get_macro_na` | 中国宏观-国民经济核算 | 20267 |
| 宏观数据 | 中国宏观指标 | `get_macro_in` | 中国宏观-工业 | 20311 |
| 宏观数据 | 中国宏观指标 | `get_macro_ci` | 中国宏观-景气指数 | 20355 |
| 宏观数据 | 中国宏观指标 | `get_macro_pi` | 中国宏观-价格指数 | 20398 |
| 宏观数据 | 中国宏观指标 | `get_macro_fa` | 中国宏观-固定资产投资 | 20441 |
| 宏观数据 | 中国宏观指标 | `get_macro_fi` | 中国宏观-财政 | 20484 |
| 宏观数据 | 中国宏观指标 | `get_macro_mb` | 中国宏观-货币与银行 | 20527 |
| 宏观数据 | 中国宏观指标 | `get_macro_ir` | 中国宏观-利率汇率 | 20571 |
| 宏观数据 | 中国宏观指标 | `get_macro_fe` | 中国宏观-对外经济 | 20615 |
| 宏观数据 | 中国宏观指标 | `get_macro_dt` | 中国宏观-国内贸易 | 20658 |
| 宏观数据 | 中国宏观指标 | `get_macro_ew` | 中国宏观-就业与工资 | 20702 |
| 宏观数据 | 中国宏观指标 | `get_macro_li` | 中国宏观-人民生活 | 20746 |
| 宏观数据 | 中国宏观指标 | `get_macro_pr` | 中国宏观-人口与资源 | 20790 |
| 宏观数据 | 中国宏观指标 | `get_macro_se` | 中国宏观-科教体卫 | 20833 |
| 宏观数据 | 中国宏观指标 | `get_macro_sm` | 中国宏观-证券市场 | 20878 |
| 宏观数据 | 中国宏观指标 | `get_macro_pm` | 中国宏观-区域宏观 | 20922 |
| 宏观数据 | 国际宏观指标 | `get_macro_gb` | 宏观行业-国际宏观 | 20969 |
| 宏观数据 | 宏观行业数据 | `get_macro_ag` | 宏观行业-农林牧渔 | 21015 |
| 宏观数据 | 宏观行业数据 | `get_macro_en` | 宏观行业-能源 | 21059 |
| 宏观数据 | 宏观行业数据 | `get_macro_ch` | 宏观行业-化工 | 21103 |
| 宏观数据 | 宏观行业数据 | `get_macro_st` | 宏观行业-钢铁 | 21147 |
| 宏观数据 | 宏观行业数据 | `get_macro_nf` | 宏观行业-有色金属 | 21192 |
| 宏观数据 | 宏观行业数据 | `get_macro_bm` | 宏观行业-建材 | 21235 |
| 宏观数据 | 宏观行业数据 | `get_macro_au` | 宏观行业-汽车 | 21278 |
| 宏观数据 | 宏观行业数据 | `get_macro_me` | 宏观行业-机械设备 | 21321 |
| 宏观数据 | 宏观行业数据 | `get_macro_ee` | 宏观行业-电子电器 | 21365 |
| 宏观数据 | 宏观行业数据 | `get_macro_tm` | 宏观行业-TMT | 21409 |
| 宏观数据 | 宏观行业数据 | `get_macro_fb` | 宏观行业-食品饮料 | 21452 |
| 宏观数据 | 宏观行业数据 | `get_macro_te` | 宏观行业-纺织服装 | 21496 |
| 宏观数据 | 宏观行业数据 | `get_macro_pp` | 宏观行业-造纸印刷 | 21539 |
| 宏观数据 | 宏观行业数据 | `get_macro_ph` | 宏观行业-医药生物 | 21582 |
| 宏观数据 | 宏观行业数据 | `get_macro_ut` | 宏观行业-公用事业 | 21626 |
| 宏观数据 | 宏观行业数据 | `get_macro_tr` | 宏观行业-交通运输 | 21670 |
| 宏观数据 | 宏观行业数据 | `get_macro_rc` | 宏观行业-房地产及建筑业 | 21714 |
| 宏观数据 | 宏观行业数据 | `get_macro_th` | 宏观行业-旅游酒店 | 21758 |
| 宏观数据 | 宏观行业数据 | `get_macro_ce` | 宏观行业-文教体娱及工艺品 | 21801 |
| 宏观数据 | 宏观行业数据 | `get_macro_wr` | 宏观行业-批发零售业 | 21844 |
| 宏观数据 | 宏观行业数据 | `get_macro_fs` | 宏观行业-金融保险业 | 21887 |
| 宏观数据 | 宏观行业数据 | `get_macro_is` | 宏观行业-行业综合 | 21931 |
| 宏观数据 | 宏观特色数据 | `get_macro_ec` | 宏观特色数据-线上电商数据 | 21977 |
| 宏观数据 | 宏观特色数据 | `get_macro_md` | 宏观特色数据-医药数据 | 22020 |
| 宏观数据 | 宏观特色数据 | `get_macro_eh` | 宏观特色数据-能化数据 | 22063 |
| 宏观数据 | 宏观特色数据 | `get_macro_ad` | 宏观特色数据-汽车数据 | 22107 |
| 宏观数据 | 宏观特色数据 | `get_macro_ha` | 宏观特色数据-家电数据 | 22150 |
| 宏观数据 | 宏观特色数据 | `get_macro_of` | 宏观特色数据-线下商超数据 | 22193 |
| 宏观数据 | 宏观特色数据 | `get_macro_rb` | 宏观特色数据-招聘数据 | 22236 |
| 宏观数据 | 宏观特色数据 | `get_macro_re` | 宏观特色数据-房地产数据 | 22280 |
| 宏观数据 | 宏观特色数据 | `get_macro_ed` | 宏观特色数据-电子数据 | 22324 |
| 宏观数据 | 宏观特色数据 | `get_macro_ep` | 宏观特色数据-电新数据 | 22367 |
| 宏观数据 | 宏观特色数据 | `get_macro_ar` | 宏观特色数据-农业数据 | 22411 |
| 宏观数据 | 宏观特色数据 | `get_macro_cm` | 宏观特色数据-大宗数据 | 22455 |
| 宏观数据 | 宏观经济日历 | `get_macro_cal` | 宏观经济日历 | 22501 |
| 宏观数据 | 宏观经济日历信息 | `get_macro_cal_info` | 宏观经济日历信息 | 22573 |
| 宏观数据 | 宏观经济日历配置 | `get_macro_cal_config` | 宏观经济日历配置 | 22626 |
| 基金数据 | 基金基础数据 | `get_fund_detail` | 获取基金基本信息 | 22671 |
| 基金数据 | 基金行情数据 | `get_fund_daily` | 获取场内基金日行情数据 | 22980 |
| 基金数据 | 基金行情数据 | `get_fund_daily_post` | 获取场内基金后复权日行情数据 | 23090 |
| 基金数据 | 基金行情数据 | `get_fund_daily_pre` | 获取场内基金前复权日行情数据 | 23295 |
| 基金数据 | ETF数据 | `get_fund_etf_cr_limits` | 获取ETF申赎限制数据 | 23502 |
| 基金数据 | ETF数据 | `get_fund_etf_cr_net` | 获取ETF净申赎数据 | 23573 |
| 基金数据 | ETF数据 | `get_fund_etf_constituents` | 获取ETF基金申赎清单成分券信息 | 23649 |
| 基金数据 | ETF数据 | `get_fund_etf_cr` | 获取ETF基金申赎清单数据 | 23718 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_dividend` | 获取优先股分红 | 23795 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_trading` | 获取优先股成交统计信息 | 23872 |
| 优先股数据 | 优先股数据 | `get_stock_issuer_credit_rating` | 获取优先股发行主体信用评级 | 23938 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_rating` | 获取优先股评级情况 | 24006 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_shares` | 获取优先股股本 | 24057 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_placement` | 获取优先股配售结果 | 24122 |
| 优先股数据 | 优先股数据 | `get_stock_preferred_detail` | 获取优先股基本资料 | 24185 |

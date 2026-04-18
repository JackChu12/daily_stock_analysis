# -*- coding: utf-8 -*-
"""
===================================
全球指数与股票代码工具
===================================

提供：
1. 全球主要指数代码映射（美股 / 欧洲 / 亚太，如 SPX -> ^GSPC, FTSE -> ^FTSE）
2. 美股股票代码识别（AAPL、TSLA 等）
3. 马股 (Bursa Malaysia) 代码识别（1155.KL 等）

Yahoo Finance 中指数使用 ^ 前缀，马股使用 .KL 后缀。
"""

import re

# 美股代码正则：1-5 个大写字母，可选 .X 后缀（如 BRK.B）
_US_STOCK_PATTERN = re.compile(r'^[A-Z]{1,5}(\.[A-Z])?$')

# 马股代码正则：4-5 位数字（可带 .KL 后缀），如 1155, 1155.KL, 5347.KL
_KL_STOCK_PATTERN = re.compile(r'^[0-9]{4,5}\.KL$', re.IGNORECASE)


# 用户输入 -> (Yahoo Finance 符号, 中文名称)
US_INDEX_MAPPING = {
    # === 美股指数 ===
    # 标普 500
    'SPX': ('^GSPC', '标普500指数'),
    '^GSPC': ('^GSPC', '标普500指数'),
    'GSPC': ('^GSPC', '标普500指数'),
    # 道琼斯工业平均指数
    'DJI': ('^DJI', '道琼斯工业指数'),
    '^DJI': ('^DJI', '道琼斯工业指数'),
    'DJIA': ('^DJI', '道琼斯工业指数'),
    # 纳斯达克综合指数
    'IXIC': ('^IXIC', '纳斯达克综合指数'),
    '^IXIC': ('^IXIC', '纳斯达克综合指数'),
    'NASDAQ': ('^IXIC', '纳斯达克综合指数'),
    # 纳斯达克 100
    'NDX': ('^NDX', '纳斯达克100指数'),
    '^NDX': ('^NDX', '纳斯达克100指数'),
    # VIX 波动率指数
    'VIX': ('^VIX', 'VIX恐慌指数'),
    '^VIX': ('^VIX', 'VIX恐慌指数'),
    # 罗素 2000
    'RUT': ('^RUT', '罗素2000指数'),
    '^RUT': ('^RUT', '罗素2000指数'),

    # === 欧洲指数 ===
    # 富时 100（英国）
    'FTSE': ('^FTSE', '富时100指数'),
    '^FTSE': ('^FTSE', '富时100指数'),
    # 德国 DAX
    'DAX': ('^GDAXI', '德国DAX指数'),
    'GDAXI': ('^GDAXI', '德国DAX指数'),
    '^GDAXI': ('^GDAXI', '德国DAX指数'),
    # 法国 CAC 40
    'CAC': ('^FCHI', '法国CAC40指数'),
    'FCHI': ('^FCHI', '法国CAC40指数'),
    '^FCHI': ('^FCHI', '法国CAC40指数'),
    # 欧洲斯托克 50
    'STOXX50E': ('^STOXX50E', '欧洲斯托克50指数'),
    '^STOXX50E': ('^STOXX50E', '欧洲斯托克50指数'),

    # === 亚太指数 ===
    # 日经 225
    'N225': ('^N225', '日经225指数'),
    '^N225': ('^N225', '日经225指数'),
    'NIKKEI': ('^N225', '日经225指数'),
    # 恒生指数（香港）
    'HSI': ('^HSI', '恒生指数'),
    '^HSI': ('^HSI', '恒生指数'),
    # 富时大马 KLCI（马来西亚）
    'KLSE': ('^KLSE', '富时大马KLCI指数'),
    '^KLSE': ('^KLSE', '富时大马KLCI指数'),
    'KLCI': ('^KLSE', '富时大马KLCI指数'),
    # 韩国 KOSPI
    'KS11': ('^KS11', '韩国KOSPI指数'),
    '^KS11': ('^KS11', '韩国KOSPI指数'),
    'KOSPI': ('^KS11', '韩国KOSPI指数'),
    # 澳洲 ASX 200
    'AXJO': ('^AXJO', '澳洲ASX200指数'),
    '^AXJO': ('^AXJO', '澳洲ASX200指数'),
    # 印度 NIFTY 50
    'NSEI': ('^NSEI', '印度NIFTY50指数'),
    '^NSEI': ('^NSEI', '印度NIFTY50指数'),
    'NIFTY': ('^NSEI', '印度NIFTY50指数'),
    # 新加坡海峡时报指数
    'STI': ('^STI', '新加坡海峡时报指数'),
    '^STI': ('^STI', '新加坡海峡时报指数'),

    # === 商品 / 货币 / 利率 ===
    # 美元指数
    'DXY': ('DX-Y.NYB', '美元指数'),
    # 黄金（COMEX 期货）
    'GOLD': ('GC=F', '黄金期货'),
    'GC': ('GC=F', '黄金期货'),
    # WTI 原油
    'WTI': ('CL=F', 'WTI原油期货'),
    'CL': ('CL=F', 'WTI原油期货'),
    # 美国 10 年期国债收益率
    'TNX': ('^TNX', '美国10年期国债收益率'),
    '^TNX': ('^TNX', '美国10年期国债收益率'),
    # 比特币（USD）
    'BTC': ('BTC-USD', '比特币(USD)'),
    'BTCUSD': ('BTC-USD', '比特币(USD)'),
}


def is_us_index_code(code: str) -> bool:
    """
    判断代码是否为美股指数符号。

    Args:
        code: 股票/指数代码，如 'SPX', 'DJI'

    Returns:
        True 表示是已知美股指数符号，否则 False

    Examples:
        >>> is_us_index_code('SPX')
        True
        >>> is_us_index_code('AAPL')
        False
    """
    return (code or '').strip().upper() in US_INDEX_MAPPING


def is_us_stock_code(code: str) -> bool:
    """
    判断代码是否为美股股票符号（排除美股指数）。

    美股股票代码为 1-5 个大写字母，可选 .X 后缀如 BRK.B。
    美股指数（SPX、DJI 等）明确排除。

    Args:
        code: 股票代码，如 'AAPL', 'TSLA', 'BRK.B'

    Returns:
        True 表示是美股股票符号，否则 False

    Examples:
        >>> is_us_stock_code('AAPL')
        True
        >>> is_us_stock_code('TSLA')
        True
        >>> is_us_stock_code('BRK.B')
        True
        >>> is_us_stock_code('SPX')
        False
        >>> is_us_stock_code('600519')
        False
    """
    normalized = (code or '').strip().upper()
    # 美股指数不是股票
    if normalized in US_INDEX_MAPPING:
        return False
    return bool(_US_STOCK_PATTERN.match(normalized))


def get_us_index_yf_symbol(code: str) -> tuple:
    """
    获取美股指数的 Yahoo Finance 符号与中文名称。

    Args:
        code: 用户输入，如 'SPX', '^GSPC', 'DJI'

    Returns:
        (yf_symbol, chinese_name) 元组，未找到时返回 (None, None)。

    Examples:
        >>> get_us_index_yf_symbol('SPX')
        ('^GSPC', '标普500指数')
        >>> get_us_index_yf_symbol('AAPL')
        (None, None)
    """
    normalized = (code or '').strip().upper()
    return US_INDEX_MAPPING.get(normalized, (None, None))


def is_kl_stock_code(code: str) -> bool:
    """
    判断代码是否为马来西亚交易所 (Bursa Malaysia) 股票符号。

    马股 Yahoo Finance 格式：4-5 位数字 + .KL 后缀
    例：1155.KL (Maybank), 5347.KL (Tenaga Nasional), 6033.KL (Petronas Gas)

    Args:
        code: 股票代码

    Returns:
        True 表示是马股代码，否则 False

    Examples:
        >>> is_kl_stock_code('1155.KL')
        True
        >>> is_kl_stock_code('5347.KL')
        True
        >>> is_kl_stock_code('AAPL')
        False
        >>> is_kl_stock_code('600519')
        False
    """
    normalized = (code or '').strip().upper()
    return bool(_KL_STOCK_PATTERN.match(normalized))

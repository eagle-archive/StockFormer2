import os

TRAINED_MODEL_DIR = "trained_models"
TENSORBOARD_LOG_DIR = "tensorboard_log"
RESULTS_DIR = "results"

START_DATE = "2010-01-01"
END_DATE = "2022-05-07"

INF = 1100

## Model Parameters
MAESAC_PARAMS = {
    "batch_size": 64,
    "buffer_size": 100000,
    "learning_rate": 0.0001,
    "learning_starts": 100,
    "ent_coef": "auto_0.1",
    "enc_in": 108,
    "dec_in": 108,
    "c_out_prediction": 1,
    "d_model": 128,
    "n_heads": 8,
    "e_layers": 3,
    "d_layers": 2,
    "d_ff": 256,
    "dropout": 0.05,
    "pred_len": 1,
    "seq_len": 60,
}

ADDITIONAL_FEATURE = [
    'label_short_term',
    'label_long_term'
]

TEMPORAL_FEATURE = [
    'open',
    'close',
    'high',
    'low',
    'volume',
    'dopen',
    'dclose',
    'dhigh',
    'dlow',
    'dvolume'
]

NORMALIZED_TEMPORAL_FEATURE = [
    'open',
    'close',
    'high',
    'low',
    'volume'
]

## stockstats technical indicator column names
## check https://pypi.org/project/stockstats/ for different names
TECHNICAL_INDICATORS_LIST = [
    "macd",
    "boll_ub",
    "boll_lb",
    "rsi_30",
    "cci_30",
    "dx_30",
    "close_30_sma",
    "close_60_sma",
    # "return_ratio",
]

# use CSI -300 ticker
USE_CSI_300_TICKET = ['600519.SS',
                      '601318.SS',
                      '600036.SS',
                      '000858.SZ',
                      '600276.SS',
                      '601166.SS',
                      '601888.SS',
                      '300059.SZ',
                      '000651.SZ',
                      '600900.SS',
                      '600887.SS',
                      '000001.SZ',
                      '000725.SZ',
                      '600030.SS',
                      '300015.SZ',
                      '601398.SS',
                      '000568.SZ',
                      '600031.SS',
                      '600309.SS',
                      '000002.SZ',
                      '600809.SS',
                      '601919.SS',
                      '002142.SZ',
                      '600436.SS',
                      '601328.SS',
                      '601899.SS',
                      '002304.SZ',
                      '002352.SZ',
                      '002230.SZ',
                      '300014.SZ',
                      '600000.SS',
                      '600438.SS',
                      '600837.SS',
                      '000661.SZ',
                      '000100.SZ',
                      '000063.SZ',
                      '002241.SZ',
                      '002271.SZ',
                      '600585.SS',
                      '600690.SS',
                      '601601.SS',
                      '601668.SS',
                      '002027.SZ',
                      '600016.SS',
                      '600763.SS',
                      '600196.SS',
                      '000338.SZ',
                      '600048.SS',
                      '600703.SS',
                      '002129.SZ',
                      '600050.SS',
                      '601688.SS',
                      '600660.SS',
                      '600104.SS',
                      '600570.SS',
                      '601766.SS',
                      '601169.SS',
                      '600999.SS',
                      '002311.SZ',
                      '002371.SZ',
                      '600019.SS',
                      '002049.SZ',
                      '600406.SS',
                      '601088.SS',
                      '601988.SS',
                      '000538.SZ',
                      '000625.SZ',
                      '600745.SS',
                      '600028.SS',
                      '600893.SS',
                      '600346.SS',
                      '601628.SS',
                      '600588.SS',
                      '601009.SS',
                      '601390.SS',
                      '601857.SS',
                      '600009.SS',
                      '600132.SS',
                      '600584.SS',
                      '000776.SZ',
                      '000895.SZ',
                      '002001.SZ',
                      '600111.SS',
                      '600426.SS',
                      '601939.SS',
                      '000166.SZ',
                      '002050.SZ',
                      '002179.SZ']

USE_N100_TICKET = os.listdir('/opt/project/data/N100')
USE_N100_TICKET = [file.replace('.csv', '') for file in USE_N100_TICKET]

use_ticker_dict = {'CSI': USE_CSI_300_TICKET, 'N100': USE_N100_TICKET, 'TEST': USE_CSI_300_TICKET[:5]}

CSI_date = ['20110117', '20180801', '20180508', '20201231', '20210104', '20220426']

date_dict = {'CSI': CSI_date, 'N100': CSI_date, 'TEST': CSI_date}

time_window_start = [59,
                     176,
                     346,
                     117,
                     633,
                     883,
                     899,
                     307,
                     682,
                     899,
                     596,
                     258,
                     880,
                     109,
                     822,
                     263,
                     918,
                     274,
                     495,
                     695,
                     716,
                     477,
                     751,
                     487,
                     719,
                     499,
                     638,
                     610,
                     679,
                     510,
                     157,
                     591,
                     889,
                     854,
                     271,
                     547,
                     78,
                     910,
                     83,
                     452,
                     176,
                     327,
                     100,
                     498,
                     681,
                     725,
                     259,
                     551,
                     149,
                     528,
                     607,
                     497,
                     109,
                     135,
                     349,
                     879,
                     432,
                     96,
                     428,
                     375,
                     455,
                     584,
                     284,
                     233,
                     778,
                     588,
                     345,
                     701,
                     255,
                     762,
                     387,
                     819,
                     314,
                     915,
                     137,
                     429,
                     882,
                     525,
                     748,
                     626,
                     637,
                     341,
                     653,
                     795,
                     914,
                     263,
                     83,
                     138,
                     878,
                     221,
                     848,
                     740,
                     869,
                     819,
                     773,
                     168,
                     355,
                     829,
                     860,
                     78,
                     472,
                     781,
                     235,
                     144,
                     319,
                     268,
                     175,
                     94,
                     664,
                     568,
                     769,
                     105,
                     168,
                     159,
                     346,
                     681,
                     881,
                     886,
                     495,
                     404,
                     400,
                     167,
                     851,
                     708,
                     351,
                     777,
                     875,
                     225,
                     318,
                     406,
                     467,
                     565,
                     864,
                     518,
                     288,
                     673,
                     578,
                     690,
                     583,
                     198,
                     551,
                     275,
                     626,
                     640,
                     934,
                     486,
                     120,
                     455,
                     86,
                     310,
                     462,
                     710,
                     845,
                     793,
                     619,
                     530,
                     599,
                     782,
                     773,
                     481,
                     706,
                     130,
                     121,
                     681,
                     619,
                     821,
                     422,
                     797,
                     699,
                     641,
                     375,
                     877,
                     129,
                     568,
                     148,
                     504,
                     173,
                     355,
                     781,
                     890,
                     230,
                     360,
                     360,
                     441,
                     317,
                     442,
                     842,
                     652,
                     705,
                     457,
                     297,
                     361,
                     668,
                     377,
                     674,
                     75,
                     227,
                     401,
                     711,
                     796,
                     752,
                     156,
                     320,
                     650,
                     651,
                     860,
                     876,
                     644,
                     481,
                     426,
                     564,
                     422,
                     356,
                     228,
                     527,
                     657,
                     219,
                     777,
                     77,
                     867,
                     728,
                     208,
                     283,
                     399,
                     85,
                     553,
                     463,
                     849,
                     535,
                     299,
                     567,
                     628,
                     730,
                     406,
                     688,
                     240,
                     811,
                     827,
                     184,
                     904,
                     829,
                     558,
                     382,
                     463,
                     75,
                     670,
                     319,
                     639,
                     114,
                     126,
                     873,
                     423,
                     933,
                     802,
                     470,
                     81,
                     490,
                     146,
                     714,
                     834,
                     809,
                     933,
                     488,
                     78,
                     440,
                     706,
                     921,
                     549,
                     539,
                     305,
                     628,
                     753,
                     433,
                     178,
                     382,
                     166,
                     327,
                     776,
                     892,
                     134,
                     393,
                     916,
                     808,
                     196,
                     714,
                     453,
                     530,
                     332,
                     897,
                     362,
                     399,
                     635,
                     130,
                     128,
                     887,
                     167,
                     776,
                     98,
                     675,
                     312,
                     377,
                     729,
                     480,
                     188,
                     71,
                     777,
                     831,
                     253,
                     504,
                     716,
                     673,
                     496,
                     339,
                     359,
                     638,
                     374,
                     249,
                     562,
                     577,
                     313,
                     628,
                     771,
                     870,
                     535,
                     630,
                     202,
                     362,
                     64,
                     893,
                     176,
                     780,
                     459,
                     293,
                     442,
                     933,
                     402,
                     73,
                     764,
                     738,
                     712,
                     167,
                     185,
                     294,
                     771,
                     235,
                     782,
                     266,
                     150,
                     360,
                     684,
                     702,
                     583,
                     100,
                     137,
                     198,
                     70,
                     674,
                     817,
                     401,
                     562,
                     230,
                     95,
                     784,
                     629,
                     503,
                     538,
                     157,
                     822,
                     699,
                     916,
                     609,
                     236,
                     611,
                     897,
                     868,
                     240,
                     877,
                     693,
                     128,
                     453,
                     73,
                     777,
                     852,
                     539,
                     762,
                     692,
                     397,
                     683,
                     638,
                     209,
                     267,
                     158,
                     663,
                     713,
                     714,
                     195,
                     151,
                     171,
                     794,
                     574,
                     420,
                     150,
                     789,
                     261,
                     305,
                     547,
                     552,
                     367,
                     888,
                     494,
                     125,
                     701,
                     885,
                     638,
                     801,
                     117,
                     483,
                     250,
                     361,
                     815,
                     872,
                     518,
                     84,
                     220,
                     75,
                     190,
                     632,
                     145,
                     628,
                     560,
                     155,
                     694,
                     248,
                     620,
                     611,
                     284,
                     690,
                     532,
                     901,
                     383,
                     651,
                     422,
                     660,
                     436,
                     687,
                     653,
                     912,
                     175,
                     833,
                     347,
                     574,
                     432,
                     574,
                     873,
                     353,
                     526,
                     384,
                     774,
                     190,
                     102,
                     465,
                     301,
                     216,
                     313,
                     196,
                     550,
                     777,
                     435,
                     586,
                     204,
                     651,
                     650,
                     64,
                     892,
                     720,
                     629,
                     699,
                     820,
                     311,
                     584,
                     647,
                     430,
                     721,
                     905,
                     702,
                     280,
                     162,
                     175,
                     153,
                     675,
                     83,
                     405,
                     783,
                     135,
                     142,
                     841,
                     196,
                     712,
                     823,
                     359]

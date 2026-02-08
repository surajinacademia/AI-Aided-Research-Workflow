# Road Accident Dataset — Summary Report
## 1. Data structure report
### 1.1 Schema
- **Rows:** 132,000
- **Columns:** 30

| Column | Dtype | Kind | Notes |
|--------|--------|------|------|
| Country | object | categorical |  |
| Year | int64 | numeric |  |
| Month | object | categorical |  |
| Day of Week | object | categorical |  |
| Time of Day | object | categorical |  |
| Urban/Rural | object | categorical |  |
| Road Type | object | categorical |  |
| Weather Conditions | object | categorical |  |
| Visibility Level | float64 | numeric | e.g. metres |
| Number of Vehicles Involved | int64 | numeric |  |
| Speed Limit | int64 | numeric |  |
| Driver Age Group | object | categorical |  |
| Driver Gender | object | categorical |  |
| Driver Alcohol Level | float64 | numeric | 0–1 scale |
| Driver Fatigue | int64 | numeric |  |
| Vehicle Condition | object | categorical |  |
| Pedestrians Involved | int64 | numeric |  |
| Cyclists Involved | int64 | numeric |  |
| Accident Severity | object | categorical |  |
| Number of Injuries | int64 | numeric |  |
| Number of Fatalities | int64 | numeric |  |
| Emergency Response Time | float64 | numeric | e.g. minutes |
| Traffic Volume | float64 | numeric |  |
| Road Condition | object | categorical |  |
| Accident Cause | object | categorical |  |
| Insurance Claims | int64 | numeric |  |
| Medical Cost | float64 | numeric |  |
| Economic Loss | float64 | numeric |  |
| Region | object | categorical |  |
| Population Density | float64 | numeric |  |

### 1.2 Quality checks

**Missing values:**

| Column | Missing | % |
|--------|---------|---|
No missing values.

**Duplicate rows:** 0

**Key numeric ranges:**

- Year: min=2000, max=2024
- Number of Fatalities: min=0, max=4
- Number of Injuries: min=0, max=19
- Speed Limit: min=30, max=119

### 1.3 Univariate summaries (categorical)

**Country** (10 distinct): Canada(13,349), Australia(13,345), Brazil(13,318), Germany(13,293), India(13,238), UK(13,186), USA(13,125), China(13,121) ...
**Month** (12 distinct): May(11,158), June(11,122), March(11,072), February(11,064), April(11,063), September(11,047), July(11,000), October(10,986) ...
**Day of Week** (7 distinct): Tuesday(19,061), Wednesday(19,001), Sunday(18,939), Friday(18,854), Saturday(18,818), Monday(18,708), Thursday(18,619)
**Time of Day** (4 distinct): Night(33,231), Evening(33,021), Afternoon(32,960), Morning(32,788)
**Urban/Rural** (2 distinct): Rural(66,502), Urban(65,498)
**Road Type** (3 distinct): Main Road(44,197), Highway(43,920), Street(43,883)
**Weather Conditions** (5 distinct): Windy(26,626), Rainy(26,562), Clear(26,426), Snowy(26,249), Foggy(26,137)
**Vehicle Condition** (3 distinct): Good(44,094), Poor(43,993), Moderate(43,913)
**Road Condition** (4 distinct): Wet(33,356), Snow-covered(33,010), Dry(32,855), Icy(32,779)
**Accident Cause** (5 distinct): Drunk Driving(26,506), Distracted Driving(26,460), Speeding(26,446), Mechanical Failure(26,343), Weather(26,245)
**Accident Severity** (3 distinct): Minor(44,063), Moderate(44,002), Severe(43,935)
**Driver Age Group** (5 distinct): <18(26,524), 18-25(26,500), 26-40(26,492), 61+(26,309), 41-60(26,175)
**Driver Gender** (2 distinct): Male(66,098), Female(65,902)
**Region** (5 distinct): Australia(26,625), North America(26,415), Asia(26,351), Europe(26,345), South America(26,264)
### 1.4 Univariate summaries (numeric)

```
            Year  Visibility Level  Number of Vehicles Involved  Speed Limit  Driver Alcohol Level  Driver Fatigue  Pedestrians Involved  Cyclists Involved  Number of Injuries  Number of Fatalities  Emergency Response Time  Traffic Volume  Insurance Claims  Medical Cost  Economic Loss  Population Density
count  132000.00         132000.00                    132000.00    132000.00             132000.00        132000.0             132000.00          132000.00           132000.00             132000.00                132000.00       132000.00         132000.00     132000.00      132000.00           132000.00
mean     2011.97            275.04                         2.50        74.54                  0.13             0.5                  1.00               1.00                9.51                  2.00                    32.49         5041.93              4.50      25198.45       50437.51             2506.48
std         7.20            129.92                         1.12        26.00                  0.07             0.5                  0.82               0.82                5.77                  1.41                    15.89         2860.67              2.87      14274.77       28584.29             1440.65
min      2000.00             50.00                         1.00        30.00                  0.00             0.0                  0.00               0.00                0.00                  0.00                     5.00          100.06              0.00        500.11        1000.34               10.00
25%      2006.00            162.34                         2.00        52.00                  0.06             0.0                  0.00               0.00                5.00                  1.00                    18.73         2560.60              2.00      12836.93       25692.82             1258.16
50%      2012.00            274.67                         3.00        74.00                  0.13             1.0                  1.00               1.00                9.00                  2.00                    32.53         5037.91              4.00      25188.20       50395.50             2506.20
75%      2018.00            388.01                         3.00        97.00                  0.19             1.0                  2.00               2.00               15.00                  3.00                    46.29         7524.64              7.00      37529.02       75186.63             3756.65
max      2024.00            500.00                         4.00       119.00                  0.25             1.0                  2.00               2.00               19.00                  4.00                    60.00        10000.00              9.00      49999.93       99999.62             4999.99
```

### 1.5 Cross-checks

**Country vs Region:** Some countries appear in multiple regions (e.g. ['Australia', 'Brazil', 'Canada', 'China', 'Germany']).

**Severe accidents with fatalities:** 35,166 of 43,935 severe.

## 2. Geographic findings

**Top countries by accident count:**

```
  Country  accidents  total_fatalities  total_injuries  fatalities_per_accident
   Canada      13349             26566          126733                   1.9901
Australia      13345             26837          126912                   2.0110
   Brazil      13318             26589          127753                   1.9965
  Germany      13293             26444          126930                   1.9893
    India      13238             26539          125739                   2.0048
       UK      13186             26402          125508                   2.0023
      USA      13125             26214          124416                   1.9973
    China      13121             26051          124277                   1.9854
    Japan      13049             26186          124019                   2.0067
   Russia      12976             25570          122796                   1.9706
```

**Top regions by accident count:**

```
       Region  accidents  total_fatalities  total_injuries  fatalities_per_accident
    Australia      26625             53045          252351                   1.9923
North America      26415             52770          252887                   1.9977
         Asia      26351             52450          248362                   1.9904
       Europe      26345             52844          251966                   2.0058
South America      26264             52289          249517                   1.9909
```



Plots saved: `geo_country_accidents_fatalities.svg`, `geo_region_accidents.svg`.

## 3. Temporal findings

**By time of day:**

```
             accidents  fatalities
Time of Day                       
Morning          32788       65312
Afternoon        32960       65267
Evening          33021       65935
Night            33231       66884
```

**By day of week:**

```
             accidents  fatalities
Day of Week                       
Monday           18708       37138
Tuesday          19061       37824
Wednesday        19001       38133
Thursday         18619       37408
Friday           18854       37824
Saturday         18818       37249
Sunday           18939       37822
```

**By month:**

```
           accidents  fatalities
Month                           
January        10952       22143
February       11064       22194
March          11072       22096
April          11063       22108
May            11158       22105
June           11122       22155
July           11000       21833
August         10791       21436
September      11047       22226
October        10986       21935
November       10836       21514
December       10909       21653
```

**By year:**

```
      accidents  fatalities
Year                       
2000       5280       10491
2001       5263       10615
2002       5433       10951
2003       5327       10601
2004       5180       10385
2005       5302       10670
2006       5156       10334
2007       5307       10635
2008       5409       10917
2009       5298       10539
2010       5144       10271
2011       5356       10695
2012       5327       10732
2013       5220       10250
2014       5351       10464
2015       5331       10544
2016       5377       10897
2017       5278       10566
2018       5295       10504
2019       5243       10462
2020       5308       10460
2021       5243       10451
2022       5175       10444
2023       5242       10544
2024       5155        9976
```

Plots saved: `temporal_patterns.svg`.

## 4. Deeper insights

### 4.1 Accident severity by cause

```
Accident Severity   Minor  Moderate  Severe
Accident Cause                             
Distracted Driving   8687      8908    8865
Drunk Driving        8841      8842    8823
Mechanical Failure   8804      8786    8753
Speeding             8838      8847    8761
Weather              8893      8619    8733
```

### 4.2 Urban vs rural

```
             accidents  total_fatalities  avg_injuries  fatalities_per_accident
Urban/Rural                                                                    
Rural            66502            132596          9.53                   1.9939
Urban            65498            130802          9.49                   1.9970
```

### 4.3 Fatalities by driver age group

```
                  accidents  total_fatalities  fatalities_per_accident
Driver Age Group                                                      
<18                   26524             52499                   1.9793
18-25                 26500             53114                   2.0043
26-40                 26492             52932                   1.9980
41-60                 26175             52287                   1.9976
61+                   26309             52566                   1.9980
```

### 4.4 Emergency response time by severity

```
                    mean  median  count
Accident Severity                      
Minor              32.52   32.59  44063
Moderate           32.51   32.48  44002
Severe             32.45   32.52  43935
```

Plot saved: `insight_fatalities_by_cause.svg`.


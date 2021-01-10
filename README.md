# Cognitive-Services-App

# Skład zespolu
1. Mateusz Karwowski - lider
2. Krzysztof Kończak
3. Dzmitry Kaliada

# Technologie
1. Python
2. Computer Vision
3. Cognitive Services

# Harmonogram
1. Zakres funkcjonalny - 1 tyg
2. Podział prac - 2 tyg
3. Implementacja - 3 tyg
4. Testy manualne - 4 tyg
5. Sprawozdanie końcowe - 5 tyg
6. Prezentacja - 6 tyg

# RAPORT KOŃCOWY

### Temat projektu

Optyczne rozpoznawanie znaków przy pomocy rozwiązań Cognitive Services dostarczanych przez platformę Azure.

### Cel projektu

Głównym cele projektu było sprawdzenie dwóch metod rozpoznawania znaków: OCR oraz READ API, sposobu ich użycia oraz porównania ze sobą. 

### READ API

READ API to jedna z nowszych technologii platformy Azure. Jest zoptymalizowana pod kątem wydzielania tekstu z obrazów i wielostronicowych dokumentów PDF z kilkoma językami. Wykrywa zarówno tekst pisany jak i drukowany na obrazie.

### Wymagania wejściowe READ API (co do obrazu)

-	Obsługiwane formaty plików: JPEG, PNG, BMP, PDF i TIFF
-	W przypadku plików PDF i TIFF, do 2000 stron (tylko pierwsze dwie strony dla warstwy Bezpłatna) są przetwarzane.
-	Rozmiar pliku musi być mniejszy niż 50 MB (4 MB dla warstwy Bezpłatna) i wymiary co najmniej 50 x 50 pikseli i maksymalnie 10000 x 10000 pikseli.
-	Wymiary PDF muszą mieć co najwyżej 17 x 17 cali, odpowiadające rozmiarowi papieru legalnego lub A3 i mniejszym.

### Wywołanie odczytu

W sposób asynchroniczny interfejs API wyodrębnia tekst z pobranego obrazu. Wywołanie zwraca w odpowiedzi pole nagłówka o nazwie Operation-Location. Wartość Operation-Location zawiera adres URL, który jest identyfikatorem operacji, która ma zostać wykonana w następnym kroku.

### Wywołanie operacji Get Results
Drugim krokiem jest wywołanie operacji Get Results wyniki . Ta operacja przyjmuje jako dane wejściowe Identyfikator operacji, który został utworzony przez operację odczytu. Zwraca odpowiedź JSON, która zawiera pole stanu z następującymi możliwymi wartościami. Tę operację można wywołać iteracyjnie, dopóki nie zwróci wartości z wartością sukces .
Gdy wartość w polu stan zostanie zakończona pomyślnie , odpowiedź JSON zawiera wyodrębnioną zawartość tekstową z obrazu lub dokumentu. Odpowiedź JSON zachowuje pierwotną grupę wierszy rozpoznanych wyrazów. Zawiera wyodrębnione wiersze tekstu.

### Przykład
```
{
   "status":"succeeded",
   "createdDateTime":"2021-01-10T14:00:55Z",
   "lastUpdatedDateTime":"2021-01-10T14:00:55Z",
   "analyzeResult":{
      "version":"3.0.0",
      "readResults":[
         {
            "page":1,
            "angle":0.1137,
            "width":614,
            "height":462,
            "unit":"pixel",
            "lines":[
               {
                  "boundingBox":[
                     29,
                     77,
                     296,
                     78,
                     296,
                     103,
                     29,
                     100
                  ],
                  "text":"\"Insanity: doing",
                  "words":[
                     {
                        "boundingBox":[
                           29,
                           78,
                           200,
                           78,
                           200,
                           103,
                           30,
                           98
                        ],
                        "text":"\"Insanity:",
                        "confidence":0.833
                     },
                     {
                        "boundingBox":[
                           211,
                           78,
                           296,
                           78,
                           295,
                           103,
                           210,
                           103
                        ],
                        "text":"doing",
                        "confidence":0.986
                     }
                  ]
               },
               {
                  "boundingBox":[
                     28,
                     110,
                     262,
                     111,
                     262,
                     136,
                     28,
                     134
                  ],
                  "text":"the same thing",
                  "words":[
                     {
                        "boundingBox":[
                           28,
                           111,
                           82,
                           111,
                           82,
                           133,
                           29,
                           132
                        ],
                        "text":"the",
                        "confidence":0.987
                     },
                     {
                        "boundingBox":[
                           95,
                           111,
                           167,
                           111,
                           165,
                           134,
                           94,
                           133
                        ],
                        "text":"same",
                        "confidence":0.986
                     },
                     {
                        "boundingBox":[
                           179,
                           111,
                           262,
                           111,
                           260,
                           136,
                           178,
                           135
                        ],
                        "text":"thing",
                        "confidence":0.983
                     }
                  ]
               },
               {
                  "boundingBox":[
                     27,
                     144,
                     245,
                     144,
                     245,
                     166,
                     27,
                     167
                  ],
                  "text":"over and over",
                  "words":[
                     {
                        "boundingBox":[
                           27,
                           147,
                           97,
                           145,
                           98,
                           168,
                           28,
                           168
                        ],
                        "text":"over",
                        "confidence":0.987
                     },
                     {
                        "boundingBox":[
                           110,
                           145,
                           164,
                           145,
                           165,
                           168,
                           111,
                           168
                        ],
                        "text":"and",
                        "confidence":0.983
                     },
                     {
                        "boundingBox":[
                           178,
                           145,
                           245,
                           146,
                           245,
                           167,
                           178,
                           168
                        ],
                        "text":"over",
                        "confidence":0.987
                     }
                  ]
               },
               {
                  "boundingBox":[
                     27,
                     179,
                     179,
                     177,
                     180,
                     200,
                     27,
                     202
                  ],
                  "text":"again and",
                  "words":[
                     {
                        "boundingBox":[
                           27,
                           180,
                           115,
                           178,
                           115,
                           202,
                           28,
                           203
                        ],
                        "text":"again",
                        "confidence":0.986
                     },
                     {
                        "boundingBox":[
                           128,
                           178,
                           180,
                           178,
                           180,
                           200,
                           128,
                           201
                        ],
                        "text":"and",
                        "confidence":0.987
                     }
                  ]
               },
               {
                  "boundingBox":[
                     29,
                     212,
                     178,
                     211,
                     178,
                     236,
                     29,
                     236
                  ],
                  "text":"expecting",
                  "words":[
                     {
                        "boundingBox":[
                           30,
                           215,
                           177,
                           212,
                           177,
                           237,
                           30,
                           234
                        ],
                        "text":"expecting",
                        "confidence":0.981
                     }
                  ]
               },
               {
                  "boundingBox":[
                     27,
                     242,
                     178,
                     244,
                     178,
                     266,
                     27,
                     265
                  ],
                  "text":"different",
                  "words":[
                     {
                        "boundingBox":[
                           28,
                           243,
                           178,
                           245,
                           179,
                           266,
                           28,
                           265
                        ],
                        "text":"different",
                        "confidence":0.983
                     }
                  ]
               },
               {
                  "boundingBox":[
                     29,
                     278,
                     158,
                     277,
                     158,
                     299,
                     29,
                     300
                  ],
                  "text":"results.",
                  "words":[
                     {
                        "boundingBox":[
                           29,
                           280,
                           158,
                           278,
                           157,
                           300,
                           29,
                           300
                        ],
                        "text":"results.",
                        "confidence":0.939
                     }
                  ]
               },
               {
                  "boundingBox":[
                     27,
                     342,
                     279,
                     342,
                     279,
                     367,
                     27,
                     366
                  ],
                  "text":"Albert Einstein",
                  "words":[
                     {
                        "boundingBox":[
                           27,
                           343,
                           135,
                           343,
                           135,
                           367,
                           27,
                           367
                        ],
                        "text":"Albert",
                        "confidence":0.86
                     },
                     {
                        "boundingBox":[
                           143,
                           343,
                           280,
                           343,
                           280,
                           367,
                           143,
                           367
                        ],
                        "text":"Einstein",
                        "confidence":0.983
                     }
                  ]
               }
            ]
         }
      ]
   }
}
```

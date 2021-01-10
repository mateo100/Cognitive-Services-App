# Cognitive-Services-App

# Skład zespolu

1. Mateusz Karwowski - lider (READ API + sprawozdanie + wnioski)
2. Krzysztof Kończak (OCR API + sprawozdanie + wnioski)
3. Dzmitry Kaliada (Porównanie dwóch metod (READ z OCR) + testy manualne + wnioski)

# Technologie

1. Python
2. Computer Vision
3. Cognitive Services (OCR API, READ API)
4. Pycharm
5. Matplotlib

# Harmonogram

1. Zakres funkcjonalny - 1 tyg OK.
2. Podział prac - 2 tyg OK.
3. Implementacja - 3 tyg OK.
4. Testy manualne - 4 tyg OK.
5. Sprawozdanie końcowe - 5 tyg OK.
6. Prezentacja - 6 tyg

# RAPORT KOŃCOWY

### Temat projektu

Rozpoznawanie wyrazów przy pomocy rozwiązań Cognitive Services dostarczanych przez platformę Azure - OCR i READ API.

### Cel projektu

Głównym celem projektu było sprawdzenie dwóch metod rozpoznawania znaków: OCR oraz READ API, sposobu ich użycia oraz porównania ze sobą. 

### READ API

READ API to jedna z nowszych technologii platformy Azure. Jest zoptymalizowana pod kątem wydzielania tekstu z obrazów i wielostronicowych dokumentów PDF z kilkoma językami. Wykrywa zarówno tekst pisany jak i drukowany na obrazie.

### Wymagania wejściowe READ API (co do obrazu)

-	Obsługiwane formaty plików: JPEG, PNG, BMP, PDF i TIFF.
-	W przypadku plików PDF i TIFF, są przetwarzane do 2000 stron.
-	Rozmiar pliku musi być mniejszy niż 50 MB i wymiary co najmniej 50 x 50 pikseli, a maksymalnie 10000 x 10000 pikseli.
-	Wymiary PDF muszą mieć co najwyżej 17 x 17 cali, odpowiadające rozmiarowi formatu Legal lub A3 i mniejszym.

### Wywołanie odczytu

W sposób asynchroniczny interfejs API wyodrębnia tekst z pobranego obrazu. Wywołanie zwraca w odpowiedzi pole nagłówka o nazwie Operation-Location. Wartość Operation-Location zawiera adres URL, który jest identyfikatorem operacji, która ma zostać wykonana w następnym kroku.

### Wywołanie operacji Get Results

Drugim krokiem jest wywołanie operacji Get Results. Ta operacja przyjmuje jako dane wejściowe identyfikator operacji, który został utworzony przez operację odczytu. Zwraca odpowiedź w formacie JSON, która zawiera pole stanu. Tę operację można wywołać iteracyjnie, dopóki nie zwróci wartości z wartością sukces.
Gdy wartość w polu stan zostanie zakończona pomyślnie, odpowiedź JSON zawiera wyodrębnioną zawartość tekstową z obrazu lub dokumentu. Odpowiedź JSON zachowuje pierwotną grupę wierszy rozpoznanych wyrazów. Zawiera wyodrębnione wiersze tekstu.

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

### OCR API

Interfejs API OCR jest przeznaczony do szybkiego wyodrębniania niewielkich ilości tekstu na obrazach. Działa synchronicznie w celu zapewnienia natychmiastowych wyników i umożliwia rozpoznawanie tekstu w wielu językach.

W trakcie przetwarzania obrazów, interfejs API OCR zwraca hierarchię informacji, która zawiera:
-  Regiony na obrazie zawierającym tekst
-	Wiersze tekstu w każdym regionie
-	Słowa w każdym wierszu tekstu

```
# EXTRACT THE WORD BOUNDING BOXES AND TEXT
line_infos = [region["lines"] for region in analysis["regions"]]
word_infos = []
for line in line_infos:
    for word_metadata in line:
        for word_info in word_metadata["words"]:
            word_infos.append(word_info)
```
W przypadku każdego z tych elementów interfejs API OCR zwraca również współrzędne pola ograniczenia, które definiują prostokąt wskazujący lokalizację regionu, wiersza lub słowa na obrazie.

### Przykład

```
{
   "language":"en",
   "textAngle":0.0,
   "orientation":"Up",
   "regions":[
      {
         "boundingBox":"29,78,266,286",
         "lines":[
            {
               "boundingBox":"32,78,263,25",
               "words":[
                  {
                     "boundingBox":"32,79,159,24",
                     "text":"\"Insanity:"
                  },
                  {
                     "boundingBox":"214,78,81,25",
                     "text":"doing"
                  }
               ]
            },
            {
               "boundingBox":"29,111,232,25",
               "words":[
                  {
                     "boundingBox":"29,111,49,19",
                     "text":"the"
                  },
                  {
                     "boundingBox":"98,117,63,14",
                     "text":"same"
                  },
                  {
                     "boundingBox":"180,111,81,25",
                     "text":"thing"
                  }
               ]
            },
            {
               "boundingBox":"30,145,214,19",
               "words":[
                  {
                     "boundingBox":"30,151,65,13",
                     "text":"over"
                  },
                  {
                     "boundingBox":"114,145,47,19",
                     "text":"and"
                  },
                  {
                     "boundingBox":"181,151,63,13",
                     "text":"over"
                  }
               ]
            },
            {
               "boundingBox":"30,178,148,25",
               "words":[
                  {
                     "boundingBox":"30,179,82,24",
                     "text":"again"
                  },
                  {
                     "boundingBox":"131,178,47,19",
                     "text":"and"
                  }
               ]
            },
            {
               "boundingBox":"31,212,147,24",
               "words":[
                  {
                     "boundingBox":"31,212,147,24",
                     "text":"expecting"
                  }
               ]
            },
            {
               "boundingBox":"30,245,147,19",
               "words":[
                  {
                     "boundingBox":"30,245,147,19",
                     "text":"different"
                  }
               ]
            },
            {
               "boundingBox":"31,278,145,19",
               "words":[
                  {
                     "boundingBox":"31,278,125,19",
                     "text":"results."
                  },
                  {
                     "boundingBox":"166,279,10,7",
                     "text":"\""
                  }
               ]
            },
            {
               "boundingBox":"29,345,250,19",
               "words":[
                  {
                     "boundingBox":"29,345,98,19",
                     "text":"Albert"
                  },
                  {
                     "boundingBox":"146,345,133,19",
                     "text":"Einstein"
                  }
               ]
            }
         ]
      }
   ]
}
```
#### Obraz do przetworzenia
![Albert Einstein - quotation](https://i.pinimg.com/originals/00/fb/11/00fb11f12caebcaf3707fbdbf22224c1.png)

#### Wynik przetworzenia obrazu
![Final result](https://github.com/mateo100/Cognitive-Services-App/blob/main/final.png?raw=true)

### Porównanie OCR API i READ API

-	Wadą metody OCR mogą być fałszywe wyniki, gdy obraz zostanie uznany za zdominowany przez tekst. READ API korzysta z najnowszych modeli rozpoznawania i jest zoptymalizowany pod kątem obrazów, na których znajduje się duża ilość tekstu lub chaos wizualny.
-	READ API jest lepszą opcją w przypadku zeskanowanych dokumentów, w których znajduje się duża ilość tekstu. READ API umożliwia również automatyczne określenie właściwego modelu rozpoznawania, którego należy użyć, biorąc pod uwagę wiersze tekstu i pomocnicze obrazy z drukowanym tekstem, jak również rozpoznawanie pisma ręcznego.
-	Ponieważ READ API umożliwia pracę z większymi dokumentami, działa asynchronicznie, aby nie blokować aplikacji w trakcie odczytywania zawartości i zwracania wyników do aplikacji. OCR API działa natomiast synchronicznie.
-	Interfejs API OCR służy do szybkiego wyodrębniania niewielkich ilości tekstu z obrazów. Read API to lepsza opcja w przypadku zeskanowanych dokumentów zawierających dużą ilość tekstu.


### Wnioski

Interfejs API OCR korzysta ze starszego modelu rozpoznawania, obsługuje tylko obrazy i działa synchronicznie, powracając natychmiast z wykrytym tekstem. Zaletą OCR API jest natomiast wsparcie dla większej liczby języków a także niższa cena ($1.50 na 1,000 transakcji).
Read API używa nowszego modelu rozpoznawania, przyjmuje obraz lub dokument PDF jako dane wejściowe i asynchronicznie wyodrębnia tekst. Wadą READ API jest natomiast wsparcie dla mniejszej liczby języków a także wyższa cena ($2.50 na 1,000 transakcji).






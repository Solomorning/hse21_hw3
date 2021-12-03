# Рабочий код в collab
Выравнивание: https://colab.research.google.com/drive/17sXaaJGzfEpOlzjvTLFMKn-XA8fqLWWf?usp=sharing
Код для сборки ALL.counts - ниже.
Стат. обработка в R: https://colab.research.google.com/drive/1O3NSKzfY9dDTYEphDdbueKyx1PB-z1wu?usp=sharing
# Multiqc
Проверяем качество чтений
![image](https://user-images.githubusercontent.com/93263163/144484715-252d2973-3299-4ba5-beed-b738a9d4c2ab.png)
![image](https://user-images.githubusercontent.com/93263163/144484775-c6fd0ace-a353-4ca2-84d4-73bbc56f2611.png)
![image](https://user-images.githubusercontent.com/93263163/144484825-b6d615fa-b608-45bd-be1d-9352fc548f1e.png)
![image](https://user-images.githubusercontent.com/93263163/144484877-19a359a3-1981-434e-9dfb-004e498ca8f1.png)
![image](https://user-images.githubusercontent.com/93263163/144484982-0c2c2510-4c66-4552-bcfe-40178f7cf35a.png)
![image](https://user-images.githubusercontent.com/93263163/144485090-284be93b-4fda-4523-b97c-12f17bb12138.png)
# Hisat и HtSeq
---
| Номер | ID |      Тип      | Исходные чтения | Чтения, успешно откартированные на геном | Уникально откартированные чтения | Чтения, попавшие на гены |
|:-----:|:----------:|:---------------------:|------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------|---------------------------------------------|
|     1 | SRR3414629 | перепрограммированние |          21106089          |                                   20510113 (97.18%)                                   |                18375888 (87.06%)               |                  16049609                 |
|     2 | SRR3414630 | перепрограммированние |          15244711          |                                   14832680 (97.3%)                                    |                13186139 (86.5%)               |                  11465324                 |
|     3 | SRR3414631 | перепрограммированние |          24244069          |                                   24244069 (97.13%)                                   |                20928945 (86.33%)               |                  18408851                 |
|     4 | SRR3414635 |        контроль       |          20956475          |                                   20395865 (97.32%)                                   |                18428317 (87.94%)               |                  16275997                 |
|     5 | SRR3414636 |        контроль       |          20307147          |                                   19757059 (97.29%)                                   |                17825380 (87.78%)               |                  15757580                 |
|     6 | SRR3414637 |        контроль       |          20385570          |                                   19847291 (97.36 )                                   |                17844858 (87.54%)               |                  15736978                 |

# Сборка ALL.counts и ALL.info
ALL.counts собираются при помощи Python из всех .counts файлов.
>files=["SRR3414635.counts","SRR3414636.counts","SRR3414637.counts","SRR3414629.counts","SRR3414630.counts","SRR3414631.counts"] <br>
>AllDict= {}  <br>
>for i in files:  <br>
>    file = open(i, 'r')  <br>
>    for line in file: <br>
>        x = line.find('\t')  <br>
>        if line[:x] not in AllDict.keys(): <br>
>            AllDict[line[:x]] = [] <br>
>        AllDict[line[:x]].append(int(line[x + 1:])) <br>
>    file.close() <br>
>file = open("ALL.counts", 'w') <br>
>file.write('c1,c2,c3,r1,r2,r3\n') <br>
>for i in AllDict.keys(): <br>
>    file.write(i) <br>
>    for j in AllDict[i]: <br>
>        file.write(','+str(j)) <br>
>    file.write('\n') <br>


ALL.info собираем вручную. Затем подгружаем к collab со статистикой. Получаем следующие фреймы:
![image](https://user-images.githubusercontent.com/93263163/144654006-7f2d5c0b-da38-47de-a06f-a48af006245a.png)
![image](https://user-images.githubusercontent.com/93263163/144654033-15d8e459-37ba-4909-a200-6c08dfb17ae2.png)
# DESeq2
## Тепловая карта
![image](https://user-images.githubusercontent.com/93263163/144654111-bed0fded-e7a3-4b67-985a-1240604b2020.png)
## MA-plot
![image](https://user-images.githubusercontent.com/93263163/144654140-43d82546-146f-4b6a-a265-3e45831019b6.png)
## Тепловая карта для генов
![image](https://user-images.githubusercontent.com/93263163/144654868-28897f98-2025-42be-ad84-e733893df85d.png)

## Гены, наиболее значимо поменявшие свою экспрессию
![image](https://user-images.githubusercontent.com/93263163/144666987-ca854785-e0cd-49d7-b2ff-503b85b6a795.png)
![image](https://user-images.githubusercontent.com/93263163/144667019-6aafbec2-9d2f-4898-a96b-4cb542e5d815.png)
![image](https://user-images.githubusercontent.com/93263163/144667035-d82185e2-c09b-45a7-a0c0-ca48767f6fce.png)
![image](https://user-images.githubusercontent.com/93263163/144667058-a0d2e074-53ab-40c6-a5ff-9d59c7494d5d.png)
![image](https://user-images.githubusercontent.com/93263163/144667091-704f6dbd-4ed0-435d-b8d4-77e9e9891438.png)
![image](https://user-images.githubusercontent.com/93263163/144667149-2b3d8f90-6f3b-4086-9011-5fc8d3c9be68.png)







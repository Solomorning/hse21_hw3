# Описание
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
# Сборка ALL.counts и ALL.info
ALL.counts собираются при помощи Python из всех .counts файлов.
>files = ["SRR3414635.counts","SRR3414636.counts","SRR3414637.counts","SRR3414629.counts","SRR3414630.counts","SRR3414631.counts"]
>AllDict= {}
>for i in files:
>    file = open(i, 'r')
>    for line in file:
>        x = line.find('\t')
>        if line[:x] not in AllDict.keys():
>            AllDict[line[:x]] = []
>        AllDict[line[:x]].append(int(line[x + 1:]))
>    file.close()
>file = open("ALL.counts", 'w')
>file.write('c1,c2,c3,r1,r2,r3\n')
>for i in AllDict.keys():
>    file.write(i)
>    for j in AllDict[i]:
>        file.write(','+str(j))
>    file.write('\n')


ALL.info собираем вручную. Затем подгружаем к collab со статистикой. Получаем следующие фреймы:
![image](https://user-images.githubusercontent.com/93263163/144654006-7f2d5c0b-da38-47de-a06f-a48af006245a.png)
![image](https://user-images.githubusercontent.com/93263163/144654033-15d8e459-37ba-4909-a200-6c08dfb17ae2.png)
# DESeq2
![image](https://user-images.githubusercontent.com/93263163/144654111-bed0fded-e7a3-4b67-985a-1240604b2020.png)
![image](https://user-images.githubusercontent.com/93263163/144654140-43d82546-146f-4b6a-a265-3e45831019b6.png)
![image](https://user-images.githubusercontent.com/93263163/144654868-28897f98-2025-42be-ad84-e733893df85d.png)
Выберем какие-то произвольные гены, чтобы проиллюстрировать изменения:
![image](https://user-images.githubusercontent.com/93263163/144655168-e19b6acd-4632-417e-b5f0-cb0ce915d4e2.png)
![image](https://user-images.githubusercontent.com/93263163/144655191-30bab771-b108-4a3d-9403-76fb0c19dd4a.png)
![image](https://user-images.githubusercontent.com/93263163/144655216-a98dba3f-e19a-4753-8083-672b45a9381a.png)
![image](https://user-images.githubusercontent.com/93263163/144655313-786085a6-cc07-48bd-bfd0-59a4e2361347.png)
![image](https://user-images.githubusercontent.com/93263163/144655429-45a6cea1-1395-4c65-a6fa-02e6c9c010c3.png)
![image](https://user-images.githubusercontent.com/93263163/144655370-ec5b6580-ea06-4543-8528-72f31e4a65a3.png)






# Hand detector game

### Сервер на стороне python
###### Распознавание объектов

Для распознавания объектов с камеры использована библиотека [**mediapipe**](https://mediapipe.dev/)
![Распознавание рук](https://mediapipe.dev/images/mobile/hand_crops.png)

Данная библиотека может распознавать и выстраивать 3D координаты точек на лицах, техал и так далее. Очень мощная штука.
В результате её работы на каждом кадре мы получаем 21 3D-координату одной руки. Данная библиотека открывает большое количество возможностей.

![Координаты](https://mediapipe.dev/images/mobile/hand_landmarks.png)

Установка происходит в 1 строчку:
```sh
pip install mediapipe
```

```python
from rich.console import Console

console = Console()
```

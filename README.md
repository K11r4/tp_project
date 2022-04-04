## Описание

2D игра. Задача игрока пройти из начальной точки в конечную, избегая врагов и ловушек.

Параметры запуска:

    pip3 install -r requirements.txt
    python3 main.py

## Структура

### charcacters/
#### player.py
class Player(Body) - реализация игрока

#### enemy.py
class Enemy (to do) - реализация врага

### scenes/
#### scene.py 
class Scene - от этого класса наследуются сцены, которые отвечают за основную логику игры, создание и удаление игровых объектов и  обновление их сосояний (игрок, враги, коллайдер, камера)

#### gameLevel.py
class GameLevel - пока единственная рабочая сцена, которая будет отвечать за организацию игрового уровня

### src/
когда нибудь здесь будут ресурсы

#### main.py
class Game - насторойка окружения: загрузка ресурсов(to do), инициализация сцен, переходы между сценами, создание экрана, запуск игрового цикла

#### screen.py
class Screen - обертка над pygame.display, отвечает за отрисовку графики

#### camera.py
class Camera - расчитывает область отрисовки для класса Screen, основываясь на местоположении игрока

#### collider.py
class Colider - расчитывает столкновения объектов

#### controller.py
class Controller - реализация паттерна Observer, которая отслеживает в главном цикле игровые события

#### directionController.py
class DirController - реализация Listener для controller, расчитывает направление движения игрока основываясь на нажатых клавишах, не выглядит очень нужным

#### map.py
class Map - парсит файл карты (после вызова конструктора от сырых данных в полях класса будут лежать, например препятсвия в формате удобном коллайдеру, собранная из спрайтов картинка карты (to do))

#### body.py
class Body - отвечает за "интересные" объекты, от него наследуется игрок, враги

#### vector.py
class Vector - отвечает за удобное взаимодейтвие с движениями объектов


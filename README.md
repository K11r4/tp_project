## Описание

2D игра. Задача игрока пройти из начальной точки в конечную, избегая врагов и ловушек.

#### Параметры запуска:

    pip3 install -r requirements.txt
    python3 main.py

#### Управление:
WASD (или стрелочки) + Пробел

#### Ссылка на uml:
https://drive.google.com/file/d/15rN_GVxVCQgZfPTg3NaLd1gvZnkJ-Q__/view?usp=sharing



## Структура
### ai/
классы регулирующие поведение персонажей
#### weakai.py
class WeakAI - очень примитивный бот для противников

### charcacters/
#### player.py
class Player(Body) - реализация игрока

#### enemy.py
class Enemy (to do) - реализация врага

### scenes/
#### scene.py 
class Scene - от этого класса наследуются сцены, которые отвечают за основную логику игры, создание и удаление игровых объектов и  обновление их сосояний (игрок, враги, коллайдер, камера)

#### gameLevel.py
class GameLevel(Scene) - пока единственная рабочая сцена, которая будет отвечать за организацию игрового уровня

#### startScreen.py
class StartScreen(Scene) - слабо анимированная заставка

#### gameEnd.py
class GameEnd(Scene) - завершающие титры

#### gameOver.py
class GameOver(Scene) - экран смерти

### src/
Ресурсы, графика и конфигурация карты, создана с помощью Tiled Map Editor

### controllers/
Классы упрощающие взаимодействие с пользователем

#### directionController.py
class DirController - реализация Listener для controller, расчитывает направление движения игрока основываясь на нажатых клавишах, не выглядит очень нужным

#### keyController.py
class KeyContoller - хранит map с нажатыми клавишами

#### clickController.py 
class ClickController - захватывает нажатие любой клавиши, удобен для использования на не игровых сценах

### objects/
Внутренние объекты, служащие для взаимодействия между персонажами

#### weapon.py
class Weapon(Body) - область коллизии для оружия игрока

#### exitpoint.py
class ExitPoint(Body) - область коллизии для точки выхода с уровня

#### healthsphere.py
class HealthSphere(Body) - предмет увеличивающий здоровье игрока

### interface/

#### healthbar.py
class HealthBar(Body) - отвечает за отображение здоровья игрока

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

#### map.py
class Map - парсит файл карты (после вызова конструктора от сырых данных в полях класса будут лежать, например препятсвия в формате удобном коллайдеру, собранная из спрайтов картинка карты (to do))

#### body.py
class Body - отвечает за "интересные" объекты, от него наследуется игрок, враги

#### vector.py
class Vector - отвечает за удобное взаимодейтвие с движениями объектов

#### spritesheet.py
class SpriteSheet - позволяет генерировать спрайты и анимации на основе графического файла

#### sprite.py
class Sprite - не очень функциональный класс, но позволяет упростить работу с графикой

#### animation.py
class Animation(Sprite) - несколько спрайтов с которым можно взаимодействоать ка с одним

# 10.014_PokerTripleTriad

## [1. Requirement](https://docs.google.com/document/d/14Yq8YuP0RxB080rZlBmDTTOS-8_ds3UmV0gc3L_Sv4s/edit)
- Written entirely in Python
- Text-based user interface (achieved using `print()` function or using `turtle` and `matplotlib` library)
- Only standard libraries (no `pip install`)

## 2. Game Description
- Based on the **Final Fantasy's game of Triple Triads.**
- **Main objective:** win as many cards as possible on a nxn grid.
- **Basic Logic:** 
    - Each player is given `N` poker-cards with 4 values randomly placed on each edge as shown:<br>
    ![](https://i.imgur.com/UDhXXCx.png)

        where aside from value from `1` to `9`, we represent *Face Card's* values and number 10 as `A` for Ace, `K` for King, `Q` for Queen, `J` for Jack, `T` for 10. This is to simplify the display formatting.
    - Player will take turn to place their cards on a `nxn` (2N > n^2) grid. We use 3x3 grid as example below: 
    ![](https://i.imgur.com/AGvWhgE.png)
    - When a card is placed next to another card, the adjacent values will be used to compare which card is *superior*. The *superior* card will win over the *inferior* card. Whoever owns most card at the end of the game (when the board is filled) will be the winner
    - e.g:
        - A `winning choice` for card at cell 8 as `Q` (current card) > `T` (right neighbor)
        ![](https://i.imgur.com/MVRsG82.png)
        - A `losing choice` for card at cell 5 (middle):
        `J` (current card) < `A` (top neighbor) by 3 points **&&** 
        `4` (current card) < `K` (bottom neighbor) by 9 points **&&**
        `J` (currnet card) > `8` (left neighbor) by 3 points
        so overall there is a net loss of 9 points<br>
        ![](https://i.imgur.com/XwaAhdA.png)
        - If a move doens't result in winning or losing a card, it is deemed a `normal choice`.
    - Currently, this is a one player game (vs a non-player character `NPC`) with 3 difficulties:
        - `EASY`: values are generated from `7` to `A`
        - `MEDIUM`: values are generated from `4` to `11`
        - `HARD`: values are generated from `2` to `9`
        you can choose your difficulty level while `NPC`'s card is capped at `MEDIUM` level
        
## 3. How to Play
- Clone this repository and open jupyter notebook to try out the game.
- Input your name and choose your difficulties:
![](https://i.imgur.com/NTXQl9s.png)
- Random cards will be distributed to your hand:<br>
![](https://i.imgur.com/RY5uJY3.png)
- The `coin_toss` function will randomly determines who play first (equal probability).
- When it is your turn, you can pick one card from your hand and then choose a position on the board to place:
![](https://i.imgur.com/KMFdYbM.png)
- After placing your card, the display of the board will be printed on the screen:<br>
![](https://i.imgur.com/ybMQYzc.png)
- Our logic will then evaluate whether your move is `winning`, `losing` or `normal` to change the card owner after every move:<br>
![](https://i.imgur.com/MsPfSgN.png)
- `NPC` will randomly place card during his turn.
- Continue to play until the whole board is filled. 

## 4. Strengths:
- `content` and `logic` are stored in different folders so different teammates can work separately easily.
- all functions are kept as modularized as possible.
- hardcode are minimized so our game can be easily scaled up to bigger board, more cards or more players.



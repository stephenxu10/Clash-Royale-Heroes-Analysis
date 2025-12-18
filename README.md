# Overview

Clash Royale is a mobile strategy game enjoyed by millions of players around the world, including myself. In December 2025, Clash Royale released an update featuring a brand-new gameplay feature: heroic cards. While heroes have introduced exciting and unique mechanics into the game, unlocking them has proven to be a laborious task. 

Players unlock heroes by collecting 200 hero fragments, which automatically summons a heroic card. The trouble is, summoning a hero does not necessarily guarantee a *new* card. Rather, players run the risk of summoning a duplicate hero, which they are meagerly compensated for. Heroes are quite strong in Clash Royale, so players want to obtain as many unique heroes as possible. Therefore, many Clash Royale players are extremely frustrated by this process, calling it yet another cash grab by Supercell. Although I personally resonate with these sentiments, this at least opens the door to some **very** interesting mathematics. 

In this repository, we will answer the following questions:
- How likely is it to obtain $k$ unique heroes after $m$ hero summons, given there are $n$ heroes currently in the game?
- How are these probabilities distributed as $k$ goes from $1$ to $\min(m, n)$?
- Is the hero unlock system really that bad?

I assume:
- Hero summons are independent of all previous summons and give equal probability of obtaining any hero in the game, regardless of which ones are currently unlocked.

We will back our findings with combinatorics and programming. Math and Clash enthusiasts should check out the PDF file in this repo, where I explain the theory and answer the questions outlined above. Enjoy!

# Usage
I've provided an executable ```./clash``` that performs the probability distribution generating. To toy around with this yourself, first clone the repo:
```bash
git clone https://github.com/stephenxu10/Clash-Royale-Heroes-Analysis
```
Install the required dependencies:
```bash
pip install matplotlib mplcursors
```
Now you are ready to explore the probability distributions for yourself. Use the following command structure:
```bash
./clash -n <heroes> -s <summons> [-l]
```
This will generate a matplotlib plot of the uniqueness distribution.

**Required Arguments:**
- `-n <heroes>`: The number of heroes currently in the game. As of 12/18/25, there are four heroes in the game among 121 total cards.
- `-s <summons>`: The number of hero summons you perform. This number can be arbitrarily large, but keep in mind most free-to-play players can only do this once per month.

**Optional Argument(s):**
- `-l`: Toggle for using a logarithmic scale.

If you encounter a permission error when running ```./clash```, fix the permissions by executing:
```bash
chmod a+x ./clash
```
Example:
```bash
./clash -n 4 -s 20 -l

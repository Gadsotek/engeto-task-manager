# Testovací případy pro program Správce úkolů

## 1. Testovací případy pro funkci `main_menu`

### Test 1.1: Validní výběr možnosti
* **Název testovacího případu**: Validní výběr z hlavního menu
* **Popis**: Ověření, že volba čísla 1-4 v hlavním menu vrátí správnou hodnotu
* **Vstupní podmínky**: Program zobrazuje hlavní menu
* **Kroky testu**: 
  1. Spusťte program
  2. Zadejte číslo 1
* **Očekávaný výsledek**: Funkce main_menu vrátí hodnotu 1
* **Skutečný výsledek**: Funkce vrátila hodnotu 1 a spustila funkci add_task()
* **Stav**: Pass
* **Poznámky**: Základní test funkčnosti hlavního menu

### Test 1.2: Nevalidní číselný vstup
* **Název testovacího případu**: Nevalidní číselný vstup v hlavním menu
* **Popis**: Ověření, že program správně odmítne číslo mimo rozsah 1-4
* **Vstupní podmínky**: Program zobrazuje hlavní menu
* **Kroky testu**: 
  1. Spusťte program
  2. Zadejte číslo 5
  3. Po chybové hlášce zadejte číslo 1
* **Očekávaný výsledek**: Program zobrazí chybovou hlášku a požádá o nový vstup
* **Skutečný výsledek**: Program zobrazil "Please select option 1 to 4." a požádal o nový vstup
* **Stav**: Pass
* **Poznámky**: Ověřuje ošetření chybného vstupu mimo platný rozsah

### Test 1.3: Nečíselný vstup
* **Název testovacího případu**: Nečíselný vstup v hlavním menu
* **Popis**: Ověření, že program správně odmítne nečíselný vstup
* **Vstupní podmínky**: Program zobrazuje hlavní menu
* **Kroky testu**: 
  1. Spusťte program
  2. Zadejte písmeno "a"
  3. Po chybové hlášce zadejte číslo 1
* **Očekávaný výsledek**: Program zobrazí chybovou hlášku a požádá o nový vstup
* **Skutečný výsledek**: Program zobrazil "Please select option 1 to 4." a požádal o nový vstup
* **Stav**: Pass
* **Poznámky**: Ověřuje ošetření vstupu, který není číslem

### Test 1.4: Prázdný vstup
* **Název testovacího případu**: Prázdný vstup v hlavním menu
* **Popis**: Ověření, že program správně odmítne prázdný vstup (pouze stisk Enter)
* **Vstupní podmínky**: Program zobrazuje hlavní menu
* **Kroky testu**: 
  1. Spusťte program
  2. Stiskněte pouze klávesu Enter bez zadání vstupu
  3. Po chybové hlášce zadejte číslo 1
* **Očekávaný výsledek**: Program zobrazí chybovou hlášku a požádá o nový vstup
* **Skutečný výsledek**: Program zobrazil "Please select option 1 to 4." a požádal o nový vstup
* **Stav**: Pass
* **Poznámky**: Ověřuje ošetření prázdného vstupu

## 2. Testovací případy pro funkci `add_task`

### Test 2.1: Přidání úkolu s validními vstupy
* **Název testovacího případu**: Přidání úkolu s validním názvem a popisem
* **Popis**: Ověření, že úkol s platným názvem a popisem je správně přidán do seznamu
* **Vstupní podmínky**: Seznam úkolů je prázdný
* **Kroky testu**: 
  1. Zvolte možnost 1 v hlavním menu
  2. Zadejte název "Nakoupit potraviny"
  3. Zadejte popis "Mléko, chléb, máslo"
* **Očekávaný výsledek**: Program přidá úkol do seznamu a zobrazí potvrzující zprávu
* **Skutečný výsledek**: Program přidal úkol do seznamu a zobrazil "Task 'Nakoupit potraviny' added."
* **Stav**: Pass
* **Poznámky**: Základní test pro přidání úkolu

### Test 2.2: Přidání úkolu s prázdným názvem
* **Název testovacího případu**: Pokus o přidání úkolu s prázdným názvem
* **Popis**: Ověření, že program nepřidá úkol s prázdným názvem
* **Vstupní podmínky**: Seznam úkolů obsahuje jeden úkol
* **Kroky testu**: 
  1. Zvolte možnost 1 v hlavním menu
  2. Stiskněte pouze Enter bez zadání názvu
* **Očekávaný výsledek**: Program zobrazí chybovou hlášku a nepřidá úkol do seznamu
* **Skutečný výsledek**: Program zobrazil "Title cannot be empty." a vrátil se do hlavního menu
* **Stav**: Pass
* **Poznámky**: Ověřuje ošetření neplatného prázdného názvu

### Test 2.3: Přidání úkolu s prázdným popisem
* **Název testovacího případu**: Přidání úkolu s prázdným popisem
* **Popis**: Ověření, že úkol je úspěšně přidán i s prázdným popisem
* **Vstupní podmínky**: Seznam úkolů obsahuje jeden úkol
* **Kroky testu**: 
  1. Zvolte možnost 1 v hlavním menu
  2. Zadejte název "Zaplatit účty"
  3. Stiskněte pouze Enter bez zadání popisu
* **Očekávaný výsledek**: Program přidá úkol do seznamu s prázdným popisem
* **Skutečný výsledek**: Program přidal úkol do seznamu a zobrazil "Task 'Zaplatit účty' added."
* **Stav**: Pass
* **Poznámky**: Ověřuje správné přidání úkolu i s prázdným popisem

### Test 2.4: Přidání prvního úkolu (hraniční případ)
* **Název testovacího případu**: Přidání prvního úkolu do prázdného seznamu
* **Popis**: Ověření, že první úkol je správně přidán do prázdného seznamu
* **Vstupní podmínky**: Seznam úkolů je prázdný
* **Kroky testu**: 
  1. Zvolte možnost 1 v hlavním menu
  2. Zadejte název "První úkol"
  3. Zadejte popis "Popis prvního úkolu"
* **Očekávaný výsledek**: Program přidá úkol do prázdného seznamu
* **Skutečný výsledek**: Program přidal úkol do seznamu a zobrazil "Task 'První úkol' added."
* **Stav**: Pass
* **Poznámky**: Ověřuje správné fungování při přidání prvního úkolu (prázdný seznam → seznam s jedním prvkem)

## 3. Testovací případy pro funkci `show_tasks`

### Test 3.1: Zobrazení seznamu s úkoly
* **Název testovacího případu**: Zobrazení neprázdného seznamu úkolů
* **Popis**: Ověření, že seznam úkolů je správně zobrazen včetně všech detailů
* **Vstupní podmínky**: Seznam obsahuje alespoň dva úkoly
* **Kroky testu**: 
  1. Zvolte možnost 2 v hlavním menu
* **Očekávaný výsledek**: Program zobrazí seznam úkolů s názvy a popisy
* **Skutečný výsledek**: Program zobrazil seznam úkolů, každý s číslem, názvem a popisem
* **Stav**: Pass
* **Poznámky**: Základní test pro zobrazení úkolů

### Test 3.2: Zobrazení prázdného seznamu úkolů (hraniční případ)
* **Název testovacího případu**: Zobrazení prázdného seznamu úkolů
* **Popis**: Ověření správného chování při zobrazení prázdného seznamu
* **Vstupní podmínky**: Seznam úkolů je prázdný
* **Kroky testu**: 
  1. Zvolte možnost 2 v hlavním menu
* **Očekávaný výsledek**: Program zobrazí zprávu o prázdném seznamu
* **Skutečný výsledek**: Program zobrazil "There are no tasks yet, please add some."
* **Stav**: Pass
* **Poznámky**: Ověřuje správné chování při prázdném seznamu

### Test 3.3: Zobrazení seznamu s úkoly bez popisů
* **Název testovacího případu**: Zobrazení úkolů s prázdnými popisy
* **Popis**: Ověření, že úkoly bez popisů jsou správně zobrazeny
* **Vstupní podmínky**: Seznam obsahuje alespoň jeden úkol bez popisu
* **Kroky testu**: 
  1. Přidejte úkol s prázdným popisem
  2. Zvolte možnost 2 v hlavním menu
* **Očekávaný výsledek**: Program zobrazí úkol s označením prázdného popisu
* **Skutečný výsledek**: Program zobrazil úkol s textem "Description: (no description))" u prázdného popisu
* **Stav**: Pass
* **Poznámky**: Ověřuje správné zobrazení úkolů bez popisů

## 4. Testovací případy pro funkci `remove_task`

### Test 4.1: Odstranění úkolu s validním indexem
* **Název testovacího případu**: Odstranění úkolu s platným indexem
* **Popis**: Ověření, že úkol je správně odstraněn ze seznamu
* **Vstupní podmínky**: Seznam obsahuje alespoň dva úkoly
* **Kroky testu**: 
  1. Zvolte možnost 3 v hlavním menu
  2. Zadejte číslo 1 (index prvního úkolu)
* **Očekávaný výsledek**: Program odstraní první úkol a zobrazí potvrzující zprávu
* **Skutečný výsledek**: Program odstranil první úkol a zobrazil zprávu o odstranění
* **Stav**: Pass
* **Poznámky**: Základní test pro odstranění úkolu

### Test 4.2: Pokus o odstranění úkolu s nevalidním indexem
* **Název testovacího případu**: Odstranění úkolu s neplatným indexem
* **Popis**: Ověření, že program správně ošetří zadání indexu mimo rozsah
* **Vstupní podmínky**: Seznam obsahuje dva úkoly
* **Kroky testu**: 
  1. Zvolte možnost 3 v hlavním menu
  2. Zadejte číslo 3 (mimo rozsah)
  3. Po chybové hlášce zadejte číslo 1
* **Očekávaný výsledek**: Program zobrazí chybovou hlášku a požádá o nový vstup
* **Skutečný výsledek**: Program zobrazil "Please enter unmber between x and y.", kde x = 1 jako první index a y = pocet a požádal o nový vstup
* **Stav**: Pass
* **Poznámky**: Ověřuje ošetření indexu mimo rozsah

### Test 4.3: Pokus o odstranění úkolu s nečíselným indexem
* **Název testovacího případu**: Odstranění úkolu s nečíselným indexem
* **Popis**: Ověření, že program správně ošetří zadání nečíselného indexu
* **Vstupní podmínky**: Seznam obsahuje alespoň jeden úkol
* **Kroky testu**: 
  1. Zvolte možnost 3 v hlavním menu
  2. Zadejte písmeno "a"
  3. Po chybové hlášce zadejte číslo 1
* **Očekávaný výsledek**: Program zobrazí chybovou hlášku a požádá o nový vstup
* **Skutečný výsledek**: Program zobrazil "Please enter unmber between x and y.", kde x = 1 jako první index a y = pocet ukolů a požádal o nový vstup
* **Stav**: Pass
* **Poznámky**: Ověřuje ošetření nečíselného vstupu

### Test 4.4: Pokus o odstranění úkolu z prázdného seznamu (hraniční případ)
* **Název testovacího případu**: Odstranění úkolu z prázdného seznamu
* **Popis**: Ověření správného chování při pokusu o odstranění z prázdného seznamu
* **Vstupní podmínky**: Seznam úkolů je prázdný
* **Kroky testu**: 
  1. Zvolte možnost 3 v hlavním menu
* **Očekávaný výsledek**: Program zobrazí zprávu o prázdném seznamu
* **Skutečný výsledek**: Program zobrazil "There are no tasks yet, please add some."
* **Stav**: Pass
* **Poznámky**: Ověřuje správné chování při prázdném seznamu

### Test 4.5: Odstranění posledního úkolu (hraniční případ)
* **Název testovacího případu**: Odstranění posledního úkolu ze seznamu
* **Popis**: Ověření, že po odstranění posledního úkolu je seznam správně označen jako prázdný
* **Vstupní podmínky**: Seznam obsahuje pouze jeden úkol
* **Kroky testu**: 
  1. Zvolte možnost 3 v hlavním menu
  2. Zadejte číslo 1
  3. Zvolte možnost 2 pro zobrazení seznamu
* **Očekávaný výsledek**: Program odstraní poslední úkol a při zobrazení informuje, že seznam je prázdný
* **Skutečný výsledek**: Program odstranil poslední úkol a při zobrazení informoval, že seznam je prázdný
* **Stav**: Pass
* **Poznámky**: Ověřuje správný přechod ze seznamu s jedním prvkem do prázdného seznamu

## 5. Testovací případy pro funkci `shutdown`

### Test 5.1: Ukončení programu
* **Název testovacího případu**: Správné ukončení programu
* **Popis**: Ověření, že program se správně ukončí po zvolení možnosti 4
* **Vstupní podmínky**: Program běží
* **Kroky testu**: 
  1. Zvolte možnost 4 v hlavním menu
* **Očekávaný výsledek**: Program zobrazí rozloučení a ukončí se
* **Skutečný výsledek**: Program zobrazil "Shutting down..." a ukončil se
* **Stav**: Pass
* **Poznámky**: Ověřuje správné ukončení programu
# Lilian, passionné de sciences : un deck custom EDH

Idée pour un deck commander avec des cartes custom, basé sur l'idée d'avoir des créatures légendaires représentant des grands informaticiens, mathématiciens et physiciens, et des enchantements et artefacts représentant leurs créations (eg. théorème = enchantement, objet = artefact).
Pour chaque famille, un "grand nom" amusant sera un planeswalker.

## Mécaniques

### Deck legends matter

Les légendaires sont au coeur du deck. Le deck est en couleurs Bant : W,U,G, avec trois sous-factions équi-réparties :

- **Physique** : couleurs W + U (Azorius), lien avec les éphémères/rituels ?
- **Informatique** : couleurs U + G (Simic), lien avec les artefacts et aussi jetons de créatures ?
- **Mathématiques** : couleurs G + W (Selesnya), lien avec les enchantements et les jetons de créatures ?

### Découvrir un théorème / inventer un objet important

2*3 créatures légendaires auront une capacité permettant d'aller tutoriser la carte associée, comme capacité activée coûtant {3} (comme les Compagnons).

### Tribu humains ?

Toutes les créatures sont des humains. Les chercheurs sans discipline sont des "chercheur", les physiciens, mathématiciens et informaticiens ont leur propre type.
Il y a des jetons Fractales 0/0.

-----

## Liste de cartes dans le deck

- 1 Commandant
- 3 Planeswalkers
- 34 créatures
- 27 enchantements + artefacts + instant/sorcery
  - 10 enchantements
  - 10 artifacts
  - 3 instants
  - 4 sorcery
- 35 terrains

Total : 1 + 3 + 34 + 35 + 10 + 10 + 3 + 4 = 100


-----

## Liste de cartes à concevoir (avec https://CardConjurer.vercel.app/)

### Commandant unique

- *Lilian, Passionné de Sciences* : {W}{U}{G}
  > Il agit comme [Captain Sisay](https://scryfall.com/card/inv/237/captain-sisay) il va tuto une légendaire et la met en main.
  > 1/3, Histoire des sciences -- {T} : Cherchez dans votre bibliothèque une carte légendaire, révélez cette carte et mettez-la dans votre main. Mélangez ensuite votre bibliothèque.
  > Avec ma photo Link, et en Mythique. FIXME:

-----

### 3 Planeswalkers

Idée : ils ont tous le *Partner*, et le *Can be your commander* ?
Si j'ai assez de place dessus...

- *Isaac Newton et la gravité* : {3}{W}{U}
  > Loyauté à 5, son +2 génère deux jeton Food (pour la pomme), et son -1 empêche les créatures non volantes d'attaquer une fois, et son ultimate à -8 donne un emblème qui donne le vol à toutes ses créatures et empêche les créatures adverses sans vol d'attaquer, Mythique.

- *Benoît Mandelbrot et ses fractales* : {U}{G}
  > Loyauté à 4, son +2 "itère le dessin" des fractale en leur donnant toutes +1/+1, son -X invoque une fractale légendaire à nommer comme on veut, de type Fractale, 0/0 avec X marqueurs +1/+1, pas d'ultimate, Mythique.

- *Alan Turing et ses machines* : {2}{W}{G}
  > Loyauté à 3, Son +1 donne un marqueur +1/+1 à un permanent ciblé que tu contrôles, qui devient une créature-artefact ce tour ci, son -1 génère une "Machine de Turing" 0/0 comme une construct d'Urza, son ultimate à -6 donne un emblème à la Gideon, qui empêche de perdre tant qu'on contrôle une "Machine de Turing" (ou un artéfact ?), Mythique.

-----

### 6 Créatures légendaires avec cartes associées (théorème ou invention)

> 2 par famille

> Ils ont tous la capacité activée suivante :
> **Major Discovery** -- {3} : search your library for a card named XXX, reveal that card, put it in your hand, then shuffle.

#### Physiciens (avec cartes associées) : en W + U (Azorius)

- *Albert Einstein, relativiste*, {2}{W}{U}, 2/4 double initiative, célérité (=> théorème *Théorie de la Relativité*), Rare.
- *Marie Curie, doublement Nobélisée*, {4}{W}{U}, 4/6 contact mortel, lien de vie, intimidate (This creature can't be blocked except by artifact creatures and/or creatures that share a color with it.) (=> artefacts *La Radioactivité*, et *Radium et Polonium*), Rare.

#### Informaticiens (avec cartes associées) : en G + W (Selesnya)

- *Edsger Dijkstra, algorithmicien* {W}{G}, 2/1 imbloquable (=> théorème *Algorithme de Dijkstra*), Rare.
- *Donald Knuth, auteur de TeX* {2}{W}{G}, 6/3 flash (=> artefact *Compilateur LaTeX* réduit de {1} le coût des non-créatures, leur donne instant speed, et donne un trésor dès qu'on lance pas pendant son tour), Rare.

#### Mathématiciens (avec cartes associées) : en U + G (Simic)

- *Euclide*, {G}{U}, 2/2, *Triangle Master* -- Sacrifice CARDNAME: counter target non-artifact spell (=> artefact *Principes d'Euclide*), Rare.
- *Léonard Euler*, {2}{G}{U}, 4/5, *Master of formulas* -- As CARDNAME enters the battlefield, note your life total.  At the beginning of your upkeep, draw a card if your life total is greater than or equal to the last noted life total for CARDNAME. Then note your life total.  Whenever you cast a spell, you gain 1 life. (=> théorème *Théorème d'Euler*), Rare.

### 16 Créatures légendaires sans carte associée

> 4/5/6 par catégorie

#### Physiciens (sans carte associée) : en W + U (Azorius)

<!-- - *Archimède* (mécanique) frame rétro, il invoque un hibou créature-artefact ? (blague avec le film Merlin l'enchanteur) -->
- *Aristote, le Levier*, {2}{W}, 2/4, Defender, *Find me a Lever!* -- {T}: tap target creature. Unco. (mécanique) frame rétro, il fait levier c'est un mur et il peut engager une créature adverse en s'engageant.
- *Max Planck*, {1}{U}, 1/3, *Energy Quanta* -- {T}: exchange target creature's power with its toughness until end of turn (physique quantique), Unco.
- *Erwin Schrödinger*, {2}{W}{U}, 3/5, *Is the cat alive?* -- {T}: target permanent you control phases out (physique quantique), Unco.
- *Stephen Hawking*, {5}{W}{U}, 8/8, Defender, *Black hole* -- {T}: destroy target creature (physique des trous noirs), Unco.
- *Sheldon Cooper*, {2}{W}{U}, 3/3, *Bazinga!* -- {T}: deal one damage to any target. *That's my spot!* -- {T}: untap target land, gain control of it until end of turn. Unco. (The Big Bang Theory, physique quantique)

#### Informaticiens (sans carte associée) : en G + W (Selesnya)

- *Stephen Cook*, {5}{W}{G}, 8/6 trample. *NP completeness* -- At the beginning of your upkeep, you may return target card from your graveyard to your hand (problèmes NP complets), Unco.
- *Marvin Minsky et John McCarthy*, {1}{W}{W}, 5/3, *Artificial intelligence* -- {T},{X}: Up to one target non-creature artifact with mana value X or less becomes an artifact creature with power and toughness each equal to its mana value. (intelligence artificielle), Unco.
- *Yoshua Bengio et Yann LeCun*, {1}{G}{G} 4/3, trample, *Neural networks* -- creatures and non-basic lands your opponents control enter the battlefield tapped. (réseaux de Neurones), Unco.
- *Tim Berners-Lee, grand navigateur*, {2}{W}{G}, 4/5, Reach, *Web browser* -- {T},{X}: destroy target creature with flying with mana value X or less. (WWW, navigateur web), Rare.
- *Rivest, Shamir et Adleman*, {W}{G}, 2/2, *Cryptography* -- Activated abilities of artifacts can't be activated. (cryptographie à clef publique et RSA), Rare.

- TODO: *Ada Lovelace, première programmeuse*, {3}{W/G}{W/G}

#### Mathématiciens (sans carte associée) : en U + G (Simic)

- *Pythagore*, {G}{U}, 1/3, *Pythagorean Theorem* -- {T}: let X and Y be target creature's power and toughness. Until end of turn, its power and toughness become Z, where Z is the square root of X^2 + Y^2, rounded up. Frame rétro, (géométrie) Unco.
- *Pascal, probabiliste avant l'heure*, {3}{G}{U} 3/3 *Introduction to probability* -- At the beginning of combat on your turn, flip a coin until you lose a flip. Whenever a player wins a coin flip, double CARDNAME's power and toughness until end of turn. (probabilité), Unco.
- *Évariste Galois, mort trop jeune*, {1}{G}{U}, 3/3 first strike *Field theory* -- Sacrifice CARDNAME: target permanent becomes indestructible until end of turn (théorie des corps), Unco.
- *Cauchy, intègre professeur*, {2}{G}{U}, 4/4, *Introduction to Integrals* -- {2},{T}: Choose a color. Add an amount of mana of that color equal to your devotion to that color. <i>(Your devotion to a color is the number of mana symbols of that color in the mana costs of permanents you control.)</i> (intégrales), Rare.
- *Ramanujan, génie autodictate*, {5}{G}{U}, 7/7 trample. *The Man Who Knew Infinity* -- When CARDNAME dies, return it to its owner's hand at the beginning of the next end step. (séries infinies), Rare.

### 11/15 Créatures non légendaires

> Des créatures déjà existantes :

- *Biomathematician*
- [*Gor Muldrak, Amphinologist*](https://scryfall.com/card/cmr/277/gor-muldrak-amphinologist) ?
- https://scryfall.com/card/ncc/86/bennie-bracks-zoologist
- https://scryfall.com/search?q=gist

> Des mana dorks reskins :

- *Étudiant antique* : {1}, 1/2, {T}: add {C}, humain et étudiant, Co.
- *Étudiante au lycée* : {G}, 1/1, {T}: add {G}, humain et étudiant, Co.
- *Étudiant en prépa* : {1}{U}, 1/3, {T}: add one mana of any color, humain et étudiant, Unco.

> Les suivants choisissent un type de créature en arrivant

- *Étudiante à l'ENS* : {G}{W}{U}, 5/4 ne peut pas être bloquée par des créatures de force 2 ou moins, humain et étudiant, Unco.
- *Agrégatif // Professeur agrégé* : {1}{G}{W}{U} : double-faced card, 5/5 up lifelink, humain et étudiant, 7/6 down, humain et chercheur, se retourne en payant 5 life pendant sa phase de fin. Down : parade 1, piétinement et lien de vie, Rare.
- *Doctorante // Docteure ès sciences* : {2}{G}{W}{U} : double-faced card, 5/6 up, humain et étudiant, 7/7 down, humain et chercheur, piétinement et lien de vie, Rare.
- *Chercheuse, Ph.D.* : {3}{G}{W}{U} : 7/7 piétinement et vigilance, {1},{T}: exile target instant or sorcery from an opponent's graveyard. You can cast that card this turn and you may spend mana as though it were mana of any color. If that card would be put into a graveyard this turn, exile it instead. (parce qu'une chercheuse même les meilleurs volent les idées des autres, lol), Mythique.

> Les suivants sont des lords en deux couleurs

- *Doyen de l'Université* : {1}{G}{G} lord +1/+1 à tous les autres G, 2/2, humain et chercheur, Rare. FIXME:
- *Directrice de Laboratoire* : {1}{B}{B} lord +1/+1 à tous les autres B, 2/2, humain et chercheur, Rare.
- *Ministère de la Recherche* : {1}{W}{W} lord +1/+1 à tous les autres W, 2/2, humain et chercheur, Rare.

- *Secrétaire de laboratoire* : {2}{W}{U} permet de lancer les sorts de légendaires en instant, 1/3, humain, Mythique.

-----

### 2 Enchantements qui existent déjà et qui sont "scolaires"

? *Oath of Scholars* (mauvais mais drôle)
- *Rhystic Study*
- *Guardian Project*
? *Kindred Discovery* : semble trop fort, comme tous sont des humains !

### 3 Enchantements : classes

> (Gain the next level as a sorcery to add its ability.)

- *Classe : physicien* : {W}{U}, The first artifact spell you cast each turn costs {1} less to cast. {1}{U}: Level 2 : When this Class becomes level 2, reveal cards from the top of your library until you reveal an artifact card. Put that card into your hand and the rest on the bottom of your library in a random order. {5}{U}: Level 3 : At the beginning of your end step, create a token that's a copy of target artifact you control, except it is not legendary. Unco.
- *Classe : mathématicien* : {G}{U}, When Mathematician Class enters the battlefield, create a 2/2 green Wolf creature token with two +1/+1 counters on it. {1}{G}: Level 2 : Whenever you attack, put a +1/+1 counter on target attacking creature. {2}{G}: Level 3 : You may look at the top card of your library any time. You may cast creature spells from the top of your library. Unco.
- *Classe : informaticien* : {W}{G}, Spells your opponents cast during your turn cost {1} more to cast. {1}{W}: Level 2 : Creatures you control get +1/+1. {3}{W}: Level 3 : Whenever you attack, until end of turn, target attacking creature gets +1/+1 for each other attacking creature and gains double strike. Unco.

> Prendre les dessins de *Artificer Class*, *Bard Class* et *Sorcerer Class* ou *Wizard Class*.
> J'ai pris les concepts de trois classes déjà existantes, pour ne pas trop m'aventurer dans des trucs foireux.

### 2 Enchantements : sagas

- *Remises de prix* : {1}{W}{U}{G}, phase 1 : sur les étudiants et les chercheurs, phase 2 : Prix Nobel sur les physiciens, Prix Turing sur les informaticiens, Médaille Field sur les mathématiciens, phase 3 : gros buff à tout le board. Unco.
- *Demande de financement* : {2}{G}, ça demande d'engager une créature qu'on contrôle comme coût supplémentaire à chaque phase. Phase 1 et 2 : créer un jeton trésor, phase 2 : créer un jeton trésor, phase 3 : tuto un rituel (représente le papier accepté). Unco.

### 3 Enchantements : théorèmes

> Cf. plus haut, un par légendaires qui tuto son théorème ?

- *Théorie de la Relativité* : {1}{W}{W} : Creatures you control have first strike. Creatures your opponents control lose first strike and can't have or gain first strike. Rare.
- *Algorithme de Dijkstra* : {2}{G}{G} : At the beginning of combat during your turn, you may choose a target creature. That creature cannot be blocked this turn. Rare.
- *Théorème d'Euler* : {2}{U} : You may have CARDNAME enter the battlefield as a copy of any artifact or enchantment on the battlefield. Rare.

-----

### 1 Artefacts qui existent déjà et qui sont "scolaires"

- *Annuaire académique* (reskin *Monster Manual*)
? *Urza's Science Fair Project*

### 3 Artefacts : inventions

> Cf. plus haut, un/deux par légendaires qui tuto son invention ?

- *Principes d'Euclide* : (reskin *Wizard's Spellbook*)
- *La Radioactivité* : {1} Creatures you control have deathtouch. Token creatures you control have decayed? (A creature with decayed can't block. When it attacks, sacrifice it at end of combat.)
- *Compilateur LaTeX* : {4} non-creature spells you cast cost {1} less to cast. You can cast non creature spell at instant speed. Whenever you cast a spell during one of your opponents' turn, create a Treasure token, Rare.

### 1 Artefacts : équipement

> Cf. plus haut, un/deux par légendaires qui tuto son invention ?

- *Radium et Polonium* = reskin d'un *Sword of ...*, probablement *Sword of Sinew and Steel* qui est la pro black + pro red, couleurs ennemies du deck, Rare.
? *Lightning Greaves*

### 1 Artefact à mana (5)

- *Sol Ring*
- *Arcane Signet*
? *Thought Vessel*
- *Talisman of Unity* en Selesnya
- *Talisman of Progress* en Azorius
- *Talisman of Curiosity* en Simic
? *Mad Science Fair Project*

-----

### 3 Éphémères / instants

- *Sword to Plowshares*
- *Path to Exile*
- *Beast Within*

-----

### 4 Rituels / sorcery

- *Farseek*
- *Cultivate*
- *Nature's Lore*
- *Kindred Summons*

Est-ce que les joueurs m'autoriseront des Leçons hors du jeu ? Non pas en EDH hein.

-----

### Terrains (35 en tout) : 8 lieux légendaires de la science

> Max 8 nouveaux terrains légendaires

- *Athène antique* (reskin *Unclaimed Territory*)
- *Paris et ses Universités* (reskin *Cavern of Souls*)
- *Cambridge et Oxford* (reskin *Secluded Courtyard*)

- *Salle de Classe* : aide les étudiants
- *Le MIT* : aide les créatures-artefacts ?

- *Institute for Advanced Study, Princeton* : (aide les physiciens) arrive engagé sauf si on révèle une carte de physicien, produit {U} ou {W}, Rare.
- *L'ENS* : (aide les mathématiciens) arrive engagé sauf si on révèle une carte de mathématicien, produit {U} ou {G}, Rare.
- *Palo-Alto, berceau de l'informatique* : (aide les informaticiens) arrive engagé sauf si on révèle une carte de informaticien, produit {G} ou {W}, Rare.

Sans changement des terrains rares 14 :

- 3 fetchlands : *Flooded Strain*, *Misty Rainforest*, *Windswept Heath*
- 3 shocklands : *Breeding Pool*, *Hallowed Fountain*, *Temple Garden*
- 3 painlands : ? (reskin *Adarkar Wastes*), *Brushland*, ? (reskin *Yavimaya Coast*)
- 3 filterland : *Flooded Grove*, *Mystic Gate*, *Wooded Bastion*
- 2 canopyland : *Horizon Canopy*, *Waterlogged Grove*

- Des basiques pour terminer : 38 - 22 = 16 donc 3 de chaque + 4 terrains communs
- *Command Tower*
- *Study Hall*
- *Reliquary Tower*
- *Path of Ancestry*
- 3 *Plains*
- 3 *Forest*
- 3 *Island*

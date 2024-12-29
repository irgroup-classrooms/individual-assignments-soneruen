# Aufgabenbearbeitung Dokumentation / Exercises for Task: 05

## Description of Data Fields in "lotr_characters.csv"

- **birth**: The birth date of the character. This may be a specific date or a time period (e.g., "late Third Age").
  
- **death**: The death date of the character, if known. Some dates may be imprecise, such as "February 26" without a year.

- **gender**: The gender of the character, if available. This could be "Male" or "Female," though some characters may not have a specified gender.

- **hair**: The hair color of the character, if known. This field may be left empty if the information is not available.

- **height**: The height of the character, if measured or described. This could be a specific measurement or a general description (e.g., "tall" or "short").

- **name**: The full name of the character as it appears in the lore of the story.

- **race**: The race of the character (e.g., Men, Elves, Orcs, etc.). This field identifies the species or cultural group the character belongs to.

- **realm**: The realm or place with which the character is associated. This could be a kingdom, city, or general geographical region.

- **spouse**: The name of the character's spouse, if married. This field may be empty for unmarried characters or those with unknown spouses.


## Description of Data Field in "lotr_scripts.csv"

- **Column**: The name of the character speaking in the dialog (e.g., Frodo, Gandalf, etc.). This field contains the main characters who speak their lines in the script.

- **char**: A shortened version or alias of the character name, if applicable. For example, "Gollum" might appear as "(GOLLUM)" in some lines. This column is used to identify the speaker more concisely, with some entries containing variations in name formatting.

- **dialog**: The actual spoken dialog or quote by the character. This field contains the text spoken by the character in the movie, including dialogue with punctuation, expressions, or exclamations.

- **movie**: The title of the movie in which the dialog was spoken (e.g., "The Fellowship of the Ring," "The Return of the King"). This column helps identify which movie the dialog comes from when the dataset contains multiple films.


## Issues with Data Quality

While working with the "lotr_characters.csv" file, I encountered some issues related to data quality, such as incorrect character names. For instance, some names are improperly encoded, like "Ar-AdÃ»nakhÃ´r," which appears due to character encoding problems.

To address these issues, I took the following steps:

1. **Text Editor (Notepad++)**: I opened the CSV file in Notepad++ and re-encoded it to UTF-8 format to ensure proper character representation.
2. **Excel**: I imported the file into Excel using the "Get Data" (Daten abrufen/Aus Datei/txt-file) with the Excel Power-Query feature to load it properly. The file was structured into tabs, including the data and the "data retrieval" process. I used the option to use the first line of the CSV as headers.
3. **Excel Formatting**: This method allowed the columns and formats to be automatically detected, as seen in datasets like those from Kaggle.
4. **Empty Fields**: While working with the data, I left many open fields with no value in them to match them with the input file from Kaggle, where the content was originally downloaded from.




## Analysis Task for lotr_scripts_clean:

- Find the total number of lines and unique words used in the dialogs (lotr_scripts_clean.csv)
```bash
# Count the total number of lines in the CSV
# Zählt die Gesamtzahl der Zeilen in der CSV-Datei
wc -l lotr_scripts_clean.csv
# Output: 2391
```

- Find the total number of unique words:
```bash
# Count the distribution of movies in the dataset
# Zählt, wie viele Male jede Filmbezeichnung in der CSV vorkommt
awk -F',' '{print $4}' lotr_scripts_clean.csv | sort | uniq -c
# Output: 2256
```

- What is the distribution across the three different films (lotr_scripts_clean.csv)?
```bash
# Count the distribution of movies in the dataset again
# Zählt erneut, wie viele Male jede Filmbezeichnung in der CSV vorkommt
awk -F',' '{print $4}' lotr_scripts_clean.csv | sort | uniq -c
# Output: 2256
      1
      1          The crownless again shall be king. ;The Return of the King
      1      Bagshot Row
      1      Childless lords sat in aged halls musing on heraldry or in high
      1      Hobbit meat. And when she throws away the bones and the empty clothes
      1      The Witch King of Angmar. You've met him before. 
      1      The pity of Bilbo
      1      after all
      1      always follow your nose. ;The Fellowship of the Ring
      1      as he hates and loves himself.  Smeagol's life is a sad story
      1      besides the will of evil.  Bilbo was meant to find the Ring
      1      but we've not much for afters. Oh no we're all right
      1      perhaps
      1      stock and stone I can master
      1      you'll have me to answer to.   One sniff that something's not right
      1     Aragorn. The people of Rohan will need you.
      1   Come on you slugs!  You two are going straight to the front line!  Move it
      1   The grey rain curtain of this world rolls back and all turns to silvered glass.  And then you see it.     ;The Return of the King
      1   You must understand.  The Ring is my burden.  It will destroy you Sam.      ;The Return of the King
      1  ' from this hour henceforth     until my lord release me or death take me. ;The Return of the King
      1  A shadow moves in the dark.
      1  And     the Ring of Power perceived.
      1  Bring forth the Ring
      1  But you'll never find a beer so     brown
      1  Gollum.
      1  Grond
      1  Grond!  ;The Return of the King
      1  I want to see     mountains again
      1  In the land of Mordor
      1  It would've been her.  ;The Return of the King
      1  Lathspell I name him.Ill news is an ill guest. ;The Two Towers
      1  May it be a light for you in dark places
      1  Mithril!
      1  Mr err... ? ;The Fellowship of the Ring
      1  Mr. Frodo
      1  Mr. Frodo. The ones that really mattered.
      1  Mr. Frodo. You have to fight it. ;The Two Towers
      1  Not seen     him for six months.  ;The Fellowship of the Ring
      1  Oh
      1  Only death! ;The Fellowship of the Ring
      1  Pippin. More than anything I wish I could see them again. ";The Return of the King
      1  Raaar it's the dwarves that go swimming with little
      1  Sam. If I put it     on......he'll find me. He'll see. ;The Two Towers
      1  Seven to the     dwarf lords
      1  They     will never stop hunting you. ;The Fellowship of the Ring
      1  Who had this one chance to destroy evil     forever.
      1  almost as old     as I am. ;The Fellowship of the Ring
      1  and Boromir of Gondor. ;The Two Towers
      1  and we wants it! ;The Two Towers
      1  breakinghacking
      1  but it wasn't out of charity. I think it was because
      1  but strong.   ;The Return of the King
      1  by any     craft that we here possess. The Ring was made in the fires of Mount Doom.      Only there can it be unmade.  It must be taken deep into Mordor and     cast back into the firey chasm from whence it came.
      1  crept from the shadows will never be crowned King.
      1  doesnt he ? ;The Fellowship of the Ring
      1  edro hi ammen! (     ;The Fellowship of the Ring
      1  esquire of Rohan.  ;The Return of the King
      1  except sideways.   ;The Return of the King
      1  forged from the shards of     Narsil.   ;The Return of the King
      1  from the river.
      1  get off your ships.      ;The Return of the King
      1  golden chipswith a nice piece of fried fish.  ;The Two Towers
      1  half as well as you deserve.    ;The Fellowship of the Ring
      1  he's known as Strider. ;The Fellowship of the Ring
      1  here we are.       ;The Fellowship of the Ring
      1  hodo
      1  if it comes at all.
      1  it     has been remarked by some that Hobbits' only real passion is for food.
      1  kill them both!
      1  let's hope it lasts the night.       ;The Two Towers
      1  lie!  ;The Two Towers
      1  listen     to me. ;The Two Towers
      1  little Shirelings.
      1  master. We will take youon safe paths through the mist.Come
      1  more than usual. He's taken to locking himself in his study.
      1  my own
      1  not grieve for those whose time has come. You     shall live to see these days renewed
      1  now far ahead the road     has gone
      1  on the     shores of the sea
      1  our people     who are dying. Sauron is biding his time. He's massing fresh armies. He will     return. And when he does
      1  pull it in!  ;The Return of the King
      1  shields shall be splintered
      1  son of the King
      1  stille n'. Lac is drefed
      1  take it
      1  the     fields and the little rivers. I am old Gandalf. I know I don't look it
      1  the Steward of Gondor kept     the forces of Mordor at bey.  By the
      1  the canniest
      1  the farther we are from harm.      It's the last thing he'll expect.       ;The Two Towers
      1  the last defence of this city will be gone.  ;The Return of the King
      1  the same fear that would take the heart of me. A day may come     when the courage of men fails
      1  they say......as an old man hooded and cloaked.And everywhere
      1  they suspects us! ;The Return of the King
      1  things are now in motion that cannot be undone. I ride for     Minas Tirith
      1  thousands of Orcses.And always the Great Eye watching
      1  to show his     quality. I think not.
      1  wasn't he
      1  we could pass through the     Mines of Moria.  My cousin Balin would give us a royal welcome.  ;The Fellowship of the Ring
      1  we warned you! Prepare to be boarded!  ;The Return of the King
      1  when Gondor's need was dire
      1  where is that boy! FRODO!  ;The Fellowship of the Ring
      1  yes
      1  your doom is near at hand
      1  your king. ;The Two Towers
      1 ) ;The Fellowship of the Ring
      1 ...and we never say anything......unless it is worth taking......a long time to say.
      1 3'8""! ";The Two Towers
      1 A chance for Faramir
      1 And then we take the precious......and we be the master!           ;The Two Towers
      1 Could be a distant relative.           ;The Two Towers
      1 Get the women and children     into the caves. ;The Two Towers
      1 Give it to us raw...
      1 He took it!
      1 He was my brother. ;The Two Towers
      1 History became legend
      1 I can see him with my waking eyes!  ;The Return of the King
      1 I mean
      1 It is a dangerous road to takethrough the mountains.
      1 Its still sharp
      1 Look to my coming at first light on the fifth day. At dawn
      1 Now
      1 So fair. So cold. Like a morning of pale spring......still clinging     to winter's chill. ;The Two Towers
      1 You wonder what his name is......where he came from.
      1 for     Gondor! ;The Two Towers
      1       Valour with honour.  Disloyalty with vengeance. 
      1      ;The Return of the King
      1      ;The Two Towers
      1   And     there are many paths to tread
      1   He is dead then.
      1   He wants it.  He needs     it.  Smeagol sees it in his eye. 
      1   Legions of Haradrim from     the South
      1   On the third
      1  Farewell. Hold to     your purpose and may the blessings of elves
      1  Lovely to see you
      1    do they?   ;The Return of the King
```

-  What are the top 5 characters in the dialogues (lotr_scripts.csv)?
```bash
# Find the top 5 characters mentioned in the 'dialog' column (case-sensitive matching)
# Findet die 5 meistgenannten Charaktere in der 'dialog'-Spalte (Groß-/Kleinschreibung wird berücksichtigt)
grep -o '\b[A-Z][a-z]*\b' lotr_scripts_clean.csv | sort | uniq -c | sort -nr | head -n 5
# Output:
#    2615 The
#    1011 Two
#    1010 Towers
#     907 King
#     874 Return
```
# TupTupTup
Docker w wersji produkcyjnej nie chce działać (próbowałem podpiąć to pod własną domenę), dlatego też do odpalenia należy użyć dockera w wersji devowej.  
Komenda do odpalenia: 
```bash
docker-compose -f docker-compose.yml up -d --build
```
Gaszenie kontenerów:
```bash
docker-compose down -v
```
Logi:
```bash
docker-compose logs -f
```
Link do testu aplikacji:  
http://fastapi.localhost:8008

Zdecydowałem się na FastAPI, dzięki któremu dodałem na stronę możliwość losowania memów oraz dodawania nowych. 
Baza okazała się niepotrzebna, bo strona nie wymaga systemu logowania, ani przechowywania żadnych informacji, memy znajdują się po prostu na dysku serwera, w odpowiednim folderze (co jest też przydatną funkcjonalnością, bo dodałem folder z nimi do plików statycznych).
W projekcie celowałem w to, żeby był dla mnie użyteczny, bardziej niż zasługiwał na wysoką ocenę, dlatego backend nie jest zbyt rozbudowany (i jakby nie patrzeć miałem tylko kilka wolnych godzin na ten projekt, z czego większość spędziłem przy dockerze i javascripcie, które do oceny nawet nie są potrzebne). 
Plan na przyszłość to na pewno prawidłowe podpięcie własnej domeny, podmienienie Google Drive'a na własnego NextClouda hostowanego na malince i opracowanie ładniejszego frontu np React(wtedy mógłbym po prostu połączyć front z backiem i nie używać poza obrazami plików statycznych).
Chciałbym bardzo dodać bazę, tylko nie wpadłem na dobry pomysł na funkcjonalność, która mogłaby z niej korzystać. Może zamiast NextClouda zbuduję jakiś własny system wyświetlania treści.

Proszę też nie zwracać za bardzo uwagi na zawartość linków z materiałami. Są tam materiały dla "potomnych", jakieś pdfy czy egzaminy/kolokwia z poprzednich lat, ale może trafić się też coś czego nie powinno zobaczyć oko prowadzącego na UMCS-ie.
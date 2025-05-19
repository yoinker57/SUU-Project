# Pixie - Projekt z przedmiotu Środowiska Udostępniania Usług

**Autorzy:** Piotr Wolanin, Radosław Niżnik, Jakub Kroczek, Jakub Bizan

**Rok:** 2025 **Grupa:** 14

---

## Spis treści

1.  [Wprowadzenie](#wprowadzenie)  
2.  [Podstawy teoretyczne i stos technologiczny](#podstawy-teoretyczne-i-stos-technologiczny)  
3.  [Opis studium przypadku](#opis-studium-przypadku)  
4.  [Architektura rozwiązania](#architektura-rozwiązania)  
5.  [Konfiguracja środowiska](#konfiguracja-środowiska)  
6.  [Sposób instalacji](#sposób-instalacji)  
7.  [Odtworzenie rozwiązania](#odtworzenie-rozwiązania)
8.  [Wdrożenie wersji demonstracyjnej](wdrożenie-wersji-demonstracyjnej)
9.  [Wykorzystanie AI](#wykorzystanie-ai)
10. [Bibliografia](#bibliografia)

---

## Wprowadzenie

W ramach niniejszego projektu zostanie zaprojektowana i wdrożona aplikacja działająca w środowisku Kubernetes, której kluczowym elementem będzie integracja z systemem obserwowalności opartym na standardzie OpenTelemetry. Dane telemetryczne, obejmujące metryki, logi i trasy żądań, będą zbierane przy użyciu narzędzia Pixie służącego do automatycznego monitorowania klastrów Kubernetes w czasie rzeczywistym. Zebrane dane zostaną przesłane i zwizualizowane w Grafanie, umożliwiając pełen wgląd w działanie aplikacji i analizę wydajności.

---

## Podstawy teoretyczne i stos technologiczny

### Podstawy teoretyczne

**Pixie** to narzędzie typu open-source służące do automatycznego monitorowania i obserwowalności aplikacji uruchamianych w klastrach Kubernetes. Jego głównym celem jest dostarczanie szczegółowych informacji o stanie systemu bez konieczności ręcznego instrumentowania kodu aplikacji lub instalowania agentów wewnątrz kontenerów.

Pixie wykorzystuje **eBPF (Extended Berkeley Packet Filter)** — technologię jądra systemu Linux, która pozwala na wydajne przechwytywanie danych o zdarzeniach systemowych bez modyfikowania kodu aplikacji. Dzięki temu Pixie jest w stanie za pomocą sond obserwować ruch sieciowy, systemowe wywołania funkcji, trasowanie zapytań, a także zbierać metryki o wydajności aplikacji praktycznie w czasie rzeczywistym, minimalizując jednocześnie narzut wydajnościowy.

Kluczowe zalety Pixie:

- **Bezagentowe monitorowanie:** Pixie nie wymaga modyfikacji kodu ani instalowania agentów w aplikacjach. Wystarczy zainstalować Pixie na poziomie klastra Kubernetes.
- **Obliczenia wewnątrz klastra (In-cluster edge compute):** Pixie wykonuje większość obliczeń i analizy danych bezpośrednio wewnątrz klastra, co ogranicza potrzebę przesyłania dużych ilości danych na zewnątrz i zmniejsza opóźnienia, a wykorzystuje tylko do około 5% klastrowego CPU.
- **Zapytania za pomocą PxL (Pixie Query Language):** Pixie posiada własny język zapytań (PxL), który umożliwia użytkownikom definiowanie niestandardowych zapytań telemetrycznych i analiz bez konieczności pisania skomplikowanego kodu.

### Stos technologiczny

W celu lokalnego uruchomienia klastra Kubernetes wykorzystano narzędzie Minikube. Pozwala ono w prosty sposób stworzyć środowisko testowe, umożliwiając szybkie testowanie i wdrażanie aplikacji kontenerowych bez potrzeby korzystania z chmury.

Aplikacja została skonteneryzowana przy użyciu Dockera, co zapewnia przenośność i ułatwia integrację z Kubernetesem.

Do zarządzania klastrem użyto narzędzia Kubectl — oficjalnego klienta linii poleceń dla Kubernetes, który pozwala m.in. na wdrażanie aplikacji, przeglądanie stanu zasobów oraz wykonywanie operacji administracyjnych w klastrze.

Wizualizacja danych telemetrycznych odbywa się w Grafanie — otwartoźródłowej platformie analitycznej. Dane przesyłane są w standardzie OpenTelemetry, który zapewnia jednolity sposób zbierania metryk, logów oraz tras żądań z aplikacji rozproszonych.

---

## Opis studium przypadku

W ramach projektu, jako środowisko demonstracyjne, wykorzystywana jest aplikacja [Sock Shop](https://github.com/pixie-labs/sock-shop-microservices-demo). Jest to popularna, realistyczna aplikacja demonstracyjna zbudowana w oparciu o architekturę mikroserwisów.

### Czym Jest Sock Shop?
Sock Shop to symulacja internetowego sklepu sprzedającego skarpetki. Został zaprojektowany nie jako pełnoprawny sklep, ale jako złożony system demonstracyjny, którego głównym celem jest ilustrowanie i ułatwianie testowania narzędzi i praktyk związanych z:
- Architekturą mikroserwisów: Prezentuje podział funkcjonalności na wiele niezależnych, komunikujących się ze sobą serwisów.
- Monitoringiem i obserwowalnością: Stanowi doskonałe środowisko do zbierania logów, metryk i śladów (tracingu) z rozproszonego systemu.
- Zarządzaniem kontenerami i orkiestracją: Idealnie nadaje się do demonstracji wdrożeń na platformach takich jak Kubernetes, Docker Swarm czy Nomad.
- Automatyzacją wdrożeń (CI/CD): Poszczególne mikroserwisy mogą być rozwijane i wdrażane niezależnie.
### Architektura
Sock Shop składa się z kilkunastu mikroserwisów, z których każdy odpowiada za specyficzny obszar funkcjonalny sklepu. Kluczowe komponenty to m.in.:
- front-end: Serwuje interfejs użytkownika i działa jako bramka API.
- catalogue: Zarządza listą produktów (skarpetek).
- carts: Obsługuje koszyk zakupowy dla użytkowników.
- orders: Procesuje i przechowuje zamówienia.
- users: Zarządza danymi użytkowników.
- payment: Symuluje proces płatności.
- shipping: Symuluje proces wysyłki.

Co istotne, Sock Shop wykorzystuje różnorodne technologie i języki programowania (np. Go, Java Spring Boot, Node.js, Python), a także różne bazy danych (np. MongoDB, MySQL). Ta architektura doskonale odzwierciedla złożoność i wyzwania typowe dla rzeczywistych środowisk mikroserwisowych, gdzie różne zespoły mogą wybierać technologie najlepiej dopasowane do ich potrzeb.

---

## Architektura rozwiązania

TODO: Dodać architekturę w sensie diagram jak to się komunikuje ze sobą (px_sock_shop -> Pixie -> za pomocą Grafana Plugin Pixie wysyła do zewnętrznej chmury -> Grafana wysyła zapytanie do chmury)

---

## Konfiguracja środowiska

TODO: Opisać grafana_values i trochę jak był konfigurowany px-sock-shop (jeśli była potrzeba żeby działał z Pixie)

px_sock_shop i monitoring (grafana_values)

---

## Sposób instalacji

Jako krok wstępny należy upewnić się, czy poniższe narzędzia są zainstalowane:

- [Minikube](https://minikube.sigs.k8s.io/docs/start/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Pixie CLI (px)](https://docs.px.dev/installing-pixie/install-schemes/cli/)

### Instalacja przez skrypt w Pythonie

Dodatkowo wymagany zainstalowany język Python. 

Krok 1: Przejście do katalogu projektu

```bash
cd <path_to_repository>/SUU-Project
```

Krok 2: Uruchomienie skryptu w Pythonie

```bash
python script.py
```

### Instalacja ręczna

Krok 1: Uruchomienie klastra Minikube

```bash
minikube start --driver=kvm2 --memory=8192 --cpus=4
```
Krok 2: Przejście do katalogu projektu

```bash
cd <path_to_repository>/SUU-Project
```

Krok 3: Instalacja Pixie w klastrze

```bash
px deploy --check=false -y
```

Krok 4: Wdrożenie przykładowej aplikacji demonstracyjnej

```bash
px demo deploy px-sock-shop -y
```

Krok 5: Tworzenie przestrzeni nazw dla monitoringu

```bash
kubectl create namespace monitoring
```

Krok 6: Instalacja Grafany z użyciem Helm

Upewnij się, że masz plik `grafana-values.yaml` w bieżącym katalogu. Następnie uruchom:

```bash
helm upgrade --install grafana grafana/grafana -f grafana-values.yaml -n monitoring
```

### Dodatkowe uwagi

-

- Pixie UI można otworzyć komendą:

  ```bash
  px ui
  ```

---

## Odtworzenie rozwiązania

TODO: Opisać jak połączyć wszystkie serwisy po instalacji (api tokeny, logowanie do Grafany itd.)

---

## Wdrożenie wersji demonstracyjnej

TODO: Usunąć jak nie będzie potrzebne

---

## Wykorzystanie AI

TODO: opisać wykorzystanie AI w rysunkach i do poprawy błędów składniowych i gramatycznych) (próba pracy z AI zawiodła przez niedziałający kod z dokumentacji)

---

## Bibliografia

1. Kubernetes Community. *Minikube*. [https://minikube.sigs.k8s.io/docs/](https://minikube.sigs.k8s.io/docs/)

2. Google. *Kubernetes*. [https://kubernetes.io/docs/home/](https://kubernetes.io/docs/home/)

3. DeisLabs. *Helm*. [https://helm.sh/docs/](https://helm.sh/docs/)

4. New Relic, Inc. *Pixie*. [https://docs.px.dev](https://docs.px.dev)

5. Brendan Gregg. *BPF and eBPF*. [https://www.brendangregg.com/ebpf.html](https://www.brendangregg.com/ebpf.html)

6. Torkel Ödegaard. *Grafana*. [https://grafana.com/grafana/](https://grafana.com/grafana/)

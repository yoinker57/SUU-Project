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

W ramach projektu, jako środowisko demonstracyjne, wykorzystywana jest aplikacja [Sock Shop](https://github.com/pixie-labs/sock-shop-microservices-demo). Jest to realistyczna aplikacja demonstracyjna zbudowana w oparciu o architekturę mikroserwisów.

### Czym jest Sock Shop?
Sock Shop to symulacja internetowego sklepu sprzedającego skarpetki. Został zaprojektowany nie jako pełnoprawny sklep, ale jako złożony system demonstracyjny, którego głównym celem jest zilustrowanie i ułatwienie testowania narzędzi i praktyk związanych z:
- Architekturą mikroserwisów - prezentuje podział funkcjonalności na wiele niezależnych, komunikujących się ze sobą serwisów.
- Monitoringiem i obserwowalnością - stanowi doskonałe środowisko do zbierania logów, metryk i śladów (tracingu) z rozproszonego systemu.
- Zarządzaniem kontenerami i orkiestracją - idealnie nadaje się do demonstracji wdrożeń na platformach takich jak Kubernetes.
- Automatyzacją wdrożeń (CI/CD) - poszczególne mikroserwisy mogą być rozwijane i wdrażane niezależnie.
### Architektura
Sock Shop składa się z kilkunastu mikroserwisów, z których każdy odpowiada za specyficzny obszar funkcjonalny sklepu. Kluczowe komponenty to m.in.:
- front-end - serwuje interfejs użytkownika i działa jako bramka API.
- catalogue - zarządza listą produktów (skarpetek).
- cart - obsługuje koszyk zakupowy dla użytkowników.
- order - procesuje i przechowuje zamówienia.
- user - zarządza danymi użytkowników.
- payment - symuluje proces płatności.
- shipping - symuluje proces wysyłki.

![image](https://github.com/microservices-demo/microservices-demo.github.io/blob/HEAD/assets/Architecture.png)

Co istotne, Sock Shop wykorzystuje różnorodne technologie i języki programowania (np. Go, Java Spring Boot, Node.js, Python), a także różne bazy danych (np. MongoDB, MySQL). Ta architektura doskonale odzwierciedla złożoność i wyzwania typowe dla rzeczywistych środowisk mikroserwisowych, gdzie różne zespoły mogą wybierać technologie najlepiej dopasowane do ich potrzeb.

---

## Architektura rozwiązania

![image](https://github.com/user-attachments/assets/3c44c7eb-a3ea-4e9a-ac8e-024dcffe9170)

Na środowisku Minikube została postawiona aplikacja Sock Shop. Dodatkowo zostało zainstalowane narzędzie Pixie do jej monitorowania oraz OTLP collector wraz z prometheusem do zbierania metryk z naszej aplikacji, oraz Grafana do wizualizacji metryk.

Pixie za pomocą pluginu eksportuje dane w formacie zgodnym z OpenTelemetry, które następnie są zbierane przez nasz collector. Dane trafiają dalej do prometheusa (bądź alternatywnie do innych rozwiązań np. Loki), a następnie przy jego pomocy do grafany.

Alternatywnie (a zarazem prościej) Pixie komunikuje się protokołem HTTPS z zewnętrzną chmurą Cosmic Cloud. Grafana wysyła zapytanie do chmury wykorzystując PXL (Pixie Query Language), a następnie Cosmic Cloud przesyła dane do Grafany protokołem HTTPS.

---

## Konfiguracja środowiska

Pixie jest narzędziem, które nie wymaga żadnych dodatkowych kroków poza instalacją. Można korzystać ze zgromadzonych przez niego metryk bezpośrednio przez Pixie UI, albo przez integrację z innymi narzędziami do wizualizacji.

Ostatnią rzeczą, którą musimy zrobić jest dodanie pluginu do Grafany, aby móc używać Pixie jako źródła danych. Nie jest to za bardzo skomplikowana operacja, wystarczy stworzyć plik `grafana-values.yaml` a w nim dodać:

```yaml
plugins:
  - pixie-pixie-datasource
```

Zapewnimy sobie tym automatyczną instalację naszego pluginu podczas wykonywania komendy:

```bash
helm upgrade --install grafana grafana/grafana -f grafana-values.yaml -n monitoring
```

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

Krok 6: Instalacja Collectora

```bash
kubectl apply -f collector.yaml
```

Krok 7: Instalacja Prometheusa

```bash
kubectl apply -f prometheus.yaml -n monitoring
```

Krok 8: Instalacja Grafany z użyciem Helm

Upewnij się, że masz plik `grafana-values.yaml` w bieżącym katalogu. Następnie uruchom:

```bash
helm upgrade --install grafana grafana/grafana -f grafana-values.yaml -n monitoring
```

---

## Odtworzenie rozwiązania

### Logowanie do Grafany

Aby zalogować się do Grafany musimy uzyskać do niej hasło. Robimy to wywołując komendę:

```bash
kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode
```

A następnie musimy przekierować port grafany, aby uzyskać do niego dostęp pod adresem: `http://localhost:3000`:

```bash
  kubectl --namespace monitoring port-forward {pod_name} 3000
```

Nazwę poda uzyskamy przy pomocy komendy:
```bash
kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=grafana
```

### Konfiguracja Prometheusa w Grafanie:

Aby dokonać połączenia Prometheusa z Grafaną musimy przejść do dodawania nowego źródła danych w Grafanie (Settings -> Data Source), a następnie dodajemy nowe źródło danych wybierając `Prometheus`.
Po wybraniu musimy podać tylko adres prometheusa jako `http://prometheus-service.monitoring.svc.cluster.local:9090`.

Następnie możemy używać danych z prometheusa przy tworzeniu naszych dashboardów.


### Konfiguracja Pixie w Grafanie

Aby dokonać połączenia Pixie z Grafaną musimy przejść do dodawania nowego źródła danych w Grafanie (Settings -> Data Source), a następnie dodajemy nowe źródło danych wybierając `Pixie Grafana Datasource Plugin`.
Po wybraniu musimy podać odpowiednie konfiguracje:

![image](https://github.com/user-attachments/assets/97ddc0a1-6527-4b8e-9ee8-7245bafbdeee)

W polu Pixie Api Key musimy wpisać klucz, który możemy uzyskać na stronie https://work.getcosmic.ai/ lub komendą:

```bash
px api-key create
```

W polu Cluster ID musimy wpisać ID uzyskane również na stronie https://work.getcosmic.ai/ lub przy pomocy komendy:

```bash
px get viziers
```

Jako Pixie Cloud Address musimy podać: `work.getcosmic.ai:443`

### Import dashboardu

Aby zaimportować dashboard do Grafany musimy przejść do zakładki `Dashboards` i kliknąć `New`, a następnie `Import`. Później wybieramy plik JSON  z katalogu `dashboards` znajdującego się w tym repozytorium.

---

## Przykładowe dashboardy

### Śledzenie requestów:
Pixie monitoruje wywołania stemowe związane z siecią. Dzięki temu może przechwytywać dane przesyłane między usługami, analizować je i prezentować w czytelnej formie. Dostępny jest pełny podgląd zawartości zapytania. Wspierane protokoły to między innymi HTTP, DNS, MySQL, Redis, Kafka.

![image](https://github.com/user-attachments/assets/00987edc-f330-417e-9601-38c8d35912c9)

### Profile aplikacji
Co około 10ms tworzony jest zrzut aktualnego stosu wywołań. Zawiera on aktualnie wywoływaną funkcje, a także wszystkie funkcje nadrzędne, które zostały wywołane, aby dojść do tego punktu w kodzie. Zebrane próbki są agregowane w szerszym, 30-sekundowym oknie czasowym, które obejmuje tysiące śladów stosu. Następnie te ślady są grupowane według wspólnych funkcji nadrzędnych. Na każdym poziomie — im szerszy fragment stosu, tym częściej dana funkcja pojawiała się w śladach stosu. Szersze ślady stosu są zazwyczaj bardziej interesujące, ponieważ wskazują, że znaczna część czasu działania aplikacji była spędzana w tej funkcji.
Funkcjonalność dostępna jest dla języków: Go, C/C++, Rust oraz Java.

![image](https://github.com/user-attachments/assets/76279908-a025-4708-a832-ff94fb906a08)

### Metryki takie jak wykoszystanie procesora:

![image](https://github.com/user-attachments/assets/8d31d312-f737-4c94-8a96-363faba91090)

### Matryki z prometheusa:

![image](https://github.com/user-attachments/assets/5fbfca7d-72e8-43e1-9be9-a609418bff8c)


## Wykorzystanie AI

Używaliśmy AI (narzędzie ChatGPT) do odpytywania odnośnie dokumentacji Pixie, niestety nie udało się nam w ten sposób uzyskać wszystkich potrzebnych informacji. Przydatne okazały się zapytania o konfigurację Grafany - głównie o instalację samej Grafany oraz ważnego Pixie Pluginu z czym poradził sobie zaskakująco dobrze (podejrzewamy, że było to spowodowane prostotą instalacji jak i szerokim dostępem do dokumentacji).

Kolejnym wykorzystaniem AI było zapytanie o skrypt do automatyzacji całego procesu, co również się udało, głównie przez to, że najpierw musieliśmy przejść przez wszystkie kroki ręcznie, więc AI w prompcie miało dostęp do wszystkich komend, których używaliśmy do instalacji. Jednak i tutaj musieliśmy poprawić kilka rzeczy, ponieważ niektóre komendy były błędne, a inne wymagały dodatkowych argumentów.

Finalnie stwierdzamy, że AI nie jest w stanie zastąpić dokumentacji, a próby jej użycia mogą wprowadzać dodatkowy chaos, ale dobrze sobie radzi z poprawą błędów gramatycznych w dokumentacji :)

---

## Bibliografia

1. Kubernetes Community. *Minikube*. [https://minikube.sigs.k8s.io/docs/](https://minikube.sigs.k8s.io/docs/)

2. Google. *Kubernetes*. [https://kubernetes.io/docs/home/](https://kubernetes.io/docs/home/)

3. DeisLabs. *Helm*. [https://helm.sh/docs/](https://helm.sh/docs/)

4. New Relic, Inc. *Pixie*. [https://docs.px.dev](https://docs.px.dev)

5. Brendan Gregg. *BPF and eBPF*. [https://www.brendangregg.com/ebpf.html](https://www.brendangregg.com/ebpf.html)

6. Torkel Ödegaard. *Grafana*. [https://grafana.com/grafana/](https://grafana.com/grafana/)

7. Microservices Demo. *microservices-demo*. [https://github.com/microservices-demo/microservices-demo](https://github.com/microservices-demo/microservices-demo)

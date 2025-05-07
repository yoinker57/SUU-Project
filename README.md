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

_placeholder_

---

## Architektura rozwiązania

_placeholder_

---

## Konfiguracja środowiska

_placeholder_

---

## Sposób instalacji

_placeholder_

---

## Odtworzenie rozwiązania

_placeholder_

---

## Wdrożenie wersji demonstracyjnej

_placeholder_

---

## Wykorzystanie AI

_placeholder_

---

## Bibliografia

_placeholder_

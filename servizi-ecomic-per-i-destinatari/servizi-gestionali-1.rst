.. _servizi-gestionali-1:

Servizi gestionali   
==================

I servizi gestionali   sono **dedicati all’archiviazione, organizzazione, descrizione, gestione e amministrazione dei beni digitali**. Costituiscono l’infrastruttura operativa che consente agli Attori   dell’ecosistema – in particolare istituzioni culturali, enti pubblici e soggetti titolari di beni digitali   – di mantenere, valorizzare e rendere disponibile nel tempo il proprio :term:`patrimonio digitale <Patrimonio digitale>`. Operano dietro le quinte della fruizione pubblica, ma sono cruciali per assicurare che i contenuti digitali siano correttamente ospitati e gestiti in un’ottica di lungo periodo, nel solco del lavoro svolto dagli Istituti Centrali, che Ecomic riconosce e valorizza come fondamento per costruire un ecosistema condiviso e continuo.

.. _sistemi-informativi-afferenti-alla-categoria-1:

Sistemi informativi afferenti alla categoria
--------------------------------------------

Tra i principali sistemi informativi dedicati alla gestione del patrimonio digitale si possono citare:

-  CLIO, per il patrimonio storico-artistico e demo-etnoantropologico, recentemente sviluppato e presentato nel mese di febbraio 2025 in sostituzione di SIGECWeb;

-  SBN (Servizio Bibliotecario Nazionale), per la gestione delle risorse bibliografiche;

-  SIA (Sistema Informativo Archivistico), per la gestione delle risorse archivistiche.

Rientrano nella categoria anche i sistemi per la conservazione digitale a lungo termine, fondamentali per garantire l’integrità e l’accesso ai contenuti nel tempo. Ne sono esempio:

-  Polo di conservazione digitale del MiC, integrato con i sistemi centrali del Ministero;

-  | conservatori accreditati AgID, impiegati da enti e istituzioni per la conservazione | a norma di documenti digitali, metadati e pacchetti informativi;

-  Polo Strategico Nazionale (PSN), infrastruttura cloud sicura sviluppata per ospitare dati e servizi critici delle pubbliche amministrazioni italiane.

Sono incluse inoltre le piattaforme di gestione documentale, strumenti per il controllo di versioni, metadati e flussi di pubblicazione, che permettono di mantenere coerenza dei dati lungo il loro :term:`ciclo di vita <Ciclo di vita del bene digitale>`, e ambienti integrati per l’editing, la verifica e la validazione dei contenuti, orientati a processi editoriali, di controllo qualità e arricchimento semantico.

Queste soluzioni, adottate in contesti diversi ma complementari, rappresentano la base infrastrutturale essenziale per una gestione efficace, sostenibile e conforme agli standard del patrimonio culturale digitale.

Teca multimediale
-----------------

La Teca Multimediale è un’applicazione rilasciata da Digital Library in modalità SaaS, progettata per favorire l’integrazione delle APIdi gestione e processamento delle risorse digitali   nei sistemi di produzione del dato delle istituzioni che collaborano con I.PaC. Si rivolge a istituti pubblici e privati che, attraverso widget configurabili, possono gestire direttamente dal proprio ambiente operativo i beni digitali   depositati nell’infrastruttura, utilizzando un’unica interfaccia applicativa.

Progettata secondo l’architettura delle *Single Page Application*, **Teca consente agli operatori di seguire l’intero ciclo di vita del bene digitale**: dalla creazione alla descrizione, dalla modifica all’organizzazione in collezioni, fino alla definizione dei profili di protezione, delle licenze d’uso e dei diritti di accesso in coerenza con le logiche di visibilità previste da I.PaC. I contenuti, strutturati secondo il profilo METS ECO-MiC, possono essere caricati e scaricati mantenendo la piena interoperabilità con i sistemi esterni.

L’applicazione integra funzionalità avanzate di visualizzazione, come media player e streaming player, che abilitano la fruizione diretta dei contenuti multimediali. Gli operatori possono inoltre attivare i servizi di CPA.

Le risorse elaborate possono essere aggregate in collezioni tematiche e organizzate in cartelle *smart*, alimentando una conoscenza computabile e interconnessa, conforme ai principi del :term:`Knowledge as a Service (KaaS)`\ . Teca supporta inoltre la descrizione  dei beni attraverso un modello dati semplificato basato su standard MODS, abilitando l’arricchimento del grafo  multimedialee contribuendo alla costruzione del grafo  cross-dominiodi Ecomic.

A questo scopo, l’interfaccia integra il widget di navigazione dei grafi, che consente l’inserimento e la gestione diretta delle entità connesse alle risorse (es. responsabilità, luoghi, soggetti), facilitando la creazione di nuove relazioni semantiche. Le operazioni attivate vengono trattate come processi asincroni, tracciati e monitorabili tramite una sezione dedicata, che offre una visione chiara dello stato delle attività in corso.

Per la sua architettura modulare, l’aderenza agli standard del PND e l’elevata interoperabilità con l’infrastruttura I.PaC, Teca Multimediale si configura come un componente **strategico di Ecomic**, in grado di supportare istituzioni culturali eterogenee nella gestione sostenibile e valorizzazione del patrimonio digitale, superando la frammentazione informativa e contribuendo attivamente agli obiettivi del Piano Nazionale di Digitalizzazione.

Widget di navigazione dei Grafi
-------------------------------

Tra gli strumenti avanzati messi a disposizione da I.PaC, o richiamabili mediante e-service forniti dall’Infrastruttura, ha notevole rilievo il componente dedicato alla gestione ed esplorazione delle :term:`Super Entità`\ \ . Si tratta di un componente progettato per offrire funzionalità trasversali ai domini e, laddove necessario, progettate ad hoc per esigenze peculiari del singolo Destinatario, anche attraverso micro-fronte dedicati.

Il componente potrà essere integrato nei sistemi di produzione del dato e in Teca Multimediale, allo scopo di supportare gli operatori nelle attività di catalogazione e descrizione, attraverso la ricerca e la cattura dal :term:`grafo di conoscenza <Grafo di conoscenza>`– prima di dominio e poi cross-dominio – di *Authority Record*, riferimenti bibliografici o altre entità di interesse (eventi, luoghi, soggetti, ecc.).

Il componente consente inoltre di validare SuperAuthority (attualmente Agenti) e, in prospettiva, tutte le Super Entità“in attesa di validazione” da parte di I.PaC. In questo modo, l’infrastruttura può ricevere contributi qualificati da esperti del settore, consentendo loro di collaborare attivamente all’aumento della qualità del dato presente e condiviso.

Un’ulteriore funzione del componente riguarda il supporto alla bonifica o integrazione dei dati da parte di sistemi che abbiano I.PaC come “mediatore”.

Tra le funzionalità messe a disposizione si segnalano:

-  ricerca classica (filtri, faccette) e avanzata (integrazione del Graph RAG per query in linguaggio naturale) basata sulla conoscenza I.PaC (grafi di dominio e cross-dominio);

-  validazione di SuperAuthority e, a tendere, di tutte le Super Entità che – a valle di clusterizzazione tramite regole e intelligenza artificiale – richiedano intervento umano (es. luoghi, eventi);

-  cattura e recupero di entità di interesse (identificativi o set di dati) in formato JSON, da inviare ai client aderenti al protocollo L2 (che consente notifiche di aggiornamento, arricchimento dati e sincronizzazione in tempo reale);

-  | azioni sui cluster (ad esempio collegamento o scollegamento di authority presenti | in un cluster);

-  dashboard di monitoraggio dei flussi di clusterizzazione o di altri processi, parametrizzabile, con reportistica di Business Intelligence sulla qualità dei dati, definita in base a metriche e parametri progressivamente individuati.

.. _servizi-generati-dai-percorsi-di-co-design-1:

Servizi generati dai percorsi di co-design
------------------------------------------

I percorsi di co-design attivati tra Digital Library e le Regioni hanno generato anche una serie di servizi gestionali   che rafforzano la capacità degli enti territoriali di governare il ciclo di vita   dei beni digitali. Si tratta di interventi che incidono sulla qualità, coerenza, interoperabilità e sostenibilità dei sistemi informativi locali, creando le condizioni per una gestione più efficace del patrimonio digitale e per l’attivazione di servizi di fruizione avanzati.

Potenziamento della cooperazione dei sistemi di descrizione 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un percorso di co-design ha riguardato il miglioramento dei sistemi di catalogazione esistenti della Regione, con l’obiettivo di accrescerne efficienza, accuratezza e capacità di interoperare con i servizi di Ecomic.

L’intervento ha previsto la progettazione e l’introduzione di un “Hub di Cooperazione” regionale, ossia un punto unico di interazione con i servizi di I.PaC che permette di semplificare e standardizzare le integrazioni e migliorare sicurezza, resilienza e tracciabilità dei flussi informativi.

Parallelamente, sono stati adeguati e potenziati i sistemi locali dedicati alla gestione delle risorse digitali   di biblioteche e archivi, così da attivare direttamente i servizi di CPA e permettere il recupero strutturato delle informazioni utili alla descrizione  dei beni.

In virtù di tali interventi, la Regione dispone ora di un’infrastruttura stabile e interoperabile per la gestione del proprio patrimonio digitale, predisposta per sostenere la futura attivazione di servizi di valorizzazione e fruizione.

Creazione di ambienti unificati di gestione del patrimonio digitale
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Un altro percorso di co-design ha riguardato la necessità di dotarsi di un ambiente in grado di gestire grandi patrimoni eterogenei, così da renderli consultabili attraverso funzionalità avanzate di ricerca.

L’attività ha portato alla progettazione di una nuova Digital Library regionale capace di:

-  raccogliere e organizzare i beni digitali   provenienti da istituti differenti e con patrimoni eterogenei;

-  integrare servizi di DAM e CPA;

-  supportare funzionalità di recupero e normalizzazione di dataset.

Questa soluzione permette all’ente di disporre di strumenti uniformi per l’archiviazione, la gestione e la valorizzazione di patrimoni complessi, assicurando coerenza dei metadati, qualità dei contenuti e interoperabilità con Ecomic.

Evoluzione D.PaC gestione
-------------------------

Digital Library sta progettando una evoluzione di D.PaC in configurazione “gestione”, ossia una piattaforma cloud in modalità Software as a Service (SaaS) pensata per supportare enti culturali di ogni dimensione nella gestione e nella valorizzazione del proprio patrimonio digitale.

D.PaC, nella sua configurazione di gestione, integrerà diversi nuovi componenti, oltre a quello già esistente di Digitalizzazione (l’attuale D.PaC), tra cui:

-  componente descrittivo cross-dominio;

-  componente per la generazione dei metadati METS ECO-MiC, integrato nelle componenti descrittive;

-  teca multimediale con funzionalità di DAM;

-  upload massivo per il caricamento efficiente di contenuti.

D.PaC permetterà così anche a piccoli enti culturali di accedere a una serie di strumenti professionali senza investimenti infrastrutturali, completi di interfacce semplificate per la descrizione  e la gestione autonoma delle collezioni digitali.



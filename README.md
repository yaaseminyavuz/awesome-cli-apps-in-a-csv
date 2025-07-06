# Awesome Command Line (CLI/TUI) Programs [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

This repository - to the best of my knowledge - contains the largest collection of command line (CLI/TUI) tools available in the form of awesome list.
With source information maintained in a handy CSV file.

To contribute, see the [contribution section](#contribute).
Read the instructions before rushing at changing the README file: you must edit the CSV files, not the README!

Some links are available to [related resources](#resources).

Summary:

* Apps/tools: **1775**
* Categories: **78**

# 📚 Contents

- **[ai](#ai)** (37 tools): [AI assistant](#ai-assistant) (1), [AI terminal assistant](#ai-terminal-assistant) (1), [ai assistant](#ai-assistant) (6), [ai chatbot](#ai-chatbot) (1), [ai cli](#ai-cli) (1), [ai toolkit](#ai-toolkit) (1), [ai workflow engine](#ai-workflow-engine) (1), [alibaba scraper](#alibaba-scraper) (1), [autonomous agent](#autonomous-agent) (1), [chatgpt cli](#chatgpt-cli) (6), [chatgpt client](#chatgpt-client) (1), [chatgpt tools](#chatgpt-tools) (3), [chatgpt](#chatgpt) (1), [cli assistant](#cli-assistant) (1), [git tool](#git-tool) (1), [gpt-powered parser](#gpt-powered-parser) (1), [http tools](#http-tools) (1), [llm runner](#llm-runner) (1), [natural language](#natural-language) (1), [ollama client](#ollama-client) (1), [pipeable ai chat](#pipeable-ai-chat) (1), [team knowledge AI](#team-knowledge-ai) (1), [terminal assistant](#terminal-assistant) (2), [terminal ui](#terminal-ui) (1)
- **[animation](#animation)** (33 tools): [AsciiTerminalAnimation](#asciiterminalanimation) (5), [EducationalCryptoVisualizer](#educationalcryptovisualizer) (1), [ImageViewer(ASCII)](#imageviewer(ascii)) (1), [SpinnerCLI](#spinnercli) (1), [ascii animation](#ascii-animation) (6), [ascii art](#ascii-art) (1), [ascii effects](#ascii-effects) (1), [ascii renderer](#ascii-renderer) (3), [ascii tree generator](#ascii-tree-generator) (1), [cli clocks](#cli-clocks) (1), [enhanced cat](#enhanced-cat) (2), [maze generator](#maze-generator) (1), [simulation](#simulation) (1), [terminal animation](#terminal-animation) (6), [terminal fun](#terminal-fun) (1), [text effects](#text-effects) (1)
- **[backup](#backup)** (19 tools): [AlternativeVCS](#alternativevcs) (2), [BackupAutomationWrapper](#backupautomationwrapper) (1), [EncryptedBackupCLI](#encryptedbackupcli) (1), [EncryptedBackupTool](#encryptedbackuptool) (1), [GpgCompressedBackupTool](#gpgcompressedbackuptool) (1), [PaperBarcodeBackup](#paperbarcodebackup) (1), [ShellSyncBackup](#shellsyncbackup) (1), [backup tool](#backup-tool) (3), [cli backup](#cli-backup) (1), [git backup](#git-backup) (1), [git-based backup](#git-based-backup) (1), [network backup](#network-backup) (1), [restic config](#restic-config) (1), [restic wrapper](#restic-wrapper) (1), [thread archiver](#thread-archiver) (1), [workspace backup](#workspace-backup) (1)
- **[browser](#browser)** (19 tools): [FastFindAlternative](#fastfindalternative) (1), [FuzzyFinderPlugin](#fuzzyfinderplugin) (1), [GeminiClientTUI](#geminiclienttui) (2), [PlaceSearchCLI](#placesearchcli) (1), [StatusSyncCLI](#statussynccli) (1), [TerminalBrowserTUI](#terminalbrowsertui) (1), [TerminalWebBrowser](#terminalwebbrowser) (4), [TextBasedWebBrowser](#textbasedwebbrowser) (1), [WebSearchCLI](#websearchcli) (1), [arXivSearcher](#arxivsearcher) (1), [console sharing](#console-sharing) (1), [fuzzy‑search](#fuzzy‑search) (1), [rss reader](#rss-reader) (1), [text browser](#text-browser) (1), [web browser](#web-browser) (1)
- **[calc](#calc)** (18 tools): [AdvancedCalculators](#advancedcalculators) (1), [MathCLI](#mathcli) (1), [StorageCalculatorCLI](#storagecalculatorcli) (1), [TerminalCalculator](#terminalcalculator) (1), [TimeDiffCalculatorCLI](#timediffcalculatorcli) (1), [bitwise tools](#bitwise-tools) (1), [calculator](#calculator) (8), [calculators](#calculators) (1), [expression calc](#expression-calc) (1), [math engine](#math-engine) (1), [programmer tools](#programmer-tools) (1)
- **[cd](#cd)** (23 tools): [FastCdTool](#fastcdtool) (1), [ShellSyncBackup](#shellsyncbackup) (1), [SmartDirectoryNavigatorCLI](#smartdirectorynavigatorcli) (1), [TerminalFileManager](#terminalfilemanager) (1), [cd enhancement](#cd-enhancement) (1), [cd enhancer](#cd-enhancer) (2), [cd tool](#cd-tool) (1), [directory jumper](#directory-jumper) (2), [directory jumpers](#directory-jumpers) (2), [directory switcher](#directory-switcher) (1), [enhanced cat](#enhanced-cat) (3), [file browser](#file-browser) (1), [navigation tools](#navigation-tools) (1), [path manager](#path-manager) (1), [project switchers](#project-switchers) (1), [shell completion](#shell-completion) (1), [shell](#shell) (2)
- **[chat](#chat)** (36 tools): [RedditClientTUI](#redditclienttui) (1), [SSHChatServerCLI](#sshchatservercli) (1), [TerminalIRCClient](#terminalircclient) (1), [TerminalMessenger](#terminalmessenger) (3), [TerminalTwitterClient](#terminaltwitterclient) (1), [bbs client](#bbs-client) (1), [chat clients](#chat-clients) (1), [chat over ssh](#chat-over-ssh) (1), [chat](#chat) (1), [decentralized chat](#decentralized-chat) (1), [discord client](#discord-client) (1), [fediverse client](#fediverse-client) (1), [irc client](#irc-client) (2), [mastodon client](#mastodon-client) (1), [matrix client](#matrix-client) (5), [messaging](#messaging) (2), [notification tools](#notification-tools) (1), [signal client](#signal-client) (1), [social clients](#social-clients) (1), [telegram client](#telegram-client) (1), [terminal sharing](#terminal-sharing) (1), [tox client](#tox-client) (1), [twitch clients](#twitch-clients) (1), [twitch tools](#twitch-tools) (1), [xmpp client](#xmpp-client) (4)
- **[cheatsheet](#cheatsheet)** (27 tools): [AliasGeneratorCLI](#aliasgeneratorcli) (1), [CommandExplainerCLI](#commandexplainercli) (1), [FastFindAlternative](#fastfindalternative) (2), [InteractiveCheatsheetCLI](#interactivecheatsheetcli) (1), [TerminalHelpFetcher](#terminalhelpfetcher) (1), [autocomplete](#autocomplete) (2), [cheatsheets](#cheatsheets) (1), [cli assistant](#cli-assistant) (1), [command correctors](#command-correctors) (1), [command history](#command-history) (1), [command-line translator](#command-line-translator) (1), [devops notebook runner](#devops-notebook-runner) (1), [enhanced cat](#enhanced-cat) (1), [fuzzy finder](#fuzzy-finder) (1), [fzf cheatsheet](#fzf-cheatsheet) (1), [fzf tools](#fzf-tools) (1), [knowledge base](#knowledge-base) (1), [manuals](#manuals) (1), [script launcher](#script-launcher) (1), [snippet manager](#snippet-manager) (5), [table generator](#table-generator) (1)
- **[conversion](#conversion)** (16 tools): [DataFormatConverterCLI](#dataformatconvertercli) (1), [MultiFormatDocumentConverter](#multiformatdocumentconverter) (1), [Translation](#translation) (1), [WordToTextConverter](#wordtotextconverter) (2), [audio tools](#audio-tools) (1), [css tools](#css-tools) (1), [data automation](#data-automation) (1), [doc extractor](#doc-extractor) (1), [doc viewer](#doc-viewer) (1), [document converter](#document-converter) (2), [file conversion](#file-conversion) (1), [format converters](#format-converters) (1), [pdf converter](#pdf-converter) (1), [resume tools](#resume-tools) (1)
- **[copilot](#copilot)** (11 tools): [AI assistant](#ai-assistant) (1), [ai assistant](#ai-assistant) (1), [ai coding assistant](#ai-coding-assistant) (1), [chatgpt cli](#chatgpt-cli) (1), [chatgpt](#chatgpt) (1), [copilot](#copilot) (1), [gpt assistant](#gpt-assistant) (1), [gpt cli](#gpt-cli) (1), [llama cli](#llama-cli) (1), [shell assistant](#shell-assistant) (1), [shell](#shell) (1)
- **[data-management](#data-management)** (16 tools): [APIReaderCLI](#apireadercli) (1), [AsciiChartCLI](#asciichartcli) (1), [DataQueryCLI](#dataquerycli) (1), [DateTimeProcessingCLI](#datetimeprocessingcli) (1), [RedisViewerTUI](#redisviewertui) (1), [TerminalDataVisualizer](#terminaldatavisualizer) (1), [TextDatabaseCLI](#textdatabasecli) (1), [command-line translator](#command-line-translator) (1), [data processing](#data-processing) (1), [database client](#database-client) (1), [dataset generator](#dataset-generator) (1), [enhanced cat](#enhanced-cat) (1), [process monitor](#process-monitor) (1), [shell](#shell) (1), [terminal dashboard](#terminal-dashboard) (1), [terminal sharing](#terminal-sharing) (1)
- **[data-management-json](#data-management-json)** (44 tools): [ImageViewer(ASCII)](#imageviewer(ascii)) (1), [JSONInspector](#jsoninspector) (1), [JSONTransformerCLI](#jsontransformercli) (1), [JSONViewerTUI](#jsonviewertui) (1), [advanced grep](#advanced-grep) (2), [cli scripting](#cli-scripting) (1), [command-line translator](#command-line-translator) (5), [enhanced cat](#enhanced-cat) (2), [format converter](#format-converter) (1), [json editor](#json-editor) (2), [json filter](#json-filter) (1), [json formatter](#json-formatter) (3), [json generator](#json-generator) (1), [json parser](#json-parser) (1), [json processor](#json-processor) (2), [json processors](#json-processors) (1), [json query tools](#json-query-tools) (1), [json query](#json-query) (1), [json search](#json-search) (1), [json table](#json-table) (1), [json toolkit](#json-toolkit) (1), [json tools](#json-tools) (3), [json viewer](#json-viewer) (1), [json viewers](#json-viewers) (1), [json-processing](#json-processing) (2), [json-yaml converter](#json-yaml-converter) (1), [record analysis](#record-analysis) (1), [shell](#shell) (2), [task management](#task-management) (1), [yaml tools](#yaml-tools) (1)
- **[data-management-tabular](#data-management-tabular)** (30 tools): [CSVProcessingCLI](#csvprocessingcli) (1), [CSVProcessorCLI](#csvprocessorcli) (1), [CSVQueryCLI](#csvquerycli) (1), [DatabaseManagerTUI](#databasemanagertui) (1), [GitStatistics](#gitstatistics) (1), [SQLClientCLI](#sqlclientcli) (3), [SQLGitDatabase](#sqlgitdatabase) (1), [TSVProcessingCLI](#tsvprocessingcli) (1), [TabularDataTUI](#tabulardatatui) (1), [cli client](#cli-client) (1), [command-line translator](#command-line-translator) (2), [csv tool](#csv-tool) (1), [csv tools](#csv-tools) (3), [csv viewer](#csv-viewer) (2), [database manager](#database-manager) (2), [enhanced cat](#enhanced-cat) (1), [json-processing](#json-processing) (1), [sql tools](#sql-tools) (1), [sql tui](#sql-tui) (1), [sql-on-csv](#sql-on-csv) (1), [sqlite client](#sqlite-client) (1), [sqlite server](#sqlite-server) (1), [sqlite](#sqlite) (1)
- **[devops](#devops)** (8 tools): [DevEnvironmentManager](#devenvironmentmanager) (1), [aws cli](#aws-cli) (1), [build tools](#build-tools) (1), [cloud clients](#cloud-clients) (1), [kubectl context switcher](#kubectl-context-switcher) (1), [kubernetes log viewer](#kubernetes-log-viewer) (1), [kubernetes](#kubernetes) (1), [unikernel](#unikernel) (1)
- **[diff](#diff)** (11 tools): [AlternativeVCS](#alternativevcs) (1), [GitStatistics](#gitstatistics) (1), [PDFDiffTool](#pdfdifftool) (1), [csv comparison](#csv-comparison) (1), [diff visualizer](#diff-visualizer) (1), [directory diff](#directory-diff) (1), [enhanced cat](#enhanced-cat) (3), [string distance](#string-distance) (1), [yaml diff](#yaml-diff) (1)
- **[disk-analyzer](#disk-analyzer)** (12 tools): [DiskAnalyzerTUI](#diskanalyzertui) (1), [DiskUsageHistogram](#diskusagehistogram) (1), [FastFindAlternative](#fastfindalternative) (2), [NcursesDiskAnalyzer](#ncursesdiskanalyzer) (2), [StylizedDiskUsageReporter](#stylizeddiskusagereporter) (6)
- **[editors](#editors)** (27 tools): [NoteTakingTUI](#notetakingtui) (1), [TUIEditor](#tuieditor) (1), [TerminalEditor](#terminaleditor) (1), [TerminalTextEditor](#terminaltexteditor) (2), [TextEditorTUI](#texteditortui) (2), [advanced-extensible](#advanced-extensible) (1), [gui-easy-editor](#gui-easy-editor) (5), [gui-sublime-inspired](#gui-sublime-inspired) (1), [lightweight-stable](#lightweight-stable) (1), [lightweight-userfriendly](#lightweight-userfriendly) (1), [line editor](#line-editor) (1), [minimalist-writing](#minimalist-writing) (1), [modal-powerful](#modal-powerful) (1), [modal-traditional](#modal-traditional) (1), [modern-nano-like](#modern-nano-like) (1), [neovim frontend](#neovim-frontend) (1), [text editor](#text-editor) (3), [vim-inspired-minimal](#vim-inspired-minimal) (1), [vim-like-lightweight](#vim-like-lightweight) (1)
- **[email](#email)** (18 tools): [EmailGeneratorCLI](#emailgeneratorcli) (1), [MailSyncTool](#mailsynctool) (1), [TemporaryEmailCLI](#temporaryemailcli) (1), [TerminalEmailClient](#terminalemailclient) (5), [cli email](#cli-email) (1), [disposable email](#disposable-email) (1), [email alias manager](#email-alias-manager) (1), [email analyzer](#email-analyzer) (1), [email client](#email-client) (3), [email tools](#email-tools) (1), [resource monitor](#resource-monitor) (1), [slack mail interface](#slack-mail-interface) (1)
- **[file-dir-cleanup](#file-dir-cleanup)** (13 tools): [DirectoryOrganizer](#directoryorganizer) (1), [DuplicateFileFinder](#duplicatefilefinder) (1), [FilenameSanitizer](#filenamesanitizer) (1), [ModernFileManager](#modernfilemanager) (1), [deduplication](#deduplication) (1), [directory organizer](#directory-organizer) (1), [duplicate finder](#duplicate-finder) (1), [file cleanup](#file-cleanup) (1), [file deduplication](#file-deduplication) (1), [file organizers](#file-organizers) (1), [folder organizer](#folder-organizer) (1), [gamified file manager](#gamified-file-manager) (1), [metadata remover](#metadata-remover) (1)
- **[file-explorer](#file-explorer)** (11 tools): [DirectoryTreePrinter](#directorytreeprinter) (1), [ModernFileManager](#modernfilemanager) (2), [directory viewers](#directory-viewers) (1), [enhanced cat](#enhanced-cat) (1), [file browser](#file-browser) (1), [file explorer](#file-explorer) (1), [file manager](#file-manager) (2), [terminal file explorer](#terminal-file-explorer) (1), [tui file explorer](#tui-file-explorer) (1)
- **[file-handling](#file-handling)** (28 tools): [ArchiveAutoExtractor](#archiveautoextractor) (1), [FileInspectorCLI](#fileinspectorcli) (1), [ModernFileManager](#modernfilemanager) (1), [ProgressCopyTool](#progresscopytool) (1), [ShellSyncBackup](#shellsyncbackup) (1), [TemporaryPasteCLI](#temporarypastecli) (1), [archive manager](#archive-manager) (1), [cloud storage](#cloud-storage) (1), [compression](#compression) (1), [copy progress monitor](#copy-progress-monitor) (1), [directory visualizer](#directory-visualizer) (1), [downloads organizer](#downloads-organizer) (1), [enhanced cat](#enhanced-cat) (2), [file deployer](#file-deployer) (1), [file permissions](#file-permissions) (1), [file transfer](#file-transfer) (1), [file utilities](#file-utilities) (1), [filesystem sandbox](#filesystem-sandbox) (1), [filesystem tools](#filesystem-tools) (1), [gui-easy-editor](#gui-easy-editor) (1), [library browser](#library-browser) (1), [log management](#log-management) (1), [media streamer](#media-streamer) (1), [shell](#shell) (1), [symlink tools](#symlink-tools) (1), [system monitor](#system-monitor) (1), [vcs client](#vcs-client) (1)
- **[file-manager](#file-manager)** (22 tools): [DualPaneFileManager](#dualpanefilemanager) (1), [LightweightFileManager](#lightweightfilemanager) (2), [ModalFileManager](#modalfilemanager) (1), [ModernFileManager](#modernfilemanager) (8), [TerminalFileManager](#terminalfilemanager) (1), [ViKeybindingsFileManager](#vikeybindingsfilemanager) (1), [VisualFileManager](#visualfilemanager) (1), [file manager](#file-manager) (2), [project manager](#project-manager) (1), [shell](#shell) (1), [terminal file manager](#terminal-file-manager) (2), [terminal file managers](#terminal-file-managers) (1)
- **[file-renamer](#file-renamer)** (14 tools): [BulkRenamerCLI](#bulkrenamercli) (2), [BulkRenamer](#bulkrenamer) (1), [InteractiveRenamer](#interactiverenamer) (1), [Translation](#translation) (1), [enhanced cat](#enhanced-cat) (1), [file manager](#file-manager) (1), [file renamer](#file-renamer) (1), [file renamers](#file-renamers) (1), [gui-easy-editor](#gui-easy-editor) (2), [image renamer](#image-renamer) (1), [music file tools](#music-file-tools) (1), [search tools](#search-tools) (1)
- **[file-system](#file-system)** (4 tools): [FileTaggerCLI](#filetaggercli) (1), [RemoteFilesystemMounting](#remotefilesystemmounting) (1), [TagBasedVirtualFS](#tagbasedvirtualfs) (1), [deployment tools](#deployment-tools) (1)
- **[file-watch](#file-watch)** (7 tools): [DirectoryWatcher](#directorywatcher) (1), [FileWatcherCLI](#filewatchercli) (1), [ProcessMonitorTUI](#processmonitortui) (1), [ShellSyncBackup](#shellsyncbackup) (1), [file monitor](#file-monitor) (1), [file watcher](#file-watcher) (1), [file watchers](#file-watchers) (1)
- **[financial](#financial)** (17 tools): [AccountingCLI](#accountingcli) (1), [Accounting](#accounting) (2), [CloudSyncManager](#cloudsyncmanager) (1), [CryptoTUI](#cryptotui) (1), [FinanceCLI](#financecli) (2), [TerminalFinanceTracker](#terminalfinancetracker) (1), [accounting](#accounting) (1), [bitcoin cli](#bitcoin-cli) (1), [budget tracking](#budget-tracking) (1), [currency converters](#currency-converters) (2), [enhanced cat](#enhanced-cat) (1), [exchange rates](#exchange-rates) (1), [invoice generator](#invoice-generator) (1), [log viewer](#log-viewer) (1)
- **[find](#find)** (8 tools): [FastFileLocator](#fastfilelocator) (1), [FastFindAlternative](#fastfindalternative) (1), [enhanced cat](#enhanced-cat) (1), [file finder](#file-finder) (1), [file search](#file-search) (1), [fuzzy finders](#fuzzy-finders) (1), [fuzzy‑search](#fuzzy‑search) (1), [grep alternative](#grep-alternative) (1)
- **[flashcard](#flashcard)** (10 tools): [FlashcardTrainerTUI](#flashcardtrainertui) (2), [anki tool](#anki-tool) (1), [cli learning tools](#cli-learning-tools) (1), [flashcard tool](#flashcard-tool) (1), [flashcard tools](#flashcard-tools) (1), [flashcards](#flashcards) (2), [nextcloud tool](#nextcloud-tool) (1), [vocabulary trainer](#vocabulary-trainer) (1)
- **[font](#font)** (4 tools): [ascii art](#ascii-art) (1), [ascii-text-rendering](#ascii-text-rendering) (1), [font manager](#font-manager) (1), [visual-effects-rendering](#visual-effects-rendering) (1)
- **[funny](#funny)** (18 tools): [AsciiSpeechGenerato](#asciispeechgenerato) (1), [AsciiSpeechGenerator](#asciispeechgenerator) (1), [EmojiPickerCLI](#emojipickercli) (1), [FunCLI](#funcli) (1), [MatrixVideoConfCLI](#matrixvideoconfcli) (1), [PokemonFetcherCLI](#pokemonfetchercli) (1), [QuoteGeneratorCLI](#quotegeneratorcli) (1), [cli fun](#cli-fun) (2), [enhanced cat](#enhanced-cat) (1), [fun / novelty](#fun-novelty) (1), [fun](#fun) (2), [funny aliases](#funny-aliases) (1), [funny tools](#funny-tools) (1), [terminal animation](#terminal-animation) (1), [terminal drawing tool](#terminal-drawing-tool) (1), [text decoration](#text-decoration) (1)
- **[games](#games)** (62 tools): [APIClientCLI](#apiclientcli) (1), [AdvancedCalculators](#advancedcalculators) (1), [GameCLI](#gamecli) (4), [GameTUI](#gametui) (1), [TUI RogueGame](#tui-roguegame) (1), [TerminalBoardGames](#terminalboardgames) (1), [TerminalChessAI](#terminalchessai) (1), [TerminalGame(Minesweeper)](#terminalgame(minesweeper)) (1), [TerminalGame(PuzzlePlatformer)](#terminalgame(puzzleplatformer)) (1), [TerminalGame(Roguelike)](#terminalgame(roguelike)) (1), [TerminalGame(SimulationStrategy)](#terminalgame(simulationstrategy)) (1), [TerminalGame(SurvivalRPG)](#terminalgame(survivalrpg)) (1), [TerminalGame(Tetris)](#terminalgame(tetris)) (1), [TerminalGameCLI](#terminalgamecli) (1), [TerminalGameTUI](#terminalgametui) (2), [TerminalGame](#terminalgame) (5), [WordleGameTUI](#wordlegametui) (1), [ascii fps game](#ascii-fps-game) (1), [chess](#chess) (1), [cli game](#cli-game) (3), [enhanced cat](#enhanced-cat) (2), [game editor](#game-editor) (1), [game](#game) (4), [interactive fiction](#interactive-fiction) (1), [irc bot game](#irc-bot-game) (1), [minesweeper](#minesweeper) (1), [puzzle game](#puzzle-game) (1), [shell](#shell) (1), [terminal chess](#terminal-chess) (1), [terminal game](#terminal-game) (12), [terminal games](#terminal-games) (3), [tetris game](#tetris-game) (1), [tui chess client](#tui-chess-client) (1), [word games](#word-games) (1), [wordle solver](#wordle-solver) (1)
- **[git](#git)** (62 tools): [AlternativeVCS](#alternativevcs) (1), [CloudSyncManager](#cloudsyncmanager) (1), [CommitHelperCLI](#commithelpercli) (1), [CommitMessageHelperCLI](#commitmessagehelpercli) (1), [DistributedVersionControl](#distributedversioncontrol) (1), [GitEnhancerCLI](#gitenhancercli) (1), [GitFzfCLI](#gitfzfcli) (1), [GitInterface(TUI)](#gitinterface(tui)) (2), [GitRemoteHelperCLI](#gitremotehelpercli) (1), [GitRepoManagerCLI](#gitrepomanagercli) (1), [GitSearchCLI](#gitsearchcli) (1), [GitSecretManagerCLI](#gitsecretmanagercli) (1), [GitServerTUI](#gitservertui) (1), [GitStatisticsCLI](#gitstatisticscli) (1), [GitStatistics](#gitstatistics) (9), [GitTUIWrapper](#gittuiwrapper) (1), [GitVisualizerCLI](#gitvisualizercli) (1), [GitforLargeFiles](#gitforlargefiles) (1), [SelfHostedGitServer](#selfhostedgitserver) (1), [cd helper](#cd-helper) (1), [changelog tools](#changelog-tools) (1), [dotfiles manager](#dotfiles-manager) (1), [enhanced cat](#enhanced-cat) (3), [git TUI tools](#git-tui-tools) (1), [git analytics](#git-analytics) (1), [git assistant](#git-assistant) (1), [git automation](#git-automation) (1), [git autosync](#git-autosync) (1), [git clients](#git-clients) (1), [git commit tools](#git-commit-tools) (1), [git diff viewer](#git-diff-viewer) (2), [git export](#git-export) (1), [git helper](#git-helper) (2), [git helpers](#git-helpers) (2), [git hook](#git-hook) (1), [git profile](#git-profile) (1), [git tool](#git-tool) (2), [git tools](#git-tools) (3), [git tui](#git-tui) (1), [github dashboard](#github-dashboard) (1), [github graph](#github-graph) (1), [github prs tracker](#github-prs-tracker) (1), [repo cleaner](#repo-cleaner) (1), [secret scanner](#secret-scanner) (1), [sourcehut git client](#sourcehut-git-client) (1)
- **[graphics](#graphics)** (45 tools): [BackupAutomationWrapper](#backupautomationwrapper) (1), [ColorToolCLI](#colortoolcli) (1), [FractalCLI](#fractalcli) (1), [ImageEditingConversion](#imageeditingconversion) (1), [ImageProcessorCLI](#imageprocessorcli) (1), [ImageToASCII](#imagetoascii) (1), [ImageViewer(ASCII)](#imageviewer(ascii)) (6), [SVGSlideExporterCLI](#svgslideexportercli) (1), [ScreenshotUtility](#screenshotutility) (1), [ai image search](#ai-image-search) (1), [ascii art](#ascii-art) (2), [ascii diagram](#ascii-diagram) (1), [ascii paint](#ascii-paint) (1), [ascii renderer](#ascii-renderer) (1), [ascii screenshot tool](#ascii-screenshot-tool) (1), [barcode scanner](#barcode-scanner) (1), [color picker](#color-picker) (1), [command-line translator](#command-line-translator) (2), [diagram scripting](#diagram-scripting) (1), [enhanced cat](#enhanced-cat) (1), [gif editors](#gif-editors) (1), [gif tools](#gif-tools) (1), [graph visualization](#graph-visualization) (1), [image optimizer](#image-optimizer) (1), [image preview](#image-preview) (1), [image processing](#image-processing) (1), [image tool](#image-tool) (1), [map viewers](#map-viewers) (1), [maps](#maps) (1), [meme generator](#meme-generator) (1), [screenshot decorators](#screenshot-decorators) (1), [screenshot tools](#screenshot-tools) (1), [space visualizer](#space-visualizer) (1), [svg color modifier](#svg-color-modifier) (1), [svg optimizers](#svg-optimizers) (1), [syntax highlighting](#syntax-highlighting) (1), [terminal image](#terminal-image) (1), [terrain generator](#terrain-generator) (1)
- **[history](#history)** (4 tools): [command-line translator](#command-line-translator) (1), [history manager](#history-manager) (2), [productivity](#productivity) (1)
- **[launcher](#launcher)** (23 tools): [ApplicationLauncherTUI](#applicationlaunchertui) (1), [CLI task runner](#cli-task-runner) (1), [CommandOrchestratorCLI](#commandorchestratorcli) (1), [FileWatcherCLI](#filewatchercli) (1), [MultiCommandRunnerTUI](#multicommandrunnertui) (2), [app launcher](#app-launcher) (1), [batch queue](#batch-queue) (1), [build tool](#build-tool) (1), [command palette](#command-palette) (1), [file watchers](#file-watchers) (1), [launcher](#launcher) (4), [parallel execution](#parallel-execution) (1), [shell launcher](#shell-launcher) (1), [shell](#shell) (2), [task manager](#task-manager) (1), [task runner](#task-runner) (2), [vagrant helper](#vagrant-helper) (1)
- **[ls](#ls)** (10 tools): [EnhancedLsRewrite](#enhancedlsrewrite) (1), [GitStatistics](#gitstatistics) (1), [ModernFileManager](#modernfilemanager) (1), [RustLsReplacement](#rustlsreplacement) (3), [enhanced cat](#enhanced-cat) (1), [ls color tool](#ls-color-tool) (1), [ls color](#ls-color) (1), [tree viewer](#tree-viewer) (1)
- **[markdown](#markdown)** (10 tools): [MarkdownBookBuilder](#markdownbookbuilder) (1), [MarkdownTUI](#markdowntui) (1), [MarkdownViewer(GUI/CLI)](#markdownviewer(gui-cli)) (1), [knowledge base](#knowledge-base) (1), [markdown parser](#markdown-parser) (1), [markdown preview](#markdown-preview) (1), [markdown tool](#markdown-tool) (1), [markdown tools](#markdown-tools) (1), [markdown viewer](#markdown-viewer) (2)
- **[monitor](#monitor)** (36 tools): [BenchmarkCLI](#benchmarkcli) (1), [DiskInspectorCLI](#diskinspectorcli) (1), [IO monitor](#io-monitor) (1), [ImageViewer(ASCII)](#imageviewer(ascii)) (2), [LogViewerTUI](#logviewertui) (1), [SystemHardwareInspector](#systemhardwareinspector) (1), [battery monitor](#battery-monitor) (1), [load monitor](#load-monitor) (1), [log viewer](#log-viewer) (1), [memory usage](#memory-usage) (1), [monitoring](#monitoring) (1), [neofetch](#neofetch) (1), [network grep](#network-grep) (1), [network scanner](#network-scanner) (1), [packet analyzer](#packet-analyzer) (1), [power monitor](#power-monitor) (1), [ram info](#ram-info) (1), [resource monitor](#resource-monitor) (4), [serial monitor](#serial-monitor) (1), [syscall monitor](#syscall-monitor) (1), [system fetcher](#system-fetcher) (3), [system info](#system-info) (5), [system information](#system-information) (1), [system monitor](#system-monitor) (2), [terminal sharing](#terminal-sharing) (1)
- **[monitor-top](#monitor-top)** (26 tools): [FastFindAlternative](#fastfindalternative) (1), [IO monitor](#io-monitor) (1), [ResourceMonitorTUI](#resourcemonitortui) (1), [gpu monitor](#gpu-monitor) (4), [process monitor](#process-monitor) (2), [process viewer,](#process-viewer,) (1), [process viewer](#process-viewer) (2), [resource monitor](#resource-monitor) (7), [system monitor](#system-monitor) (6), [task manager](#task-manager) (1)
- **[music](#music)** (55 tools): [AudioMixerCLI](#audiomixercli) (1), [AudioMixer](#audiomixer) (1), [LightweightAudioPlayer](#lightweightaudioplayer) (19), [MusicAppFramework](#musicappframework) (1), [MusicDownloaderCLI](#musicdownloadercli) (1), [MusicLibraryManager](#musiclibrarymanager) (1), [PodcastClientTUI](#podcastclienttui) (1), [SpotifyClientTUI](#spotifyclienttui) (1), [TerminalAudioPlayer(ogg)](#terminalaudioplayer(ogg)) (1), [TerminalMusicPlayer(MPD)](#terminalmusicplayer(mpd)) (1), [TerminalMusicPlayer](#terminalmusicplayer) (1), [TerminalMusicVisualizer](#terminalmusicvisualizer) (1), [TextToSpeech](#texttospeech) (1), [YouTubeAudioCLI](#youtubeaudiocli) (1), [YouTubeToMP3Downloader](#youtubetomp3downloader) (1), [audio player](#audio-player) (3), [audio visualizer](#audio-visualizer) (1), [audiobook manager](#audiobook-manager) (1), [cli midi](#cli-midi) (1), [cli music player](#cli-music-player) (1), [debugging](#debugging) (1), [media control](#media-control) (1), [music catalog](#music-catalog) (1), [music player](#music-player) (5), [music scraper](#music-scraper) (1), [music theory](#music-theory) (1), [podcast downloader](#podcast-downloader) (1), [podcast ui for newsboat](#podcast-ui-for-newsboat) (1), [radio player](#radio-player) (1), [spotify client](#spotify-client) (1), [youtube client](#youtube-client) (1)
- **[networking](#networking)** (82 tools): [BluetoothManagerTUI](#bluetoothmanagertui) (1), [HTTPSProxyAnalyzer](#httpsproxyanalyzer) (1), [ListManagerCLI](#listmanagercli) (1), [NetworkToolCLI](#networktoolcli) (1), [NetworkTrafficMonitor](#networktrafficmonitor) (1), [OpenAPIEditorCLI](#openapieditorcli) (1), [RedditClientTUI](#redditclienttui) (1), [SpeedTestCLI](#speedtestcli) (1), [ad blocker](#ad-blocker) (1), [api client](#api-client) (1), [bandwidth monitor](#bandwidth-monitor) (1), [bluetooth tool](#bluetooth-tool) (1), [cli-to-web](#cli-to-web) (1), [debugging](#debugging) (1), [dns client](#dns-client) (1), [dns tools](#dns-tools) (2), [file manager](#file-manager) (1), [file‑sharing](#file‑sharing) (1), [grpc client](#grpc-client) (1), [http client](#http-client) (2), [http proxy](#http-proxy) (1), [ip generator](#ip-generator) (1), [ip geolocation](#ip-geolocation) (1), [kubectl port forwarder](#kubectl-port-forwarder) (1), [load testing](#load-testing) (1), [log analyzer](#log-analyzer) (1), [mock server](#mock-server) (1), [monitoring](#monitoring) (1), [network diagnostics](#network-diagnostics) (1), [network info](#network-info) (1), [network interface info](#network-interface-info) (1), [network monitor](#network-monitor) (3), [network proxy](#network-proxy) (1), [network scanner](#network-scanner) (2), [network tools](#network-tools) (2), [network traffic viewer](#network-traffic-viewer) (1), [oauth manager](#oauth-manager) (1), [packet sender](#packet-sender) (1), [parallel ssh tools](#parallel-ssh-tools) (1), [proxy tool](#proxy-tool) (1), [reconnaissance](#reconnaissance) (1), [remote shells](#remote-shells) (1), [remote terminal server](#remote-terminal-server) (1), [shell](#shell) (2), [sip analyzer](#sip-analyzer) (1), [smb tools](#smb-tools) (1), [socket monitor](#socket-monitor) (1), [ssh file transfer client](#ssh-file-transfer-client) (1), [ssh manager](#ssh-manager) (2), [ssh tools](#ssh-tools) (3), [static server](#static-server) (1), [subnetting tools](#subnetting-tools) (1), [system information](#system-information) (1), [tcp client](#tcp-client) (1), [terminal API client](#terminal-api-client) (1), [terminal sharing](#terminal-sharing) (5), [tunnelCLI / port forwarder](#tunnelcli-port-forwarder) (1), [tunneling](#tunneling) (1), [vpn tools](#vpn-tools) (2), [vpn](#vpn) (1), [web server](#web-server) (2), [web tools](#web-tools) (1), [websocket](#websocket) (1), [wifi manager](#wifi-manager) (1), [xmpp server](#xmpp-server) (2)
- **[note-taking](#note-taking)** (29 tools): [CLIJournal](#clijournal) (1), [EvernoteClientCLI](#evernoteclientcli) (1), [NoteTakingCLI](#notetakingcli) (3), [NoteTakingTUI](#notetakingtui) (1), [NotesCLI](#notescli) (1), [TerminalKnowledgeBase](#terminalknowledgebase) (1), [calendar & notes](#calendar-&-notes) (1), [cli kanban notes](#cli-kanban-notes) (1), [command-line translator](#command-line-translator) (1), [journal](#journal) (2), [knowledge base](#knowledge-base) (4), [markdown viewer](#markdown-viewer) (1), [note taking](#note-taking) (2), [note-taking](#note-taking) (5), [terminal journal](#terminal-journal) (1), [terminal notes](#terminal-notes) (1), [terminal sharing](#terminal-sharing) (2)
- **[office](#office)** (19 tools): [MarkdownPresenterTUI](#markdownpresentertui) (1), [PlaintextPresenterCLI](#plaintextpresentercli) (1), [TerminalPresentation](#terminalpresentation) (1), [calculator](#calculator) (1), [cli presentation](#cli-presentation) (1), [code tutorial](#code-tutorial) (1), [enhanced cat](#enhanced-cat) (1), [form sharing](#form-sharing) (1), [markdown slides](#markdown-slides) (1), [pdf tools](#pdf-tools) (2), [presentation tool](#presentation-tool) (1), [presentation tools](#presentation-tools) (2), [presentations](#presentations) (1), [search tool](#search-tool) (1), [spreadsheet calculator](#spreadsheet-calculator) (1), [terminal presentation](#terminal-presentation) (1), [terminal spreadsheet](#terminal-spreadsheet) (1)
- **[online](#online)** (26 tools): [ArchWikiCLI](#archwikicli) (1), [CLICatalog](#clicatalog) (1), [GoogleSearchCLI](#googlesearchcli) (1), [StackOverflowCLI](#stackoverflowcli) (1), [StackOverflowSearchCLI](#stackoverflowsearchcli) (1), [WikipediaCLI](#wikipediacli) (1), [awesome list tools](#awesome-list-tools) (1), [command-line translator](#command-line-translator) (1), [fuzzy finder](#fuzzy-finder) (1), [git tool](#git-tool) (1), [github tools](#github-tools) (1), [hackernews tracker](#hackernews-tracker) (1), [jira tools](#jira-tools) (2), [output sharing tools](#output-sharing-tools) (1), [read-later tools](#read-later-tools) (1), [recipe tools](#recipe-tools) (1), [reddit cleaner](#reddit-cleaner) (1), [subdomain finder](#subdomain-finder) (1), [terminal messaging](#terminal-messaging) (1), [terminal sharing](#terminal-sharing) (1), [username/email availability checker](#username-email-availability-checker) (1), [vcs performance](#vcs-performance) (1), [web scraper](#web-scraper) (1), [wikipedia client](#wikipedia-client) (2)
- **[option-picker](#option-picker)** (17 tools): [TerminalMenu](#terminalmenu) (1), [date picker](#date-picker) (1), [enhanced cat](#enhanced-cat) (2), [file search](#file-search) (1), [fuzzy finder](#fuzzy-finder) (1), [fuzzy selector](#fuzzy-selector) (1), [fuzzy-filter](#fuzzy-filter) (1), [fuzzy‑search](#fuzzy‑search) (1), [fzf selector](#fzf-selector) (1), [interactive selector](#interactive-selector) (1), [interactive-line-select](#interactive-line-select) (1), [menu builder](#menu-builder) (1), [menu tools](#menu-tools) (1), [menu](#menu) (1), [shell](#shell) (2)
- **[organizers](#organizers)** (22 tools): [EmailSenderCLI](#emailsendercli) (1), [GoogleContactsCLI](#googlecontactscli) (1), [TerminalCalendarTasker](#terminalcalendartasker) (1), [TimezoneCLI](#timezonecli) (1), [caldav calendar](#caldav-calendar) (2), [calendar sync tools](#calendar-sync-tools) (1), [calendar tools](#calendar-tools) (2), [calendar](#calendar) (2), [contact manager](#contact-manager) (1), [google calendar client](#google-calendar-client) (1), [knowledge base](#knowledge-base) (1), [remind frontend](#remind-frontend) (1), [reminders](#reminders) (1), [rule-based calendar](#rule-based-calendar) (1), [scheduler](#scheduler) (1), [text calendar](#text-calendar) (1), [vcard address book](#vcard-address-book) (3)
- **[package-manager](#package-manager)** (20 tools): [AlternativeVCS](#alternativevcs) (1), [GitforLargeFiles](#gitforlargefiles) (1), [PackageManagerCLI](#packagemanagercli) (1), [PyPiSearcherCLI](#pypisearchercli) (1), [Translation](#translation) (1), [binary installer](#binary-installer) (1), [dev env manager](#dev-env-manager) (1), [knowledge base](#knowledge-base) (1), [kubectl plugin manager](#kubectl-plugin-manager) (1), [package manager frontend](#package-manager-frontend) (1), [package manager](#package-manager) (6), [runtime managers](#runtime-managers) (1), [shell](#shell) (1), [system info](#system-info) (1), [system updater](#system-updater) (1)
- **[password-manager](#password-manager)** (21 tools): [EncryptedPasswordManager](#encryptedpasswordmanager) (5), [PasswordGeneratorCLI](#passwordgeneratorcli) (1), [PasswordManagerCLI](#passwordmanagercli) (1), [PasswordWrapperCLI](#passwordwrappercli) (1), [bitwarden cli](#bitwarden-cli) (1), [enhanced cat](#enhanced-cat) (1), [password generator](#password-generator) (1), [password manager](#password-manager) (8), [secrets manager](#secrets-manager) (1), [secure archive manager](#secure-archive-manager) (1)
- **[pastebin](#pastebin)** (3 tools): [PastebinCLI](#pastebincli) (1), [pastebin](#pastebin) (1), [terminal sharing](#terminal-sharing) (1)
- **[productivity](#productivity)** (11 tools): [DirectionsQueryCLI](#directionsquerycli) (1), [GoogleScraperCLI](#googlescrapercli) (1), [Translation](#translation) (1), [VaccineCertViewerCLI](#vaccinecertviewercli) (1), [mind‑mapping](#mind‑mapping) (1), [notifications](#notifications) (1), [speed reading](#speed-reading) (1), [task manager](#task-manager) (1), [terminal dashboard](#terminal-dashboard) (1), [time tools](#time-tools) (1), [tui utils](#tui-utils) (1)
- **[programming](#programming)** (52 tools): [AlternativeVCS](#alternativevcs) (1), [BenchmarkingCLI](#benchmarkingcli) (1), [CodeStatsCLI](#codestatscli) (3), [DeterministicDebugger](#deterministicdebugger) (1), [DevToolboxCLI](#devtoolboxcli) (1), [GDBEnhancerTUI](#gdbenhancertui) (1), [ImageViewer(ASCII)](#imageviewer(ascii)) (1), [LightweightTextViewer](#lightweighttextviewer) (1), [OfflineDocsetSearcher](#offlinedocsetsearcher) (1), [RegexRefactorTool](#regexrefactortool) (1), [StaticAnalyzerCLI](#staticanalyzercli) (2), [advanced grep](#advanced-grep) (2), [api testing](#api-testing) (1), [argument parser](#argument-parser) (1), [assembly visualizers](#assembly-visualizers) (1), [benchmark dashboard](#benchmark-dashboard) (1), [build tool](#build-tool) (1), [build tools](#build-tools) (1), [cli generator](#cli-generator) (1), [code bundler](#code-bundler) (1), [code runner](#code-runner) (1), [code submission](#code-submission) (1), [command-line translator](#command-line-translator) (2), [contributor helper](#contributor-helper) (1), [debug assistant](#debug-assistant) (1), [debugging](#debugging) (2), [dev environment manager](#dev-environment-manager) (1), [dev environment](#dev-environment) (1), [devops tools](#devops-tools) (1), [enhanced cat](#enhanced-cat) (3), [env manager](#env-manager) (1), [file renamer](#file-renamer) (1), [go tools](#go-tools) (1), [javascript minifier](#javascript-minifier) (1), [leetcode client](#leetcode-client) (1), [live reloader](#live-reloader) (1), [npm tools](#npm-tools) (1), [release automation](#release-automation) (2), [scripting](#scripting) (1), [shell builder](#shell-builder) (1), [stack tools](#stack-tools) (1), [terminal sharing](#terminal-sharing) (1), [vcs tool](#vcs-tool) (1)
- **[programming-boilerplate](#programming-boilerplate)** (12 tools): [AlternativeVCS](#alternativevcs) (2), [changelog generators](#changelog-generators) (1), [contributing.md generator](#contributing.md-generator) (1), [enhanced cat](#enhanced-cat) (1), [git tools](#git-tools) (1), [license generators](#license-generators) (2), [project boilerplate](#project-boilerplate) (1), [project scaffolding ](#project-scaffolding) (1), [readme generators](#readme-generators) (1), [template generators](#template-generators) (1)
- **[prompt](#prompt)** (13 tools): [ShellPromptEnhancer](#shellpromptenhancer) (1), [ShellPromptTheme](#shellprompttheme) (1), [TerminalStatusLineEnhancer](#terminalstatuslineenhancer) (1), [WelcomeMessageCLI](#welcomemessagecli) (1), [bash tool](#bash-tool) (1), [custom prompt](#custom-prompt) (2), [shell prompt](#shell-prompt) (2), [shell](#shell) (2), [zsh prompt](#zsh-prompt) (2)
- **[religion](#religion)** (4 tools): [bible readers](#bible-readers) (1), [cli bible viewer](#cli-bible-viewer) (1), [command-line translator](#command-line-translator) (1), [text readers](#text-readers) (1)
- **[rm](#rm)** (13 tools): [DataRecovery](#datarecovery) (1), [FileDeletionTool](#filedeletiontool) (1), [ShellSyncBackup](#shellsyncbackup) (1), [command-line translator](#command-line-translator) (1), [enhanced cat](#enhanced-cat) (1), [file management](#file-management) (1), [file recovery](#file-recovery) (2), [safe delete](#safe-delete) (3), [shell](#shell) (1), [trash management](#trash-management) (1)
- **[rss](#rss)** (10 tools): [rss parser](#rss-parser) (1), [rss reader](#rss-reader) (6), [rss readers](#rss-readers) (1), [rss tool](#rss-tool) (1), [rss](#rss) (1)
- **[science](#science)** (20 tools): [AcademicDownloaderCLI](#academicdownloadercli) (1), [AlternativeVCS](#alternativevcs) (1), [AudioMixer](#audiomixer) (1), [BibManagerCLI](#bibmanagercli) (1), [ConferenceTrackerCLI](#conferencetrackercli) (1), [bioinformatics](#bioinformatics) (1), [command-line translator](#command-line-translator) (1), [education](#education) (1), [enhanced cat](#enhanced-cat) (2), [fun tools](#fun-tools) (1), [game](#game) (1), [knowledge base](#knowledge-base) (3), [periodic table](#periodic-table) (2), [reference manager](#reference-manager) (1), [terminal animation](#terminal-animation) (1), [terminal games](#terminal-games) (1)
- **[screen-recorder](#screen-recorder)** (11 tools): [svg generator](#svg-generator) (1), [terminal animation](#terminal-animation) (1), [terminal recorder](#terminal-recorder) (8), [terminal sharing](#terminal-sharing) (1)
- **[screensaver](#screensaver)** (6 tools): [TerminalScreensaver](#terminalscreensaver) (1), [ascii aquarium](#ascii-aquarium) (1), [ascii screensaver](#ascii-screensaver) (1), [screensaver](#screensaver) (2), [terminal animations ](#terminal-animations) (1)
- **[security](#security)** (38 tools): [EncryptionCLI](#encryptioncli) (1), [FastFindAlternative](#fastfindalternative) (1), [FileSignerCLI](#filesignercli) (1), [OneTimeSecretCLI](#onetimesecretcli) (1), [SecuritySandboxCLI](#securitysandboxcli) (1), [TOTPAuthenticatorCLI](#totpauthenticatorcli) (1), [VimEnhancer](#vimenhancer) (1), [cli encryption](#cli-encryption) (1), [code signer](#code-signer) (1), [encrypted filesystem](#encrypted-filesystem) (2), [encryption module](#encryption-module) (1), [encryption](#encryption) (2), [enhanced cat](#enhanced-cat) (1), [file encryption](#file-encryption) (1), [fuzzer](#fuzzer) (1), [gpg tools](#gpg-tools) (1), [license manager](#license-manager) (1), [oauth client](#oauth-client) (1), [package scanner](#package-scanner) (1), [password generator](#password-generator) (1), [password manager](#password-manager) (1), [password recovery](#password-recovery) (1), [secret manager](#secret-manager) (1), [secure backups](#secure-backups) (1), [security audit](#security-audit) (1), [security tools](#security-tools) (1), [shell](#shell) (1), [ssh vulnerability scan](#ssh-vulnerability-scan) (1), [ssl tools](#ssl-tools) (1), [steganography](#steganography) (5), [vulnerability scanner](#vulnerability-scanner) (1), [vulnerability viewer](#vulnerability-viewer) (1)
- **[shells](#shells)** (25 tools): [automation shell](#automation-shell) (1), [kornshell](#kornshell) (1), [modern shell](#modern-shell) (1), [shell](#shell) (21), [text-based window manager](#text-based-window-manager) (1)
- **[system](#system)** (39 tools): [CloudSyncManager](#cloudsyncmanager) (1), [DirectoryOrganizer](#directoryorganizer) (1), [HardwareController](#hardwarecontroller) (1), [ProcessManagerCLI](#processmanagercli) (1), [SystemMonitorTUI](#systemmonitortui) (1), [autocomplete](#autocomplete) (2), [brightness control](#brightness-control) (1), [checksum tools](#checksum-tools) (1), [clipboard manager](#clipboard-manager) (1), [clipboard tool](#clipboard-tool) (1), [command-line translator](#command-line-translator) (1), [console sharing](#console-sharing) (2), [dotfiles manager](#dotfiles-manager) (2), [enhanced cat](#enhanced-cat) (2), [env manager](#env-manager) (1), [hardware info](#hardware-info) (1), [man page viewer](#man-page-viewer) (1), [mount tools](#mount-tools) (1), [notification tool](#notification-tool) (1), [notifications](#notifications) (1), [port killer](#port-killer) (1), [process killer](#process-killer) (1), [sandbox runner](#sandbox-runner) (1), [shell logger](#shell-logger) (1), [shell](#shell) (2), [sound notifier](#sound-notifier) (1), [system inspector](#system-inspector) (1), [system manager](#system-manager) (2), [task killer](#task-killer) (1), [user management](#user-management) (1), [vcs benchmark](#vcs-benchmark) (1), [viewport tools](#viewport-tools) (1), [window info tools](#window-info-tools) (1)
- **[terminal](#terminal)** (24 tools): [ProjectNavigatorTUI](#projectnavigatortui) (1), [SessionDetachTool](#sessiondetachtool) (1), [TmuxSessionManager](#tmuxsessionmanager) (1), [minimal terminal](#minimal-terminal) (1), [multiplexer](#multiplexer) (3), [shared-terminal](#shared-terminal) (1), [terminal emulator](#terminal-emulator) (5), [terminal manager](#terminal-manager) (1), [terminal multiplexer](#terminal-multiplexer) (1), [terminal sharing](#terminal-sharing) (5), [tmux tools](#tmux-tools) (2), [wayland terminal](#wayland-terminal) (1), [window-manager](#window-manager) (1)
- **[text-processing](#text-processing)** (52 tools): [FileLineDeduperCLI](#filelinededupercli) (1), [FuzzySelectorCLI](#fuzzyselectorcli) (1), [LinkCheckerCLI](#linkcheckercli) (2), [TextProcessorCLI](#textprocessorcli) (1), [ascii-text-rendering](#ascii-text-rendering) (1), [browser utilities](#browser-utilities) (1), [character frequency](#character-frequency) (1), [cli formatter](#cli-formatter) (1), [code format checkers](#code-format-checkers) (1), [command-line translator](#command-line-translator) (5), [country normalizer](#country-normalizer) (1), [data extractor](#data-extractor) (1), [directory tree](#directory-tree) (1), [documentation](#documentation) (1), [enhanced cat](#enhanced-cat) (3), [file size tools](#file-size-tools) (1), [fuzzy text matcher](#fuzzy-text-matcher) (1), [hashing tools](#hashing-tools) (1), [html parsers](#html-parsers) (1), [lexicon matcher](#lexicon-matcher) (1), [line selector](#line-selector) (1), [log debugger](#log-debugger) (1), [log pattern extractor](#log-pattern-extractor) (1), [log viewer](#log-viewer) (2), [markdown viewer](#markdown-viewer) (2), [ngrams frequency analyzer](#ngrams-frequency-analyzer) (1), [output formatter](#output-formatter) (1), [pipeline builder](#pipeline-builder) (1), [scraping](#scraping) (1), [spell checker](#spell-checker) (1), [syntax highlighting](#syntax-highlighting) (1), [system info tools](#system-info-tools) (1), [terminal dashboard](#terminal-dashboard) (2), [text formatter](#text-formatter) (2), [text processing](#text-processing) (1), [text sampler](#text-sampler) (1), [text tokenizer](#text-tokenizer) (1), [text transformers](#text-transformers) (2), [url parser](#url-parser) (1), [vpn tools](#vpn-tools) (1)
- **[text-search](#text-search)** (15 tools): [AdvancedGrepCLI](#advancedgrepcli) (2), [FastFindAlternative](#fastfindalternative) (1), [advanced grep](#advanced-grep) (2), [code analysis](#code-analysis) (1), [code search](#code-search) (2), [file search](#file-search) (1), [interactive-line-select](#interactive-line-select) (1), [natural language](#natural-language) (1), [search tool](#search-tool) (1), [semantic text search](#semantic-text-search) (1), [text search](#text-search) (2)
- **[text-search-replace](#text-search-replace)** (6 tools): [CodeReplaceCLI](#codereplacecli) (1), [code refactoring](#code-refactoring) (1), [enhanced cat](#enhanced-cat) (1), [search tools](#search-tools) (1), [tabular-sql-query](#tabular-sql-query) (1), [text replace](#text-replace) (1)
- **[time-tracker](#time-tracker)** (23 tools): [AlternativeVCS](#alternativevcs) (1), [HabitTrackerTUI](#habittrackertui) (1), [TimeTrackerCLI](#timetrackercli) (1), [automatic time tracker](#automatic-time-tracker) (1), [command-line translator](#command-line-translator) (1), [enhanced cat](#enhanced-cat) (1), [habit tracker](#habit-tracker) (2), [habit trackers](#habit-trackers) (1), [load monitor](#load-monitor) (1), [pomodoro tracker](#pomodoro-tracker) (1), [pomodoro](#pomodoro) (3), [productivity](#productivity) (1), [time trackers](#time-trackers) (2), [time tracking](#time-tracking) (3), [time-tracker](#time-tracker) (2), [timers](#timers) (1)
- **[todo-manager](#todo-manager)** (35 tools): [ForensicsCLI](#forensicscli) (1), [GitBackedTodoCLI](#gitbackedtodocli) (1), [TaskManagerCLI](#taskmanagercli) (3), [TodoListTUI](#todolisttui) (1), [TwitterClientCLI](#twitterclientcli) (1), [command-line translator](#command-line-translator) (2), [feature-rich todo manager](#feature-rich-todo-manager) (1), [hierarchical todo manager](#hierarchical-todo-manager) (1), [interactive todo.txt](#interactive-todo.txt) (1), [kanban](#kanban) (2), [knowledge base](#knowledge-base) (3), [note-taking](#note-taking) (1), [plain-text todo manager](#plain-text-todo-manager) (1), [project-based todo manager](#project-based-todo-manager) (1), [python todo manager](#python-todo-manager) (1), [shell history](#shell-history) (1), [task manager](#task-manager) (2), [terminal sharing](#terminal-sharing) (1), [text calendar](#text-calendar) (1), [todo manager](#todo-manager) (6), [todo managers](#todo-managers) (1), [todoist client](#todoist-client) (1), [wishlist](#wishlist) (1)
- **[torrent](#torrent)** (8 tools): [AlternativeVCS](#alternativevcs) (1), [RPGClientTUI](#rpgclienttui) (1), [TUIBitTorrentClient](#tuibittorrentclient) (1), [TorrentClientCLI](#torrentclientcli) (1), [TorrentClientTUI](#torrentclienttui) (1), [TorrentClient](#torrentclient) (1), [terminal sharing](#terminal-sharing) (1), [torrent streamer](#torrent-streamer) (1)
- **[transfer](#transfer)** (44 tools): [ClipboardManagerCLI](#clipboardmanagercli) (1), [CloudFileDownloaderCLI](#cloudfiledownloadercli) (1), [CloudSyncManager](#cloudsyncmanager) (1), [DownloadManagerCLI](#downloadmanagercli) (1), [FTPClient](#ftpclient) (1), [FileSharingCLI](#filesharingcli) (1), [FileSharingOverTor](#filesharingovertor) (1), [FileSynchronizer](#filesynchronizer) (1), [FileTransferCLI](#filetransfercli) (4), [FileTransferP2PCLI](#filetransferp2pcli) (1), [HTTPIEAlternative](#httpiealternative) (1), [LocalHTTPFileServer](#localhttpfileserver) (1), [NetworkDataFetcherCLI](#networkdatafetchercli) (1), [ShellSyncBackup](#shellsyncbackup) (1), [SiteSyncOverFTP](#sitesyncoverftp) (1), [TranslatorCLI](#translatorcli) (1), [VideoDownloaderCLI](#videodownloadercli) (1), [YouTubeSearchPlayerCLI](#youtubesearchplayercli) (1), [YouTubeToMP3Downloader](#youtubetomp3downloader) (1), [clipboard sync](#clipboard-sync) (2), [code sharing](#code-sharing) (1), [downloader](#downloader) (1), [enhanced cat](#enhanced-cat) (1), [file sharing tool](#file-sharing-tool) (1), [file sharing](#file-sharing) (3), [file sync](#file-sync) (1), [github file downloader](#github-file-downloader) (1), [knowledge base](#knowledge-base) (1), [media downloader](#media-downloader) (1), [rclone frontend](#rclone-frontend) (1), [rss tools](#rss-tools) (1), [scp alternative](#scp-alternative) (1), [shell](#shell) (1), [telegram tools](#telegram-tools) (1), [terminal sharing](#terminal-sharing) (1), [video downloader](#video-downloader) (2), [youtube downloader](#youtube-downloader) (1)
- **[typing](#typing)** (16 tools): [HotkeyManager](#hotkeymanager) (1), [TerminalGame(TypingTrainer)](#terminalgame(typingtrainer)) (1), [typing game](#typing-game) (3), [typing practice ](#typing-practice) (1), [typing practice](#typing-practice) (3), [typing speed test](#typing-speed-test) (1), [typing test](#typing-test) (5), [typing tutor](#typing-tutor) (1)
- **[utility](#utility)** (46 tools): [ClipboardHelperCLI](#clipboardhelpercli) (1), [DesktopEntryGenerator](#desktopentrygenerator) (1), [alerting](#alerting) (1), [bash learning tool](#bash-learning-tool) (1), [bash utils](#bash-utils) (1), [caching](#caching) (1), [checksum tool](#checksum-tool) (1), [colorizer](#colorizer) (1), [command launcher](#command-launcher) (1), [command watcher](#command-watcher) (1), [config validator](#config-validator) (1), [developer automation](#developer-automation) (1), [devtools](#devtools) (1), [emoji generators](#emoji-generators) (1), [enhanced cat](#enhanced-cat) (1), [env manager](#env-manager) (1), [file remover](#file-remover) (1), [file utilities](#file-utilities) (1), [fzf tools](#fzf-tools) (1), [image recognition](#image-recognition) (1), [installer](#installer) (1), [language learning](#language-learning) (1), [log generators](#log-generators) (1), [movie info tools](#movie-info-tools) (1), [performance tools](#performance-tools) (1), [process monitor](#process-monitor) (1), [progress viewer](#progress-viewer) (1), [regex practice](#regex-practice) (1), [semantic search](#semantic-search) (1), [shell customization](#shell-customization) (1), [shell enhancements](#shell-enhancements) (1), [shell](#shell) (2), [spell checker](#spell-checker) (1), [stock tracker](#stock-tracker) (1), [table generator](#table-generator) (1), [terminal games](#terminal-games) (1), [terminal navigation](#terminal-navigation) (1), [terminal sharing](#terminal-sharing) (2), [terminal testing](#terminal-testing) (1), [terminal themes](#terminal-themes) (1), [unicode tools](#unicode-tools) (1), [weather](#weather) (2), [wellness](#wellness) (1)
- **[versioning](#versioning)** (9 tools): [AlternativeVCS](#alternativevcs) (3), [RepoManagerCLI](#repomanagercli) (1), [fossil interface](#fossil-interface) (1), [git manage](#git-manage) (1), [git translator](#git-translator) (1), [terminal sharing](#terminal-sharing) (1), [version control](#version-control) (1)
- **[video](#video)** (14 tools): [LightweightAudioPlayer](#lightweightaudioplayer) (1), [MediaConverterCLI](#mediaconvertercli) (1), [VideoEditorCLI](#videoeditorcli) (1), [YouTubeAudioSplitter](#youtubeaudiosplitter) (1), [ascii video](#ascii-video) (1), [audio translator](#audio-translator) (1), [downloader](#downloader) (1), [screen recording](#screen-recording) (1), [video converter](#video-converter) (1), [video info](#video-info) (1), [video meme](#video-meme) (1), [video streaming](#video-streaming) (1), [youtube browser](#youtube-browser) (1), [youtube client](#youtube-client) (1)
- **[viewers](#viewers)** (34 tools): [ImageViewer(ASCII)](#imageviewer(ascii)) (2), [MarkdownViewer(GUI/CLI)](#markdownviewer(gui-cli)) (1), [TerminalIPTVPlayer](#terminaliptvplayer) (1), [TerminalImageViewer](#terminalimageviewer) (1), [VideoAudioPlayer(GUI/CLI)](#videoaudioplayer(gui-cli)) (2), [YouTubeVideoSearcher](#youtubevideosearcher) (1), [article readers](#article-readers) (1), [audio visualizer](#audio-visualizer) (1), [cli reader](#cli-reader) (1), [comic reader](#comic-reader) (1), [command-line translator](#command-line-translator) (4), [ebook reader](#ebook-reader) (2), [enhanced cat](#enhanced-cat) (2), [github tools](#github-tools) (1), [interactive tail viewer](#interactive-tail-viewer) (1), [ipynb viewer](#ipynb-viewer) (1), [jupyter notebook viewer](#jupyter-notebook-viewer) (1), [kafka viewer](#kafka-viewer) (1), [markdown viewer](#markdown-viewer) (1), [media viewer](#media-viewer) (1), [news reader](#news-reader) (3), [rss reader](#rss-reader) (1), [terminal process viewer](#terminal-process-viewer) (1), [vcs viewer](#vcs-viewer) (1), [youtube client](#youtube-client) (1)
- **[vm](#vm)** (23 tools): [QEMU UI](#qemu-ui) (1), [android emulation](#android-emulation) (1), [container inspector](#container-inspector) (1), [container manager](#container-manager) (2), [container tools](#container-tools) (1), [container](#container) (5), [dev environment](#dev-environment) (1), [docker analysis](#docker-analysis) (1), [docker management](#docker-management) (2), [docker manager](#docker-manager) (1), [docker tool](#docker-tool) (1), [docker tools](#docker-tools) (1), [docker tui](#docker-tui) (1), [emulator](#emulator) (1), [resource monitor](#resource-monitor) (1), [shell](#shell) (1), [virtualization](#virtualization) (1)
- **[webdev](#webdev)** (30 tools): [APIClientCLI](#apiclientcli) (1), [AlternativeVCS](#alternativevcs) (1), [GitBackedWikiEngine](#gitbackedwikiengine) (1), [LinkCheckerCLI](#linkcheckercli) (1), [LoadTestingTool](#loadtestingtool) (1), [Network tools](#network-tools) (1), [ReconToolCLI](#recontoolcli) (1), [StaticSiteGenerator](#staticsitegenerator) (3), [TextToMorseCLI](#texttomorsecli) (1), [api client](#api-client) (1), [api tool](#api-tool) (1), [cleanup tools](#cleanup-tools) (1), [cloud storage clients](#cloud-storage-clients) (1), [deployment tools](#deployment-tools) (1), [django tools](#django-tools) (1), [enhanced cat](#enhanced-cat) (1), [file generator](#file-generator) (1), [html/xml tools](#html-xml-tools) (1), [http clients](#http-clients) (1), [load testing](#load-testing) (2), [pentest suite](#pentest-suite) (1), [screenshot tools](#screenshot-tools) (1), [shopify dev](#shopify-dev) (1), [static site deployers](#static-site-deployers) (1), [terminal sharing](#terminal-sharing) (1), [uptime checkers](#uptime-checkers) (1), [web crawlers](#web-crawlers) (1)
- **[writing](#writing)** (11 tools): [Translation](#translation) (1), [command-line translator](#command-line-translator) (1), [dictionary](#dictionary) (2), [grammar checker](#grammar-checker) (1), [markdown tools](#markdown-tools) (1), [story generator](#story-generator) (1), [terminal sharing](#terminal-sharing) (1), [text linting](#text-linting) (1), [vocabulary builder](#vocabulary-builder) (1), [writing linter](#writing-linter) (1)


# ai
[Back to TOC](#📚-contents)

Interfaces and front-ends to GPT engines and other tools powered by artificial intelligence and Natural Language Processing
## 📁 AI assistant
_... description of the subcategory ..._

* [gemini-cli](nan) [🤖 🌐 🖥️CLI] - A command-line interface (CLI) for Google Gemini.

## 📁 AI terminal assistant
_... description of the subcategory ..._

* [llm-term](nan) [🤖 🌐 🖥️CLI] - A Rust-based CLI tool that generates and executes terminal commands using OpenAI's language models.

## 📁 ai assistant
_... description of the subcategory ..._

* [clai](nan) [🤖 🌐 🖥️CLI] - Command Line AI is a command line integration for openai. It's setup to help you learn new shell commands and construct more complex commands.
* [clevercli](nan) [🤖 🌐 🖥️CLI] - ChatGPT powered CLI utilities. Easily add new prompt types.
* [Instrukt](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A integrated AI environment in the terminal. Build, test and instruct agents.
* [Mods!](nan) [🤖 🌐 🖥️CLI] - AI for the command line, built for pipelines.
* [safespace](nan) [🤖 ❌ 🖥️CLI 🖥️TUI] - Your local AI counselor. LLM app that runs offline from a single binary.
* [wtg](nan) [🤖 ❌ 🖥️CLI] - What The GPT (wtg), a CLI to chat with your program logs.

## 📁 ai chatbot
_... description of the subcategory ..._

* [HAL 2023](nan) [🤖 🌐 🖥️CLI] - Inspired by the infamous HAL9000, it is a simple script to chat with OpenAI's ChatGPT.

## 📁 ai cli
_... description of the subcategory ..._

* [ChatGPTerminator](nan) [🤖 🌐 🖥️CLI] - GPTerminator provides a convenient way to interact with OpenAI's chat completion and image generation API's using your command line interface.

## 📁 ai toolkit
_... description of the subcategory ..._

* [leettools](nan) [🤖 🌐 🖥️CLI] - AI Search tools.

## 📁 ai workflow engine
_... description of the subcategory ..._

* [fabric](nan) [🤖 🌐 🖥️CLI] - An open-source framework for augmenting humans using AI, providing a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere.

## 📁 alibaba scraper
_... description of the subcategory ..._

* [Alibaba-CLI-Scraper](nan) [🤖 🌐 🖥️TUI] - Create your own Alibaba dataset and interact with it in plain English.

## 📁 autonomous agent
_... description of the subcategory ..._

* [kwaak](nan) [🤖 ❌ 🖥️CLI] - Run a team of autonomous AI agents on your code.

## 📁 chatgpt
_... description of the subcategory ..._

* [cligpt](nan) [🤖 🌐 🖥️CLI] - ChatGPT but in the terminal.

## 📁 chatgpt cli
_... description of the subcategory ..._

* [AIChat](nan) [🤖 🌐 🖥️CLI] - Using ChatGPT/GPT-3.5/GPT-4 in the terminal.
* [cai](nan) [🤖 🌐 🖥️TUI] - The fastest CLI tool for prompting LLMs. Including support for prompting several LLMs at once!
* [cha](nan) [🤖 🌐 🖥️TUI] - A simple CLI chat tool to easily interface with OpenAI's models.
* [Chatblade](nan) [🤖 🌐 🖥️CLI] - Chatblade is a versatile command-line interface (CLI) tool designed to interact with OpenAI's ChatGPT.
* [gpterm](nan) [🤖 🌐 🖥️CLI] - Yet another command-line ChatGPT frontend written in Rust.
* [llm-term](nan) [🤖 🌐 🖥️CLI] - Chat with OpenAI's GPT models directly from the command line.

## 📁 chatgpt client
_... description of the subcategory ..._

* [Elia](nan) [🤖 🌐 🖥️TUI] - A terminal ChatGPT client built with Textual.

## 📁 chatgpt tools
_... description of the subcategory ..._

* [AI](nan) [🤖 🌐 🖥️CLI] - A command-line ChatGPT client in BASH with conversation/completion support.
* [ata](nan) [❌ 🌐 🖥️CLI] - Ask the Terminal Anything: OpenAI GPT in the terminal.
* [chatgpt](nan) [🤖 🌐 🖥️CLI] - Simple command line integration to ChatGPT.

## 📁 cli assistant
_... description of the subcategory ..._

* [genie](nan) [🤖 🌐 🖥️CLI] - Personal assistant for the CLI that helps in tasks such as running commands, generating images and music, summarizing comments.

## 📁 git tool
_... description of the subcategory ..._

* [egit](nan) [🤖 ❌ 🖥️TUI] - A.I. tools and workflows for Git.

## 📁 gpt-powered parser
_... description of the subcategory ..._

* [GPTparser](nan) [🤖 🌐 🖥️TUI] - Use GPTparser with your OpenAI API to scrape & parse files into structured JSON files.

## 📁 http tools
_... description of the subcategory ..._

* [ht](nan) [❌ ❌ 🖥️CLI] - A shell command that answers your questions about shell commands using OpenAI GPT.

## 📁 llm runner
_... description of the subcategory ..._

* [ollama](https://ollama.com/) [🤖 ❌ 🖥️CLI] - Get up and running with large language models locally.

## 📁 natural language
_... description of the subcategory ..._

* [osh](nan) [🤖 ❌ 🖥️CLI] - Ollama Shell Helper (osh): English to Unix-like Shell Commands translation using Local LLMs with Ollama.

## 📁 ollama client
_... description of the subcategory ..._

* [parllama](nan) [🤖 🌐 🖥️TUI] - TUI designed for easy management and use of Ollama based LLMs.

## 📁 pipeable ai chat
_... description of the subcategory ..._

* [chat.sh](nan) [🤖 🌐 🖥️CLI] - Pipeable LLM wrapper with code execution (OpenRouter).

## 📁 team knowledge AI
_... description of the subcategory ..._

* [savvy-cli](nan) [🤖 🌐 🖥️CLI] - Automatically capture and surface your team's tribal knowledge.

## 📁 terminal assistant
_... description of the subcategory ..._

* [Spren](https://smadgulkar.github.io/spren/) [🤖 🌐 🖥️CLI] - AI-powered terminal assistant that converts natural language to shell commands. Supports PowerShell, Bash, and CMD with intelligent command suggestions and safety checks.
* [wut](nan) [❌ ❌ 🖥️TUI] - An terminal assistant for the hopelessly confused; it explains the meaning of the output from the last command.

## 📁 terminal ui
_... description of the subcategory ..._

* [termite](nan) [🤖 ❌ 🖥️TUI] - Generative UI in your terminal.

# animation
[Back to TOC](#📚-contents)

Generate or display animated graphics and effects
## 📁 AsciiTerminalAnimation
_... description of the subcategory ..._

* [asciicquarium](http://www.robobunny.com/projects/asciiquarium/html/) [❌ ❌ 🖥️TUI] - Enjoy the mysteries of the sea from the safety of your own terminal!
* [cmatrix](http://www.asty.org/cmatrix/) [❌ ❌ 🖥️TUI] - ncurses program that display the scrolling lines found in the movie `The matrix`.
* [StarWars vision](nan) [❌ 🌐 🖥️TUI] - See Star Wars in ASCII with ``telnet towel.blinkenlights.nl`` (server seems down recently - I leave the link in the hope that it will be resumed in the future).
* [Steam Locomotive](http://www.cyberciti.biz/tips/displays-animations-when-accidentally-you-type-sl-instead-of-ls.html) [❌ ❌ 🖥️TUI] - A steam locomotive traverses the screen from right to left if `sl` is typed instead of `ls`.
* [ternimal](nan) [❌ ❌ 🖥️TUI] - Simulate a life form in the terminal.

## 📁 EducationalCryptoVisualizer
_... description of the subcategory ..._

* [sha256-animation](nan) [❌ ❌ 🖥️TUI] - Animation of the SHA-256 hash function in your terminal.

## 📁 ImageViewer(ASCII)
_... description of the subcategory ..._

* [cbonsai](nan) [❌ ❌ 🖥️TUI] - A bonsai tree generator, written in C using ncurses. It intelligently creates, colors, and positions a bonsai tree.

## 📁 SpinnerCLI
_... description of the subcategory ..._

* [ora](nan) [❌ ❌ 🖥️CLI] - Elegant terminal spinner.

## 📁 ascii animation
_... description of the subcategory ..._

* [ascii-movie](nan) [❌ ❌ 🖥️CLI] - Allows to play the ASCII art Star War movie locally or it can open a connection to play it over SSH or telnet.
* [ccube](nan) [❌ ❌ 🖥️TUI] - Rotating 3d cube in terminal; written in C.
* [chaftrix](nan) [❌ ❌ 🖥️CLI] - C program that will render the matrix effect in the terminal window in the background, while rendering an image in the foreground, allowing animation of this image in one or two dimensions.
* [ctree](nan) [❌ ❌ 🖥️TUI] - A Christmas tree right from your terminal.
* [LundukeHoliday](nan) [❌ ❌ 🖥️TUI] - A simple Bash script that shows some animated, ASCII holiday decorations in your shell.
* [terminal-art](nan) [❌ ❌ 🖥️TUI] - Art made in the terminal: rotating cube.

## 📁 ascii art
_... description of the subcategory ..._

* [ascii-matrix](nan) [❌ ❌ 🖥️CLI] - This script written in the C language, will render the matrix effect in the terminal, while rendering ASCII art loaded from a txt file, at the center of the terminal window.

## 📁 ascii effects
_... description of the subcategory ..._

* [console-fun](nan) [❌ 🌐 🖥️TUI] - Some console stuff to have a fun and watch some animations with texts, figures, etc.

## 📁 ascii renderer
_... description of the subcategory ..._

* [animatrix](nan) [❌ ❌ 🖥️CLI] - C program that will create some basic animation of ascii-art loaded from a txt file, while rendering the matrix effect in the terminal window.
* [c-pipes](nan) [❌ ❌ 🖥️CLI] - Program written in the C language that will render random coloured zigzag lines in the terminal, while the font, speed, density and number of lines are fully costumizable. Each line stops once it reaches the edge of the window, only for a new line to begin.
* [c-squares](nan) [❌ ❌ 🖥️CLI] - Program written in C that will render random coloured rectangulars in the terminal, while the font, speed, density, color, ratio and number of the shapes drawn are fully costumizable.

## 📁 ascii tree generator
_... description of the subcategory ..._

* [PyBonsai](nan) [❌ ❌ 🖥️TUI] - Generate procedural ASCII art trees in the terminal.

## 📁 cli clocks
_... description of the subcategory ..._

* [Binary Clock](nan) [❌ ❌ 🖥️CLI] - Displays a clock where numbers are represented with blue and gray dots with binary encoding.

## 📁 enhanced cat
_... description of the subcategory ..._

* [cli-fireplace](nan) [❌ ❌ 🖥️CLI] - Shows digital fireplace.
* [cli-mandelbrot](nan) [❌ ❌ 🖥️CLI] - A CLI for traversing the Mandelbrot fractal.

## 📁 maze generator
_... description of the subcategory ..._

* [Maze Solver](nan) [❌ ❌ 🖥️TUI] - Generate, display and solve mazes in an animated way in the terminal.

## 📁 simulation
_... description of the subcategory ..._

* [rich_life](nan) [❌ ❌ 🖥️CLI] - Conway's Game of Life and Langton's Ant.

## 📁 terminal animation
_... description of the subcategory ..._

* [bb](nan) [❌ ❌ 🖥️TUI] - The portable BB demo of AAlib, with fixes for vax etc.
* [firew0rks](nan) [❌ ❌ 🖥️TUI] - Fireworks in your terminal.
* [neo](nan) [❌ ❌ 🖥️TUI] - Recreates the digital rain effect from "The Matrix". Streams of random characters will endlessly scroll down your terminal screen.
* [No More Secrets](nan) [❌ ❌ 🖥️CLI] - A command line tool that recreates the famous data decryption effect seen in the 1992 movie Sneakers.
* [nyancat](nan) [❌ ❌ 🖥️TUI] - Nyancat in your terminal, rendered through ANSI escape sequences.
* [rusty-rain](nan) [❌ ❌ 🖥️TUI] - A cross platform matrix rain made with Rust.

## 📁 terminal fun
_... description of the subcategory ..._

* [paclear](nan) [❌ ❌ 🖥️CLI] - paclear is a clear command with pacman animation.

## 📁 text effects
_... description of the subcategory ..._

* [terminaltexteffects](nan) [❌ ❌ 🖥️TUI] - TerminalTextEffects (TTE) is a terminal visual effects engine, application, and Python library.

# backup
[Back to TOC](#📚-contents)

Tools to manage the backup of files and directories
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [shallow-backup](nan) [❌ ❌ 🖥️CLI] - Git integrated backup tool.
* [zbackup](http://zbackup.org/) [❌ ❌ 🖥️CLI] - A globally-deduplicating backup tool, based on the ideas found in rsync.

## 📁 BackupAutomationWrapper
_... description of the subcategory ..._

* [Duply](http://duply.net/) [❌ ❌ 🖥️CLI] - Simplifies the use of [duplicity](http://duplicity.nongnu.org/) by keeping clean configuration files to automate the backup.

## 📁 EncryptedBackupCLI
_... description of the subcategory ..._

* [bupstash](nan) [❌ ❌ 🖥️CLI] - Secure, encrypted backups with efficient deduplication, client-side encryption, offline decryption, search-tagged data protection, strong privacy, robust performance on slow networks, memory-safe security against attacks, incremental backups, and minimal RAM usage for production use.

## 📁 EncryptedBackupTool
_... description of the subcategory ..._

* [borg](https://www.borgbackup.org/) [❌ ❌ 🖥️CLI] - Encrypted backups with a clean and simple interface, easy to use and set up, possibility to mount the backup archive with FUSE and inspect it as a regular file system.

## 📁 GpgCompressedBackupTool
_... description of the subcategory ..._

* [duplicity](http://duplicity.nongnu.org/) [❌ ❌ 🖥️CLI] - Creates GPG encrypted, compressed backups; client-side encryption allows uploading the backup onto untrusted servers.

## 📁 PaperBarcodeBackup
_... description of the subcategory ..._

* [paperbackup](nan) [❌ ❌ 🖥️CLI] - Create a PDF with barcodes to backup text files on paper.

## 📁 ShellSyncBackup
_... description of the subcategory ..._

* [Zaloha.sh](nan) [❌ ❌ 🖥️CLI] - Shellscript for synchronization of files and directories.

## 📁 backup tool
_... description of the subcategory ..._

* [Restic](https://restic.net/) [❌ 🌐 🖥️CLI] - A backup program that is fast, efficient, and secure.
* [rsnapshot](https://rsnapshot.org) [❌ ❌ 🖥️CLI] -  A filesystem snapshot utility based on rsync. It manages a rotation schedule when to discard older backup, e.g. from hourly to yearly. The Perl code makes extensive use of hard links and greatly reduces the disk space required.
* [ZnapZend](https://www.znapzend.org) [❌ ❌ 🖥️CLI] - ZFS centric backup tool creates snapshots and sends them to backup volumes. It manages local and remote copies by thinning them out as time progresses.

## 📁 cli backup
_... description of the subcategory ..._

* [Kopia](https://kopia.io/) [❌ 🌐 🖥️CLI] - Cross-platform backup tool for Windows, macOS & Linux with fast, incremental backups, client-side end-to-end encryption, compression, and data deduplication. CLI and GUI included.

## 📁 git backup
_... description of the subcategory ..._

* [backhub](nan) [❌ 🌐 🖥️CLI] - Backhub helps maintain backups of multiple GitHub repos as full local mirrors.

## 📁 git-based backup
_... description of the subcategory ..._

* [bup](https://bup.github.io/) [❌ ❌ 🖥️CLI] - Very efficient backup system based on the git packfile format, providing fast incremental saves and global deduplication.

## 📁 network backup
_... description of the subcategory ..._

* [rdiff-backup](https://rdiff-backup.net/) [❌ 🌐 🖥️CLI] - Reverse differential backup tool, over a network or locally, using the same protocol as rsync to transfer and store data.

## 📁 restic config
_... description of the subcategory ..._

* [Crestic](https://nils-werner.github.io/crestic/) [❌ 🌐 🖥️CLI] - Configurable Restic Wrapper.

## 📁 restic wrapper
_... description of the subcategory ..._

* [autorestic](https://autorestic.vercel.app/) [❌ 🌐 🖥️CLI] - A wrapper around the [restic](https://restic.net/) backup tool, with the goal of simplifying the setup and usage through the use of config files.

## 📁 thread archiver
_... description of the subcategory ..._

* [thread-safe](nan) [❌ ❌ 🖥️CLI] - Keep your favorite Twitter threads safe with a local copy.

## 📁 workspace backup
_... description of the subcategory ..._

* [gwbackupy](nan) [❌ ❌ 🖥️CLI] - Open source Google Workspace™ backup solution.

# browser
[Back to TOC](#📚-contents)

Web browsers with textual interface
## 📁 FastFindAlternative
_... description of the subcategory ..._

* [asuka](https://git.sr.ht/~julienxx/asuka) [❌ ❌ 🖥️CLI] - A Gemini Project client written in Rust with ncurses.

## 📁 FuzzyFinderPlugin
_... description of the subcategory ..._

* [Telescope](https://telescope.omarpolo.com/) [❌ ❌ 🖥️CLI] - Gemini client with UI that is strongly inspired from Emacs and W3M.

## 📁 GeminiClientTUI
_... description of the subcategory ..._

* [Amfora](nan) [❌ 🌐 🖥️TUI] - Amfora aims to be the best looking Gemini client with the most features. It does not support Gopher or other non-Web protocols.
* [Bombadillo](https://bombadillo.colorfield.space/) [❌ 🌐 🖥️TUI] - A non-web browser, designed for a growing list of protocols operating outside of the web. Currently supports Gemini, Finger and Gopher.

## 📁 PlaceSearchCLI
_... description of the subcategory ..._

* [gplaces](nan) [❌ 🌐 🖥️CLI] - Simple but powerful terminal Gemini client.

## 📁 StatusSyncCLI
_... description of the subcategory ..._

* [Gremlin](nan) [❌ 🌐 🖥️CLI] - Gemini browser for the terminal.

## 📁 TerminalBrowserTUI
_... description of the subcategory ..._

* [browsh](https://www.brow.sh/) [❌ 🌐 🖥️TUI] - It renders anything that a modern browser can; HTML5, CSS3, JS, video and even WebGL. Its main purpose is to be run on a remote server and accessed via SSH/Mosh or the in-browser HTML service in order to significantly reduce bandwidth and thus both increase browsing speeds and decrease bandwidth costs.

## 📁 TerminalWebBrowser
_... description of the subcategory ..._

* [Elinks](http://elinks.cz/) [❌ 🌐 🖥️TUI] - "Advanced and well-established feature-rich text mode web browser"; started as a fork of `Links`; it supports background download with queueing, some support from CSS, text box editing in external text editor.
* [Links](http://www.jikos.cz/~mikulas/links//) [❌ 🌐 🖥️TUI] - A textual Web browser with tables and frames.
* [Lynx](http://lynx.invisible-island.net/) [❌ 🌐 🖥️TUI] - A highly configurable text-based web browser, one of the oldest CLI browser I'm aware of.
* [w3m](http://w3m.sourceforge.net/) [❌ 🌐 🖥️TUI] - A text-based web browser as well as a pager like `less`, it can be used as a text formatting tool which typesets HTML into plain text.

## 📁 TextBasedWebBrowser
_... description of the subcategory ..._

* [Graphene](nan) [❌ 🌐 🖥️TUI] - A text-based web browser that's a joy to use.

## 📁 WebSearchCLI
_... description of the subcategory ..._

* [s](nan) [❌ 🌐 🖥️CLI] - Web search from the terminal. Just opens in your browser.

## 📁 arXivSearcher
_... description of the subcategory ..._

* [cli-arxiv](nan) [❌ 🌐 🖥️CLI] - CLI tool for exploring arXiv.

## 📁 console sharing
_... description of the subcategory ..._

* [Romulus](nan) [❌ ❌ 🖥️CLI] - A cross-platform Gemini console client in C# with a simple user interface, interactive menus and mouse support.

## 📁 fuzzy‑search
_... description of the subcategory ..._

* [min](nan) [❌ 🌐 🖥️CLI] - A Gemini browser with Vim style keyboard navigation, client certificate support and history and bookmarks saved in TSV files.

## 📁 rss reader
_... description of the subcategory ..._

* [Litter](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - Litter is a minimalistic, terminal-based read-only browser that allows users to browse the web without the bloat and distractions of modern web browsers.

## 📁 text browser
_... description of the subcategory ..._

* [Chawan](https://sr.ht/~bptato/chawan/) [❌ 🌐 🖥️CLI 🖥️TUI] - A text-mode web browser. It displays websites in your terminal and allows you to navigate on them. It can also be used as a terminal pager.

## 📁 web browser
_... description of the subcategory ..._

* [carbonyl](nan) [❌ 🌐 🖥️TUI] - Chromium running inside your terminal.

# calc
[Back to TOC](#📚-contents)

Calculators for mathematical operations among numbers, dates, base conversions, etc.
## 📁 AdvancedCalculators
_... description of the subcategory ..._

* [Qalculate](https://qalculate.github.io/) [❌ ❌ 🖥️CLI] - Multi-purpose calculator with customizable functions, units, arbitrary precision, plotting (it includes a GUI).

## 📁 MathCLI
_... description of the subcategory ..._

* [kalker](nan) [❌ ❌ 🖥️CLI] - Calculator that supports math-like syntax with user-defined variables, functions, derivation, integration, and complex numbers.

## 📁 StorageCalculatorCLI
_... description of the subcategory ..._

* [bcal](nan) [❌ ❌ 🖥️CLI] - Byte CALculator - A REPL CLI utility for storage expression evaluation, SI/IEC conversion, byte address calculation, base conversion and LBA/CHS calculation.

## 📁 TerminalCalculator
_... description of the subcategory ..._

* [Nota](https://kary.us/nota/) [❌ ❌ 🖥️TUI] - Terminal calculator with rich notation.

## 📁 TimeDiffCalculatorCLI
_... description of the subcategory ..._

* [pdd](nan) [❌ ❌ 🖥️CLI] - Tiny date, time diff calculator.

## 📁 bitwise tools
_... description of the subcategory ..._

* [Bitwise](nan) [❌ ❌ 🖥️TUI] - Base conversion and bit manipulator in ncurses.

## 📁 calculator
_... description of the subcategory ..._

* [AngouriMathCLI](nan) [❌ ❌ 🖥️CLI] - CLI calculator based on AngouriMath.
* [CalcPy](nan) [❌ ❌ 🖥️TUI] - Terminal calculator and advanced math solver using Python, IPython and SymPy.
* [DateTimeMate](nan) [❌ ❌ 🖥️CLI] - Golang package and CLI to compute the difference between date, time or duration.
* [genius](nan) [❌ ❌ 🖥️CLI] - Genius calculator is a general purpose calculator and mathematics tool with many features.
* [HIP35](nan) [❌ ❌ 🖥️CLI] - HP-35 RPN calculator emulator in C++17 with a terminal user interface.
* [kalc](nan) [❌ ❌ 🖥️TUI] - A complex numbers, 2D/3D graphing, arbitrary precision, vector, CLI calculator with real-time output.
* [Numbat](nan) [❌ ❌ 🖥️CLI] - Numbat is a calculator for scientific computations with first class support for physical dimensions and units.
* [Speedcrunch](nan) [❌ ❌ ❌] - SpeedCrunch is a high-precision scientific calculator featuring a fast, keyboard-driven user interface.

## 📁 calculators
_... description of the subcategory ..._

* [mdlt](nan) [❌ ❌ 🖥️CLI] - A lightweight command line tool that lets you perform arithmetic and symbolic math operations right from the terminal.

## 📁 expression calc
_... description of the subcategory ..._

* [ka](nan) [❌ ❌ 🖥️CLI] - A calculator language.

## 📁 math engine
_... description of the subcategory ..._

* [maxima](nan) [❌ ❌ 🖥️CLI] - Maxima is a manipulation system for symbolic and numerical expressions, including differentiation, integration, Taylor series, Laplace transforms, ordinary differential equations, systems of linear equations, polynomials, sets, lists, vectors, matrices and tensors.

## 📁 programmer tools
_... description of the subcategory ..._

* [Programmer calculator](nan) [❌ ❌ 🖥️TUI] - Terminal calculator made for programmers working with multiple number representations, sizes, and overall close to the bits.

# cd
[Back to TOC](#📚-contents)

Programs for improving the efficiency of directory traversal by remembering common paths and other approaches; alternatives to the `cd` command
## 📁 FastCdTool
_... description of the subcategory ..._

* [fasd](nan) [❌ ❌ 🖥️CLI] - It offers quick access to files and directories for POSIX shells by keeping track of files and directories you have accessed, so that you can quickly reference them in the command line.

## 📁 ShellSyncBackup
_... description of the subcategory ..._

* [SmartCd](nan) [❌ ❌ 🖥️CLI] - A cd command with improved usability features, which can remember your recently visited directory paths and, search and directly traverse to sub-directories and as well as parent directories, all with Fuzzy searching.

## 📁 SmartDirectoryNavigatorCLI
_... description of the subcategory ..._

* [zoxide](nan) [❌ ❌ 🖥️CLI] - It remembers which directories you use most frequently, so you can "jump" to them in just a few keystrokes.

## 📁 TerminalFileManager
_... description of the subcategory ..._

* [broot](https://dystroy.org/broot/) [❌ ❌ 🖥️TUI] - broot displays an optimized (omitting unnecessary content) tree view of the filesystem, allowing to fuzzy search files and folder, and move to specified directories.

## 📁 cd enhancement
_... description of the subcategory ..._

* [qcd](nan) [❌ ❌ 🖥️TUI] - A tool to change to another directory by just by entering commands like `qcd 3` and step back to where you came from with `qcd -o`. Frequently visited directories are stored in a sqlite3 database.

## 📁 cd enhancer
_... description of the subcategory ..._

* [navita](nan) [❌ ❌ 🖥️CLI] - A command-line tool for fast directory navigation in Bash & Zsh, ranking directories by frequency and recency. It enables quick fuzzy searches, recent history access, and smooth directory switching for efficient terminal workflows.
* [Shunpo](nan) [❌ ❌ 🖥️CLI] - A minimalist bash tool that makes directory navigation just a little bit faster.

## 📁 cd tool
_... description of the subcategory ..._

* [cdwe](nan) [❌ ❌ 🖥️CLI] - (cd with env vars) Wrapper of the cd command that sets and unsets env vars when you change dir based on a config file.

## 📁 directory jumper
_... description of the subcategory ..._

* [slingshot](nan) [❌ ❌ 🖥️CLI] - Lightweight command line tool to quickly navigate across folders.
* [zm](nan) [❌ ❌ 🖥️CLI] - Improved cd.

## 📁 directory jumpers
_... description of the subcategory ..._

* [z](nan) [❌ ❌ 🖥️CLI] - Directory changer based on aging and 'frecency'.
* [z.lua](nan) [❌ ❌ 🖥️CLI] - Directory changer that learns your habits.

## 📁 directory switcher
_... description of the subcategory ..._

* [menucd](nan) [❌ 🌐 🖥️TUI] - Directory browser and changer for the command line.

## 📁 enhanced cat
_... description of the subcategory ..._

* [fastdiract](nan) [❌ ❌ 🖥️CLI] - Lightning-fast cd and command execution.
* [Jmp](nan) [❌ ❌ 🖥️CLI] - Change directory with smart searching of the path specified through regex.
* [pazi](nan) [❌ ❌ 🖥️CLI] - Fast autojump helper.

## 📁 file browser
_... description of the subcategory ..._

* [nav](nan) [❌ ❌ 🖥️TUI] - Terminal navigator for interactive ls workflows.

## 📁 navigation tools
_... description of the subcategory ..._

* [autojump](nan) [❌ ❌ 🖥️CLI] - A cd command that maintains a database of most visited paths and allows the access to a directory with shortened versions of the path.

## 📁 path manager
_... description of the subcategory ..._

* [Apparition](nan) [❌ ❌ 🖥️CLI] - Apparition allows giving names to paths, so that moving to the specific path can be done by using the name; it also allows managing the list of assigned names.

## 📁 project switchers
_... description of the subcategory ..._

* [pm](nan) [❌ ❌ 🖥️CLI] - The easy way to switch between your projects on ZSH. In short, another directory changer.

## 📁 shell
_... description of the subcategory ..._

* [enhancd](nan) [❌ ❌ 🖥️CLI] - A next-generation cd command with your interactive filter.
* [ff](nan) [❌ ❌ 🖥️CLI] - ff is a command-line tool to manage favorite folders, creating an alias, to be used via shell directly with the cd command.

## 📁 shell completion
_... description of the subcategory ..._

* [fz](nan) [❌ ❌ 🖥️CLI] - Fuzzy tab completion for z.

# chat
[Back to TOC](#📚-contents)

Clients for chat and other instant messaging protocols, e.g., IRC, Discord, Mattermost, Matrix, Slack, Telegram, Reddit
## 📁 RedditClientTUI
_... description of the subcategory ..._

* [TUIR](nan) [❌ 🌐 🖥️TUI] - Text-based interface (TUI) to view and interact with Reddit from your terminal; TUIR is a fork of rtv, featuring vim keybindings and themes.

## 📁 SSHChatServerCLI
_... description of the subcategory ..._

* [ssh-chat](nan) [❌ 🌐 🖥️CLI] - Custom SSH server written in Go. Instead of a shell, you get a chat prompt.

## 📁 TerminalIRCClient
_... description of the subcategory ..._

* [tiny](nan) [❌ 🌐 🖥️TUI] - tiny is an IRC client written in Rust.

## 📁 TerminalMessenger
_... description of the subcategory ..._

* [finch](http://www.pidgin.im/) [❌ 🌐 🖥️TUI] - IM program supporting many protocols, including Yahoo!, AIM, IRC, or WLM; comes with the `Pidgin` project.
* [irssi](http://www.irssi.org) [❌ 🌐 🖥️TUI] - The most popular IRC client for the command-line; a flexible program, with many options and supporting many protocols.
* [WeeChat](http://weechat.org/) [❌ 🌐 🖥️TUI] - WeeChat is a fast, light and extensible chat client, with a text-based user interface, designed to be light and extensible: a lightweight core with optional plugins.

## 📁 TerminalTwitterClient
_... description of the subcategory ..._

* [RainbowStream](http://www.rainbowstream.org/) [❌ 🌐 🖥️TUI] - Twitter client for the terminal allows almost all the operations that can be done from GUI and Web clients.

## 📁 bbs client
_... description of the subcategory ..._

* [icy_tools](nan) [❌ ❌ 🖥️CLI] - Icy Term a terminal program for legacy BBS systems, Icy Draw a drawing tool supporting almost all ANSI formats, Icy View a viewer to browse/view Ansi screens, Icy Play a tool that shows icy draw animations on cmd line/bbs.

## 📁 chat
_... description of the subcategory ..._

* [cli_chat_app](nan) [🤖 🌐 🖥️TUI] - A end-to-end encrypted chat application.

## 📁 chat clients
_... description of the subcategory ..._

* [kirc](http://kirc.io/) [❌ 🌐 🖥️CLI] - A tiny IRC client written in POSIX C99.

## 📁 chat over ssh
_... description of the subcategory ..._

* [devzat](nan) [❌ ❌ 🖥️TUI] - Custom SSH server that takes you to a chat instead of a shell prompt.

## 📁 decentralized chat
_... description of the subcategory ..._

* [tweets](nan) [❌ 🌐 🖥️CLI] - Decentralized alternative to Twitter that uses git as support tool to manage the tweets.

## 📁 discord client
_... description of the subcategory ..._

* [Discordo](nan) [❌ 🌐 🖥️TUI] - A lightweight, secure, and feature-rich Discord terminal client.

## 📁 fediverse client
_... description of the subcategory ..._

* [Servitor](nan) [❌ 🌐 🖥️CLI] - A command-line Fediverse client that doesn’t require a server.

## 📁 irc client
_... description of the subcategory ..._

* [senpai](nan) [❌ 🌐 🖥️CLI] - A modern terminal IRC client.
* [sic](https://tools.suckless.org/sic/) [❌ 🌐 🖥️CLI] - sic is an extremely simple IRC client. It consists of less than 250 lines of code.

## 📁 mastodon client
_... description of the subcategory ..._

* [tut](nan) [❌ 🌐 🖥️TUI] - TUI for Mastodon with vim inspired keys.

## 📁 matrix client
_... description of the subcategory ..._

* [gomuks](nan) [❌ 🌐 🖥️TUI] - A terminal based Matrix client written in Go.
* [iamb](https://iamb.chat/) [❌ 🌐 🖥️CLI] - A Matrix client for the terminal that uses Vim keybindings.
* [matrix-commander](nan) [❌ 🌐 🖥️CLI] - Simple but convenient CLI-based Matrix client app for sending and receiving.
* [matrixcli](nan) [❌ 🌐 🖥️CLI] - A minimal command line matrix client.
* [Weechat-Matrix](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A Python script for Weechat that lets Weechat communicate over the Matrix protocol.

## 📁 messaging
_... description of the subcategory ..._

* [scli](nan) [❌ 🌐 🖥️TUI] - A simple terminal user interface for signal messenger.
* [tgbounce](nan) [❌ 🌐 🖥️CLI] - Simple Telegram Assistant that allows replying to messages, clicking buttons from bots, marking messages as read, logging notable messages, and providing desktop notifications, among other features.

## 📁 notification tools
_... description of the subcategory ..._

* [PingMe](nan) [❌ 🌐 🖥️CLI] - Sends messages or alerts to multiple messaging platforms & email, including Slack, Telegram, Mattermost, WeChat, and others.

## 📁 signal client
_... description of the subcategory ..._

* [signal-cli](nan) [❌ 🌐 🖥️CLI] - signal-cli provides an unofficial command-line, dbus and JSON-RPC interface for the Signal messenger.

## 📁 social clients
_... description of the subcategory ..._

* [toot](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - Mastodon CLI & TUI.

## 📁 telegram client
_... description of the subcategory ..._

* [Telegram messenger CLI](nan) [❌ 🌐 🖥️CLI] - Command-line interface for Telegram using the readline interface.

## 📁 terminal sharing
_... description of the subcategory ..._

* [matterhorn](nan) [❌ 🌐 🖥️TUI] - A terminal client for the Mattermost chat system.

## 📁 tox client
_... description of the subcategory ..._

* [toxic](nan) [❌ 🌐 🖥️TUI] - A Tox-based instant messaging and video chat client.

## 📁 twitch clients
_... description of the subcategory ..._

* [ttchat](nan) [❌ ❌ 🖥️TUI] - Twitch chats in the terminal.

## 📁 twitch tools
_... description of the subcategory ..._

* [twitch-tui](nan) [❌ 🌐 🖥️TUI] - Twitch chat in the terminal.

## 📁 xmpp client
_... description of the subcategory ..._

* [GNU Freetalk](https://www.gnu.org/software/freetalk/) [❌ 🌐 🖥️CLI 🖥️TUI] - A console based chat client for Jabber and other XMPP servers. It has context-sensitive autocompletion for buddy names, commands, and even ordinary English words.
* [MCABBER](https://mcabber.com/) [❌ 🌐 🖥️TUI] - A small XMPP (Jabber) console client including features such as SASL/SSL/TLS support, MUC (Multi-User Chat) support, history logging, command completion, OpenPGP encryption and more.
* [Poezio](https://poez.io/en/) [❌ 🌐 🖥️TUI] - Poezio is a free console XMPP client. It lets you connect very easily (no account creation needed) to the network and join various chatrooms. Many commands are identical to common IRC clients. Configuration can be made in a configuration file or directly from the client.
* [Profanity](https://profanity-im.github.io/) [❌ 🌐 🖥️TUI] - Profanity is a console based XMPP client written in C using ncurses and libstrophe, inspired by Irssi.

# cheatsheet
[Back to TOC](#📚-contents)

Tools to manage often used commands, code snippets, and alternative manual pages
## 📁 AliasGeneratorCLI
_... description of the subcategory ..._

* [topalias](nan) [❌ ❌ 🖥️CLI] - Linux alias generator from bash/zsh command history with statistics, written on Python.

## 📁 CommandExplainerCLI
_... description of the subcategory ..._

* [kmdr-cli](nan) [❌ 🌐 🖥️CLI] - The CLI tool for explaining commands from your terminal.

## 📁 FastFindAlternative
_... description of the subcategory ..._

* [tealdeer](nan) [❌ ❌ 🖥️CLI] - Very fast implementation of tldr in Rust.
* [tlrc](https://tldr.sh/tlrc/) [❌ ❌ 🖥️CLI] - Official tldr client written in Rust.

## 📁 InteractiveCheatsheetCLI
_... description of the subcategory ..._

* [navi](nan) [❌ ❌ 🖥️CLI] - An interactive cheatsheet tool for the command-line.

## 📁 TerminalHelpFetcher
_... description of the subcategory ..._

* [ehh](nan) [❌ ❌ 🖥️CLI] - Command-line tool for remembering Linux/terminal commands.

## 📁 autocomplete
_... description of the subcategory ..._

* [carapace](nan) [❌ ❌ 🖥️CLI] - Carapace provides argument completion for multiple CLI commands and works across multiple POSIX and non-POSIX shells.
* [IntelliShell](nan) [❌ ❌ 🖥️TUI] - Like IntelliSense, but for shells, acting like a bookmark store for commands.

## 📁 cheatsheets
_... description of the subcategory ..._

* [Wat](nan) [❌ ❌ 🖥️CLI] - Instant, central, community-built docs.

## 📁 cli assistant
_... description of the subcategory ..._

* [halp](nan) [❌ ❌ 🖥️CLI] - halp aims to help find the correct arguments for command-line tools by checking the predefined list of commonly used options/flags.

## 📁 command correctors
_... description of the subcategory ..._

* [The Fuck](nan) [🤖 ❌ 🖥️CLI] - Magnificent app which corrects your previous console command (although I would be extra-cautious at making a program to automatically infer what I was intending).

## 📁 command history
_... description of the subcategory ..._

* [MUC](nan) [❌ ❌ 🖥️TUI] - Visualize your most used commands.

## 📁 command-line translator
_... description of the subcategory ..._

* [eg](nan) [❌ ❌ 🖥️CLI] - Useful examples at the command line.

## 📁 devops notebook runner
_... description of the subcategory ..._

* [Runme](https://runme.dev/) [❌ 🌐 🖥️CLI] - DevOps notebooks built with Markdown.

## 📁 enhanced cat
_... description of the subcategory ..._

* [ManPDF & ManWEB](nan) [❌ 🌐 ❌] - Read your Man pages in PDF format. Even online!

## 📁 fuzzy finder
_... description of the subcategory ..._

* [docfd](nan) [❌ ❌ 🖥️TUI] - TUI fuzzy document finder that looks for documentation files in Markdown and txt format in the directory tree.

## 📁 fzf cheatsheet
_... description of the subcategory ..._

* [cheatshh](nan) [❌ ❌ 🖥️TUI] - A fzf based cheatsheet to store commands and their descriptions in a place you can look into so you dont have to remember them.

## 📁 fzf tools
_... description of the subcategory ..._

* [fzf-help](nan) [❌ ❌ 🖥️TUI] - An fzf extension that allows you to select command line options of a given command; the options are retrieved from the command its `--help` documentation.

## 📁 knowledge base
_... description of the subcategory ..._

* [cmdCompass](nan) [❌ ❌ 🖥️TUI] - Cross-platform terminal command manager/notebook with features like custom collections, tagging, variable substitution, and integrated man page with option highlighting.

## 📁 manuals
_... description of the subcategory ..._

* [tldr](https://tldr.sh/) [❌ 🌐 🖥️CLI] - Client for tldr pages, a community effort to simplify the beloved man pages with practical examples.

## 📁 script launcher
_... description of the subcategory ..._

* [tome](nan) [❌ ❌ 🖥️TUI] - Interactive Script playbooks for your terminal with Vim/Neovim (and Tmux).

## 📁 snippet manager
_... description of the subcategory ..._

* [Nap](nan) [❌ ❌ 🖥️CLI] - Code snippet manager that allows creating and access new snippets quickly with the command-line interface or browse, manage, and organize them with the text-user interface.
* [pet](nan) [❌ ❌ 🖥️CLI] - Pet is a simple command-line snippet manager, written in Go.
* [rsnip](nan) [❌ ❌ 🖥️TUI] - A powerful command-line snippet manager.
* [snip](nan) [❌ ❌ 🖥️TUI] - A simple and minimal command-line snippet manager.
* [snip](nan) [❌ ❌ 🖥️CLI] - A snippet manager for bash, mostly written in pure bash.

## 📁 table generator
_... description of the subcategory ..._

* [asciit](nan) [❌ ❌ 🖥️CLI] - A more compact and intuitive ASCII table in your terminal: an alternative to "man 7 ascii" and "ascii".

# conversion
[Back to TOC](#📚-contents)

File format converters
## 📁 DataFormatConverterCLI
_... description of the subcategory ..._

* [NestedTextTo](nan) [❌ ❌ 🖥️CLI] - CLI to convert between NestedText and JSON, YAML, or TOML.

## 📁 MultiFormatDocumentConverter
_... description of the subcategory ..._

* [Pandoc](http://pandoc.org/) [❌ ❌ 🖥️CLI] - Universal document file converter; handles input output from/to a number of formats: HTML, PDF, LaTeX, DOCX, ODT, AsciiDoc, Markdown, Textile, just to mention a few; the quality of conversion strongly depends on the combination of input/output formats.

## 📁 Translation
_... description of the subcategory ..._

* [BaFi](https://mmalcek.github.io/bafi/) [❌ ❌ 🖥️CLI] - Universal JSON, BSON, YAML, CSV, XML translator to ANY format using templates.

## 📁 WordToTextConverter
_... description of the subcategory ..._

* [catdoc](http://www.wagner.pp.ru/~vitus/software/catdoc/) [❌ ❌ 🖥️CLI] - Convert Microsoft Word files to plain text; output is sent to the standard output.
* [simtex](nan) [❌ ❌ 🖥️CLI] - simtex (simplified LaTeX) allows you to convert your Markdown or text lectures into LaTeX file with one command, configured with simple .json file.

## 📁 audio tools
_... description of the subcategory ..._

* [transflac](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A repository containing a series of utilities to assist in the maintenance and organization of FLAC based music collections.

## 📁 css tools
_... description of the subcategory ..._

* [scss-to-css](https://scsstocss.org) [❌ ❌ 🖥️CLI] - Recursively compile all SCSS files into minified CSS.

## 📁 data automation
_... description of the subcategory ..._

* [hecat](nan) [❌ ❌ 🖥️CLI] - A generic automation tool around data stored as plain-text YAML files.

## 📁 doc extractor
_... description of the subcategory ..._

* [wv](https://wvware.sourceforge.net/) [❌ ❌ 🖥️CLI] - Utility for performing operations on .doc files. The tool is now deprecated in favor of AbiWord, which uses the same library that is used in the CLI program.

## 📁 doc viewer
_... description of the subcategory ..._

* [antiword](https://web.archive.org/web/20071002133135/http://www.winfield.demon.nl/) [❌ ❌ 🖥️CLI] - Reader and converted for the proprietary MS .doc file format.

## 📁 document converter
_... description of the subcategory ..._

* [MarkItDown](nan) [❌ ❌ 🖥️TUI] - Python tool for converting files and office documents to Markdown.
* [unoserver](nan) [❌ ❌ 🖥️CLI] - Using LibreOffice as a server for converting documents, it allows converting multiple documents without loading libreoffice into memory every time.

## 📁 file conversion
_... description of the subcategory ..._

* [Vertopal-CLI](nan) [❌ ❌ 🖥️CLI] - Vertopal-CLI is a small, yet powerful utility for converting digital files to a variety of file formats using Vertopal public API.

## 📁 format converters
_... description of the subcategory ..._

* [hget](nan) [❌ ❌ 🖥️CLI] - A CLI to convert HTML into plain text. Can be used to fetch a site's HTML version and convert it into plain text, or to deliver plain text versions of your site dynamically.

## 📁 pdf converter
_... description of the subcategory ..._

* [markdrop](nan) [❌ ❌ 🖥️TUI] - Converts PDFs to markdown while extracting images and tables, generating descriptive text descriptions for extracted tables/images using several LLM clients.

## 📁 resume tools
_... description of the subcategory ..._

* [jsonify-resume](nan) [❌ ❌ 🖥️CLI] - A CLI that converts resumes into JSON Resume schema.

# copilot
[Back to TOC](#📚-contents)

Programs that use GPT and GPT-like engines to generate commands at the command line or code in general from natural language
## 📁 AI assistant
_... description of the subcategory ..._

* [Open Interpreter](nan) [🤖 ❌ 🖥️CLI] - OpenAI's Code Interpreter in your terminal, running locally.

## 📁 ai assistant
_... description of the subcategory ..._

* [Yai](nan) [🤖 ❌ 🖥️CLI] - Yai (your AI) is an assistant for your terminal, using OpenAI ChatGPT to build and run commands for you.

## 📁 ai coding assistant
_... description of the subcategory ..._

* [aider](nan) [🤖 🌐 🖥️CLI] - aider is AI pair programming in your terminal.

## 📁 chatgpt
_... description of the subcategory ..._

* [aido-cli](nan) [🤖 🌐 🖥️CLI] - Looks another interface to online GPT models to execute command through natural language. Very poor documentation and readme, though.

## 📁 chatgpt cli
_... description of the subcategory ..._

* [Commandpilot](nan) [🤖 🌐 🖥️CLI] - An assistant which uses ChatGPT to aid in constructing commands for bash.

## 📁 copilot
_... description of the subcategory ..._

* [gpt-do](nan) [🤖 🌐 🖥️CLI] - This is a handy-dandy CLI for when you don't know wtf to do; instead of furiously grepping through man pages, simply use do (or ddo if on bash/zsh), and have GPT-3 do all the magic for you.

## 📁 gpt assistant
_... description of the subcategory ..._

* [codemancer](https://0xmmo.github.io/codemancer/) [🤖 🌐 🖥️CLI] - Code with GPT-4 from your command line.

## 📁 gpt cli
_... description of the subcategory ..._

* [CLI Co-Pilot](nan) [🤖 🌐 🖥️CLI] - CLI tool that uses GPT4 to turn natural language commands into their Bash/ZShell/PowerShell equivalents.

## 📁 llama cli
_... description of the subcategory ..._

* [Llama Terminal Completion](nan) [🤖 ❌ 🖥️CLI] - Application that interacts with the llama.cpp library to provide virtual assistant capabilities through the command line. It allows you to ask questions and receive intelligent responses, as well as generate Linux commands based on your prompts.

## 📁 shell
_... description of the subcategory ..._

* [aish](nan) [❌ ❌ 🖥️CLI] - A program that retrieve shell script one-liners, ready to be executed in the terminal.

## 📁 shell assistant
_... description of the subcategory ..._

* [shy-sh](nan) [🤖 🌐 🖥️TUI] - Shell AI copilot.

# data-management
[Back to TOC](#📚-contents)

Tools to manage data files
## 📁 APIReaderCLI
_... description of the subcategory ..._

* [ROAPI](nan) [❌ 🌐 🖥️CLI] - ROAPI automatically spins up read-only APIs for static datasets without requiring you to write a single line of code.

## 📁 AsciiChartCLI
_... description of the subcategory ..._

* [lowcharts](nan) [❌ ❌ 🖥️CLI] - lowcharts is meant to be used in those scenarios where we have numerical data in text files that we want to display in the terminal to do a basic analysis.

## 📁 DataQueryCLI
_... description of the subcategory ..._

* [zq](https://zed.brimdata.io/docs/commands/zq/) [❌ 🌐 🖥️CLI] - A command-line tool that uses the Zed language for pipeline-style search and analytics. It can query a variety of data formats (CSV, JSON, etc.) in files, over HTTP, or in S3 storage.

## 📁 DateTimeProcessingCLI
_... description of the subcategory ..._

* [dateutils](http://www.fresse.org/dateutils/) [❌ ❌ 🖥️CLI] - Dateutils are a bunch of tools that revolve around fiddling with dates and times in the command line with a strong focus on use cases that arise when dealing with large amounts of financial data.

## 📁 RedisViewerTUI
_... description of the subcategory ..._

* [Redis Viewer](nan) [❌ 🌐 🖥️TUI] - A tool to view Redis data in terminal.

## 📁 TerminalDataVisualizer
_... description of the subcategory ..._

* [datadash](nan) [❌ ❌ 🖥️TUI] - Visualize and graph data in the terminal.

## 📁 TextDatabaseCLI
_... description of the subcategory ..._

* [GNU Recutils](https://www.gnu.org/software/recutils/manual/) [❌ ❌ 🖥️CLI] - Set of tools and libraries to access human-editable, text-based databases called recfiles.

## 📁 command-line translator
_... description of the subcategory ..._

* [osmf](nan) [❌ 🌐 🖥️CLI] - OpenStreetMap find - A simple command line tool to explore OSM data.

## 📁 data processing
_... description of the subcategory ..._

* [ramda-cli](nan) [❌ ❌ 🖥️CLI] - A tool for processing data with functional pipelines.

## 📁 database client
_... description of the subcategory ..._

* [redis_tui](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - Redis terminal browser application.

## 📁 dataset generator
_... description of the subcategory ..._

* [datasetGPT](nan) [🤖 🌐 🖥️CLI] - A command-line interface and a Python library for inferencing Large Language Models to generate textual datasets.

## 📁 enhanced cat
_... description of the subcategory ..._

* [gnuplot](https://www.explainshell.com/explain/1/gnuplot) [❌ ❌ 🖥️CLI] - Generate two and three-dimensional plots of data.

## 📁 process monitor
_... description of the subcategory ..._

* [crudini](nan) [❌ ❌ 🖥️CLI] - A utility for manipulating .ini files.

## 📁 shell
_... description of the subcategory ..._

* [IRedis](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Interactive Redis: A CLI for Redis with autocompletion and Syntax Highlighting.

## 📁 terminal dashboard
_... description of the subcategory ..._

* [sampler](nan) [❌ ❌ 🖥️TUI] - Sampler is a tool for shell commands execution, visualization, and alerting. Configured with a simple YAML file.

## 📁 terminal sharing
_... description of the subcategory ..._

* [WOPR](nan) [❌ ❌ 🖥️CLI] - A simple markup language for creating rich terminal reports, presentations, and infographic.

# data-management-json
[Back to TOC](#📚-contents)

Tools to manage data files, dedicated to JSON, YAML and other similar formats
## 📁 ImageViewer(ASCII)
_... description of the subcategory ..._

* [dasel](nan) [❌ ❌ 🖥️CLI] - Allows you to query and modify data structures using selector strings.

## 📁 JSONInspector
_... description of the subcategory ..._

* [jqview](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Simplest possible native GUI for inspecting JSON.

## 📁 JSONTransformerCLI
_... description of the subcategory ..._

* [jtc](nan) [❌ ❌ 🖥️CLI] - JSON manipulation and transformation.

## 📁 JSONViewerTUI
_... description of the subcategory ..._

* [jqp](nan) [❌ ❌ 🖥️TUI] - A TUI playground for exploring jq.

## 📁 advanced grep
_... description of the subcategory ..._

* [jiq](nan) [❌ ❌ 🖥️CLI] - jid on jq - interactive JSON query tool using jq expressions.
* [JSON-Grep](nan) [❌ ❌ 🖥️CLI] - JGrep is a command line tool and API for parsing JSON documents based on logical expressions.

## 📁 cli scripting
_... description of the subcategory ..._

* [jayin](nan) [❌ ❌ 🖥️CLI] - Piping with js at terminal.

## 📁 command-line translator
_... description of the subcategory ..._

* [fx](nan) [❌ ❌ 🖥️CLI] - Command-line JSON viewer.
* [Graphtage](nan) [❌ ❌ 🖥️CLI] - Graphtage is a command-line utility and underlying library for semantically comparing and merging tree-like structures, such as JSON, XML, HTML, YAML, plist, and CSS files.
* [jc](nan) [❌ ❌ 🖥️CLI] - Serializes the output of command line tools to JSON.
* [jless](https://pauljuliusmartinez.github.io/) [❌ ❌ 🖥️TUI] - Command-line JSON viewer designed for reading, exploring, and searching through JSON data.
* [yq](nan) [❌ ❌ 🖥️CLI] - Portable command-line YAML processor.

## 📁 enhanced cat
_... description of the subcategory ..._

* [gojq](nan) [❌ ❌ 🖥️CLI] - Pure Go implementation of jq.
* [jello](nan) [❌ ❌ 🖥️CLI] - CLI tool to filter JSON and JSON Lines data with Python syntax, similar to - surprise :-), jq!

## 📁 format converter
_... description of the subcategory ..._

* [faq](nan) [❌ ❌ 🖥️CLI] - Format Agnostic jQ - process various formats with libjq.

## 📁 json editor
_... description of the subcategory ..._

* [jj](nan) [❌ ❌ 🖥️CLI] - A command line utility that provides a fast and simple way to retrieve or update values from JSON documents.
* [jsed](nan) [❌ ❌ 🖥️CLI] - jsed is a small command-line utility to add, remove, and search for data in a JSON structure.

## 📁 json filter
_... description of the subcategory ..._

* [jsongrep](nan) [❌ ❌ 🖥️CLI] - A shell tool to search and select bits out of JSON documents.

## 📁 json formatter
_... description of the subcategory ..._

* [gron](nan) [❌ ❌ 🖥️CLI] - gron transforms JSON into discrete assignments to make it easier to grep for what you want and see the absolute 'path' to it.
* [json](nan) [❌ ❌ 🖥️CLI] - A "json" command for massaging JSON on your Unix command line.
* [jsonpp](nan) [❌ ❌ 🖥️CLI] - A fast command line JSON pretty printer.

## 📁 json generator
_... description of the subcategory ..._

* [jo](nan) [❌ ❌ 🖥️CLI] - A small utility to create JSON objects from the command line.

## 📁 json parser
_... description of the subcategory ..._

* [JSON.awk](nan) [❌ ❌ 🖥️TUI] - A practical JSON parser written in awk.

## 📁 json processor
_... description of the subcategory ..._

* [Jsawk](nan) [❌ ❌ 🖥️CLI] - Like awk, but for JSON. You work with an array of JSON objects read from stdin, filter them using JavaScript to produce a results array that is printed to stdout.
* [RecordStream](nan) [❌ ❌ 🖥️TUI] - Command-line tools for slicing and dicing JSON records.

## 📁 json processors
_... description of the subcategory ..._

* [jp](nan) [❌ ❌ 🖥️CLI] - A command line interface to JMESPath, an expression language for manipulating JSON.

## 📁 json query
_... description of the subcategory ..._

* [jp](nan) [❌ ❌ 🖥️TUI] - A tiny command-line tool for parsing JSON from any source.

## 📁 json query tools
_... description of the subcategory ..._

* [GROQ](nan) [❌ ❌ 🖥️CLI] - The CLI tool consumes both JSON and NDJSON documents. You can pass in data from a local file, or from piping to standard input.

## 📁 json search
_... description of the subcategory ..._

* [jsongrep](nan) [❌ ❌ 🖥️CLI] - Python for extracting pieces of JSON objects

## 📁 json table
_... description of the subcategory ..._

* [jtbl](nan) [❌ ❌ 🖥️CLI] - A simple CLI tool to print JSON and JSON Lines data as a table in the terminal.

## 📁 json toolkit
_... description of the subcategory ..._

* [JSON Command](nan) [❌ ❌ 🖥️TUI] - JSON command line processing toolkit: no more writing code to inspect or transform JSON objects.

## 📁 json tools
_... description of the subcategory ..._

* [jid](nan) [❌ ❌ 🖥️TUI] - You can drill down JSON interactively by using filtering queries like jq.
* [jl](nan) [❌ ❌ 🖥️CLI] - jl ("JSON lambda") is a tiny functional language for querying and manipulating JSON.
* [underscore-cli](nan) [❌ ❌ 🖥️CLI] - Command-line utility-belt for hacking JSON and JavaScript.

## 📁 json viewer
_... description of the subcategory ..._

* [jnv](nan) [❌ ❌ 🖥️TUI] - Interactive JSON filter using jq.

## 📁 json viewers
_... description of the subcategory ..._

* [vj](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - JSON Humanizer makes JSON human-readable by applying visual formatting.

## 📁 json-processing
_... description of the subcategory ..._

* [jaq](nan) [❌ ❌ 🖥️CLI] - jaq is a clone of the JSON data processing tool jq, that aims to support a large subset of jq's syntax and operations.
* [jq](https://stedolan.github.io/jq/) [❌ ❌ 🖥️CLI] - (JSON Query?) - sed-like processor for JSON data; can be used to process JSON files and data streams and perform operations such as those allowed by `cat`, `sed`, `grep` and `awk` on regular text files.

## 📁 json-yaml converter
_... description of the subcategory ..._

* [jsonv.sh](nan) [❌ ❌ 🖥️TUI] - A Bash command line tool for converting JSON to CSV.

## 📁 record analysis
_... description of the subcategory ..._

* [rq](nan) [❌ ❌ 🖥️CLI] - Record Query - A tool for doing record analysis and transformation.

## 📁 shell
_... description of the subcategory ..._

* [jshon](nan) [❌ ❌ 🖥️CLI] - Jshon is a JSON parser designed for maximum convenience within the shell.
* [JSON.sh](nan) [❌ ❌ 🖥️CLI] - A JSON parser written in shell, compatible with ash, bash, dash and zsh.

## 📁 task management
_... description of the subcategory ..._

* [TickTick](nan) [❌ ❌ 🖥️CLI] - TickTick enables you to put JSON in bash scripts. Yes, just encapsulate them with two back-ticks.

## 📁 yaml tools
_... description of the subcategory ..._

* [YAML Paths](nan) [❌ ❌ 🖥️CLI] - YAML/JSON/EYAML/Compatible get/set/merge/validate/scan/convert/diff processors using powerful, intuitive, command-line friendly syntax.

# data-management-tabular
[Back to TOC](#📚-contents)

Tools to manage tabular data files, such as CSV, spreadsheets, and database tables
## 📁 CSVProcessingCLI
_... description of the subcategory ..._

* [csvkit](nan) [❌ ❌ 🖥️CLI] - A suite of command-line tools for converting to and working with CSV, the king of tabular file formats.

## 📁 CSVProcessorCLI
_... description of the subcategory ..._

* [csvtk](https://bioinf.shenwei.me/csvtk/) [❌ ❌ 🖥️CLI] - A cross-platform, efficient and practical CSV/TSV toolkit written in Go.

## 📁 CSVQueryCLI
_... description of the subcategory ..._

* [xsv](https://www.johndcook.com/blog/2019/12/31/sql-join-csv-files/) [❌ ❌ 🖥️CLI] - Doing a SQL join with CSV files.

## 📁 DatabaseManagerTUI
_... description of the subcategory ..._

* [termdbms](nan) [❌ ❌ 🖥️TUI] - A TUI for viewing and editing databases, written in pure Go.

## 📁 GitStatistics
_... description of the subcategory ..._

* [csvq](nan) [❌ ❌ 🖥️CLI] - SQL-like query language for CSV.

## 📁 SQLClientCLI
_... description of the subcategory ..._

* [mycli](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A command line client for MySQL that can do autocompletion and syntax highlighting.
* [pgcli](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Postgres CLI with autocompletion and syntax highlighting.
* [usql](nan) [❌ ❌ 🖥️CLI] - Universal command-line interface for PostgreSQL, MySQL, Oracle Database, SQLite3, Microsoft SQL Server, and others, including NoSQL and non-relational databases.

## 📁 SQLGitDatabase
_... description of the subcategory ..._

* [Dolt](nan) [❌ 🌐 🖥️CLI] - Dolt is Git for Data! Dolt is a SQL database that you can fork, clone, branch, merge, push and pull just like a git repository.

## 📁 TSVProcessingCLI
_... description of the subcategory ..._

* [TSV Utilities](nan) [❌ ❌ 🖥️CLI] - Command line tools for large, tabular data files.

## 📁 TabularDataTUI
_... description of the subcategory ..._

* [VisiData](https://www.visidata.org/) [❌ ❌ 🖥️TUI] - Interactive multitool for tabular data. It combines the clarity of a spreadsheet, the efficiency of the terminal, and the power of Python, into a lightweight utility which can handle millions of rows with ease.

## 📁 cli client
_... description of the subcategory ..._

* [pykli](nan) [❌ ❌ 🖥️CLI] - Interactive ksqlDB command line client with autocompletion and syntax highlighting written in Python.

## 📁 command-line translator
_... description of the subcategory ..._

* [sq](nan) [❌ ❌ 🖥️CLI] - Command line tool that provides jq-style access to structured data sources such as SQL databases, or document formats like CSV or Excel.
* [tabview](nan) [❌ ❌ 🖥️TUI] - Python curses command line CSV and tabular data viewer.

## 📁 csv tool
_... description of the subcategory ..._

* [csvsuite](nan) [❌ ❌ 🖥️CLI] - A suite of tools to process CSV files, written in C++.

## 📁 csv tools
_... description of the subcategory ..._

* [daff](nan) [❌ ❌ 🖥️CLI] - Efficient table comparison and alignment, supporting formats like CSV and SQLite, useful for data analysis and synchronization tasks.
* [qsv](nan) [❌ ❌ 🖥️CLI] - CSVs sliced, diced & analyzed.
* [textql](nan) [❌ ❌ 🖥️CLI] - Execute SQL against structured text like CSV or TSV.

## 📁 csv viewer
_... description of the subcategory ..._

* [csvlens](nan) [❌ ❌ 🖥️TUI] - CSV file viewer; like `less` but made for CSV.
* [tabiew](nan) [❌ ❌ 🖥️TUI] - A lightweight, terminal-based application to view and query delimiter separated value formatted documents, such as CSV or TSV files.

## 📁 database manager
_... description of the subcategory ..._

* [gobang](nan) [❌ ❌ 🖥️TUI] - A cross-platform TUI database management tool written in Rust.
* [rainfrog](nan) [❌ ❌ 🖥️TUI] - A database management tui for PostGres.

## 📁 enhanced cat
_... description of the subcategory ..._

* [TV](nan) [❌ ❌ 🖥️TUI] - Cross-platform CSV pretty printer made to maximize viewer enjoyment.

## 📁 json-processing
_... description of the subcategory ..._

* [Miller](nan) [❌ ❌ 🖥️CLI] - Miller is like awk, sed, cut, join, and sort for data formats such as CSV, TSV, JSON, JSON Lines, and positionally-indexed.

## 📁 sql tools
_... description of the subcategory ..._

* [YAS-QWIN](nan) [❌ ❌ 🖥️CLI] - YAS-QWIN (Yet Another SQL-Query Writing Interface) is a CLI tool for building (and optionally running) SQL queries.

## 📁 sql tui
_... description of the subcategory ..._

* [harlequin](nan) [❌ ❌ 🖥️TUI] - The SQL IDE for Your Terminal.

## 📁 sql-on-csv
_... description of the subcategory ..._

* [q](http://harelba.github.io/q/) [❌ ❌ 🖥️CLI] - Execute SQL-like queries on CSVs/TSVs tabular data files; each tabular file is treated as a database table; supports all SQL constructs (`WHERE`, `GROUP BY`, `JOIN`).

## 📁 sqlite
_... description of the subcategory ..._

* [sqlite-utils](nan) [❌ ❌ 🖥️CLI] - Python CLI utility and library for manipulating SQLite databases.

## 📁 sqlite client
_... description of the subcategory ..._

* [litecli](nan) [❌ ❌ 🖥️CLI] - CLI for SQLite Databases with autocompletion and syntax highlighting.

## 📁 sqlite server
_... description of the subcategory ..._

* [Soul](nan) [❌ 🌐 🖥️CLI] - A SQLite REST and real-time server.

# devops
[Back to TOC](#📚-contents)

Applications for supporting DevOps tasks, such as containers or cloud systems management
## 📁 DevEnvironmentManager
_... description of the subcategory ..._

* [Devbox](nan) [❌ ❌ 🖥️CLI] - Devbox is a command-line tool that lets you easily create isolated shells and containers by defining the list of packages required by the environment.

## 📁 aws cli
_... description of the subcategory ..._

* [SAWS](nan) [❌ ❌ 🖥️TUI] - A supercharged AWS command line interface (CLI).

## 📁 build tools
_... description of the subcategory ..._

* [mkdkr](nan) [❌ ❌ 🖥️CLI] - Super small and powerful framework for build CI pipeline, scripted with Makefile and isolated with docker.

## 📁 cloud clients
_... description of the subcategory ..._

* [planor](nan) [❌ 🌐 🖥️TUI] - The Cloud Aviator: TUI client for cloud services (AWS, Vultr, Heroku, Render.com, Fleek, ...).

## 📁 kubectl context switcher
_... description of the subcategory ..._

* [kubectx](https://kubectx.dev/) [❌ ❌ 🖥️CLI] - Quickly switch between clusters and namespaces in kubectl.

## 📁 kubernetes
_... description of the subcategory ..._

* [k9s](nan) [❌ ❌ 🖥️TUI] - Kubernetes CLI To Manage Your Clusters In Style!

## 📁 kubernetes log viewer
_... description of the subcategory ..._

* [stern](nan) [❌ ❌ 🖥️TUI] - Multi pod and container log tailing for Kubernetes.

## 📁 unikernel
_... description of the subcategory ..._

* [OPS](nan) [❌ 🌐 🖥️CLI] - Ops is a tool for creating and running a [Nanos](https://github.com/nanovms/nanos) unikernel. It is used to package, create, and run your application as a [Nanos](https://github.com/nanovms/nanos) unikernel instance.

# diff
[Back to TOC](#📚-contents)

Calculation of diffs between files and data, even with context or semantic awareness (i.e., considering the meaning of the data)
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [Difftastic](nan) [❌ ❌ 🖥️CLI] - Syntax-aware structured diff tool.

## 📁 GitStatistics
_... description of the subcategory ..._

* [diff2html-cli](nan) [❌ ❌ 🖥️CLI] - Parse git diffs as JSON and generate pretty HTML.

## 📁 PDFDiffTool
_... description of the subcategory ..._

* [pdf-diff](nan) [❌ ❌ 🖥️CLI] - A tool for visualizing differences between two PDF files. Mainly dedicated to editors that usually spends a lot of hours on several PDFs.

## 📁 csv comparison
_... description of the subcategory ..._

* [csv-diff](nan) [❌ ❌ 🖥️CLI] - Python CLI tool and library for diffing CSV and JSON files

## 📁 diff visualizer
_... description of the subcategory ..._

* [sesdiff](nan) [❌ ❌ 🖥️TUI] - Generates a shortest edit script (Myers' diff algorithm) to indicate how to get from the strings in column A to the strings in column B. Also provides the edit distance (levenshtein).

## 📁 directory diff
_... description of the subcategory ..._

* [Dirdiff](nan) [❌ ❌ 🖥️CLI] - Efficiently compute the differences between two directories.

## 📁 enhanced cat
_... description of the subcategory ..._

* [delta](nan) [❌ ❌ 🖥️CLI] - A syntax-highlighter for git and diff output.
* [diff-so-fancy](nan) [❌ ❌ 🖥️CLI] - Make your diffs human-readable instead of machine-readable.
* [ydiff](nan) [❌ ❌ 🖥️CLI] - View colored, incremental diff.

## 📁 string distance
_... description of the subcategory ..._

* [leven-cli](nan) [❌ ❌ 🖥️CLI] - Measure the difference between two strings using the Levenshtein distance algorithm.

## 📁 yaml diff
_... description of the subcategory ..._

* [dyff](nan) [❌ ❌ 🖥️CLI] - A diff tool for YAML files, and sometimes JSON.

# disk-analyzer
[Back to TOC](#📚-contents)

Programs to analyze and summarize the usage of disks, visualize and report the size of directories and sub-directories, etc.
## 📁 DiskAnalyzerTUI
_... description of the subcategory ..._

* [gdu](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Pretty fast disk usage analyzer written in Go. Gdu is intended primarily for SSD disks where it can fully utilize parallel processing. However, HDDs work as well, but the performance gain is not so huge.

## 📁 DiskUsageHistogram
_... description of the subcategory ..._

* [cdu](http://arsunik.free.fr/prog/cdu.html) [❌ ❌ 🖥️CLI] - (colored `du`) - a Perl script that calls `du` and displays a pretty histogram with optional colors allowing to immediately see the directories which take most disk space.

## 📁 FastFindAlternative
_... description of the subcategory ..._

* [diskus](nan) [❌ ❌ 🖥️CLI] - Minimal, fast alternative to du -sh.
* [Dust](nan) [❌ ❌ 🖥️CLI] - du + rust = dust. Like du but more intuitive.

## 📁 NcursesDiskAnalyzer
_... description of the subcategory ..._

* [diskonaut](nan) [❌ ❌ 🖥️TUI] - Terminal disk space navigator that traverse the file-system with a TUI interface.
* [ncdu](https://dev.yorhel.nl/ncdu) [❌ ❌ 🖥️TUI] - "A disk usage analyzer with a ncurses interface. It is designed to find space hogs on a remote server where you don't have an entire graphical setup available."

## 📁 StylizedDiskUsageReporter
_... description of the subcategory ..._

* [dfc](nan) [❌ ❌ 🖥️CLI] - Report file system space usage information with style.
* [dua](nan) [❌ ❌ 🖥️CLI] - Disk Usage Analyzer. Learn about the usage of disk space of a given directory with parallel access to max out SSD exploration.
* [duf](nan) [❌ ❌ 🖥️TUI] - Disk Usage/Free Utility.
* [dutree](nan) [❌ ❌ 🖥️TUI] - A tool to analyze file system usage written in Rust.
* [erdtree](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A multithreaded file-tree visualizer and disk usage analyzer.
* [vizex](nan) [❌ ❌ 🖥️TUI] - Visualize the disk space usage for every partition and media on the user's machine.

# editors
[Back to TOC](#📚-contents)

Text editors
## 📁 NoteTakingTUI
_... description of the subcategory ..._

* [Feather](https://www.feathereditor.com/) [❌ ❌ 🖥️TUI] - The only terminal based text editor designed to work with BIG files.

## 📁 TUIEditor
_... description of the subcategory ..._

* [Diakonos](nan) [❌ ❌ 🖥️TUI] - A powerful editor with “standard" keybindings and several advanced features; written in Ruby.

## 📁 TerminalEditor
_... description of the subcategory ..._

* [zee](nan) [❌ ❌ 🖥️TUI] - Zee is a modern editor for the terminal, in the spirit of Emacs. It is written in Rust and it is somewhat experimental.

## 📁 TerminalTextEditor
_... description of the subcategory ..._

* [eon](nan) [❌ ❌ 🖥️TUI] - A light, modern editor for your terminal that doesn't want to be vim.
* [vy](nan) [❌ ❌ 🖥️TUI] - A vim-like in Python made from scratch.

## 📁 TextEditorTUI
_... description of the subcategory ..._

* [Helix](nan) [❌ ❌ 🖥️TUI] - A Kakoune / Neovim inspired editor, written in Rust. The editing model is very heavily based on Kakoune.
* [Tilde](https://os.ghalkes.nl/tilde/) [❌ ❌ 🖥️TUI] - Tilde is a text editor that provides an intuitive interface for people accustomed to GUI environments, usual shortcuts for common operation, a traditional menu bar, etc.

## 📁 advanced-extensible
_... description of the subcategory ..._

* [Emacs](https://www.gnu.org/software/emacs/) [❌ ❌ 🖥️CLI 🖥️TUI] - One of the oldest text editors, free long-standing software project, with a huge amount of functionalities and extensions; implemented and extendable with E-Lisp.

## 📁 gui-easy-editor
_... description of the subcategory ..._

* [aretext](nan) [❌ ❌ 🖥️TUI] - Minimalist text editor with vim-compatible key bindings.
* [ash](nan) [❌ ❌ 🖥️TUI] - A simple and clean terminal-based text editor, that aims to be easy to use with modern key-bindings.
* [jed](http://www.jedsoft.org/jed/index.html) [❌ ❌ 🖥️TUI] - A text editor with a drop-down menu facility that make it especially user-friendly.
* [Kakoune](http://kakoune.org/) [❌ ❌ 🖥️TUI] - Modal editor, faster as in less keystrokes, multiple selections, orthogonal design.
* [VE](http://www.inverary.net/ve/ve.html) [❌ ❌ 🖥️CLI] - Lean, fast and feature rich text editor.

## 📁 gui-sublime-inspired
_... description of the subcategory ..._

* [slap](nan) [❌ ❌ 🖥️TUI] - Text editor inspired by [Sublime Text](https://www.sublimetext.com/) written in NodeJS, extendable in JavaScript.

## 📁 lightweight-stable
_... description of the subcategory ..._

* [joe](http://joe-editor.sourceforge.net/) [❌ ❌ 🖥️TUI] - (Joe's Own Editor) - a compact text editor written in C, a detailed list of features and missing ones is explicitly reported on the website. This editor is mentioned in several web sources for its capability in handling large files.

## 📁 lightweight-userfriendly
_... description of the subcategory ..._

* [nano](https://www.nano-editor.org/) [❌ ❌ 🖥️TUI] - Easy to use, lightweight text editor; no complex keybindings to remember; the main ones are shown in the main menu.

## 📁 line editor
_... description of the subcategory ..._

* [ed](https://www.gnu.org/software/ed/) [❌ ❌ 🖥️CLI] - GNU ed is a line-oriented text editor. It is used to create, display, modify and otherwise manipulate text files, both interactively and via shell scripts.

## 📁 minimalist-writing
_... description of the subcategory ..._

* [WordGrinder](https://cowlark.com/wordgrinder/) [❌ ❌ 🖥️TUI] - From the website: "WordGrinder is a word processor for processing words. It is not WYSIWYG. It is not point and click. It is not a desktop publisher. It is not a text editor. It does not do fonts and it barely does styles. What it does do is words. It's designed for writing text. It gets out of your way and lets you type." 

## 📁 modal-powerful
_... description of the subcategory ..._

* [neovim](https://neovim.io/) [❌ ❌ 🖥️CLI 🖥️TUI] - A work in progress attempt to improve [vim](http://www.vim.org/), dropping older/unused OS compatibility, improving the codebase readability, modularity, and maintainability; it has chances to become the next choice of vim users.

## 📁 modal-traditional
_... description of the subcategory ..._

* [vim](http://www.vim.org/) [❌ ❌ 🖥️CLI 🖥️TUI] - Historically one of the preferred text editors, behavior based on editing modes, plenty of plugins and tips to address every possible editing problem.

## 📁 modern-nano-like
_... description of the subcategory ..._

* [micro](nan) [❌ ❌ 🖥️TUI] - Aims to be a successor to [`nano`](https://www.nano-editor.org/). Aiming to be easy to use, it has a nano-like keybindings menu; also takes advantage of the full capabilities of modern terminals, supports mutiple cursors, and has a plugin system. Written in Go.

## 📁 neovim frontend
_... description of the subcategory ..._

* [Bob](nan) [❌ ❌ 🖥️CLI] - Bob is a cross-platform and easy-to-use Neovim version manager, allowing for easy switching between versions.

## 📁 text editor
_... description of the subcategory ..._

* [edit](nan) [❌ ❌ 🖥️CLI] - This editor pays homage to the classic MS-DOS Editor, but with a modern interface and input controls similar to VS Code.
* [o](nan) [❌ ❌ 🖥️CLI] - Configuration-free text editor and IDE limited to VT100. Suitable for writing git commit messages, editing Markdown, config files, source code, viewing man pages and for quick edit-compile cycles when programming.
* [ox](nan) [❌ ❌ 🖥️TUI] - An independent Rust text editor.

## 📁 vim-inspired-minimal
_... description of the subcategory ..._

* [vis](nan) [❌ ❌ 🖥️TUI] - "a modern, legacy free, simple yet efficient vim-like editor", and more: "The intention is not to be bug for bug compatible with vim, instead a similar editing experience should be provided. The goal could thus be summarized as 80% of vim's features implemented in roughly 1% of the code"; the editor is scriptable in LUA and supports editing large files.

## 📁 vim-like-lightweight
_... description of the subcategory ..._

* [vai](nan) [❌ ❌ 🖥️TUI] - Text editor similar to `vim` written in Python; many features are nicely replicated, some are still missing; however, the advantage of this implementation is its simplicity, maintainability and extensibility, thanks to the Python implementation.

# email
[Back to TOC](#📚-contents)

Email clients (MUA - Mail User Agents), mail synchronization, generation indexing and search
## 📁 EmailGeneratorCLI
_... description of the subcategory ..._

* [pymailgen](nan) [❌ ❌ 🖥️CLI] - Starting from the content of a CSV file and a template text file, pymailgen generates a list of emails to be sent out using a command-line SMTP client.

## 📁 MailSyncTool
_... description of the subcategory ..._

* [mbsync](http://isync.sourceforge.net/mbsync.html) [❌ ❌ 🖥️CLI] - Mailboxes synchronization tool, allows downloading email locally, MailDir format supported.

## 📁 TemporaryEmailCLI
_... description of the subcategory ..._

* [tmpmail](nan) [❌ ❌ 🖥️CLI] - A command line utility written in POSIX sh that allows you to create a temporary email address and receive emails to the temporary email address.

## 📁 TerminalEmailClient
_... description of the subcategory ..._

* [alot](nan) [❌ ❌ 🖥️TUI] - MUA written in Python using the [NotMuch](https://notmuchmail.org/) backend, MailDir format support.
* [alpine](http://www.washington.edu/alpine/) [❌ ❌ 🖥️TUI] - Mail client which aims at being "fast, easy to use email client that is suitable for both the inexperienced email user as well as for the most demanding of power users".
* [Mutt](http://www.mutt.org/) [❌ ❌ 🖥️CLI 🖥️TUI] - Mail client with tons of features, customization chances, support for IMAP, POP3, multiple storage formats.
* [NeoMutt](https://neomutt.org/) [❌ 🌐 🖥️TUI] - Patched and up-to-dated mutt fork.
* [sup](http://sup-heliotrope.github.io/) [❌ ❌ 🖥️TUI] - MUA written in Ruby; specifically developed for accounts with "a lot of emails"; nice thread-based presentation.

## 📁 cli email
_... description of the subcategory ..._

* [Himalaya](nan) [❌ ❌ 🖥️CLI] - Command-line interface for email management.

## 📁 disposable email
_... description of the subcategory ..._

* [mailsy](nan) [❌ 🌐 🖥️CLI] - Generates disposable emails in the CLI through [mail.tm](https://mail.tm).

## 📁 email alias manager
_... description of the subcategory ..._

* [quackalias-cli](nan) [❌ ❌ 🖥️CLI] - Scripts to generate DuckDuckGo email aliases and store the history of generated aliases.

## 📁 email analyzer
_... description of the subcategory ..._

* [maildir-rank-addr](nan) [❌ ❌ 🖥️CLI] - Creates a ranked list of email addresses from local email files, which can be used for address completion for example in aerc.

## 📁 email client
_... description of the subcategory ..._

* [aerc](https://aerc-mail.org/) [❌ 🌐 🖥️TUI] - A pretty good email client
* [meli](nan) [❌ 🌐 🖥️TUI] - Terminal mail client.
* [pop](nan) [❌ 🌐 🖥️CLI] - Send emails from your terminal; it uses the API at [https://resend.com/](resend.com).

## 📁 email tools
_... description of the subcategory ..._

* [Notmuch](nan) [❌ ❌ 🖥️CLI] - Notmuch is a command-line based program for indexing, searching, reading, and tagging large collections of email messages.

## 📁 resource monitor
_... description of the subcategory ..._

* [nmail](nan) [❌ 🌐 🖥️TUI] - nmail is a console-based email client for Linux and macOS with a user interface similar to alpine / pine.

## 📁 slack mail interface
_... description of the subcategory ..._

* [paws](nan) [❌ ❌ 🖥️TUI] - sendmail/maildir interface to Slack.

# file-dir-cleanup
[Back to TOC](#📚-contents)

Find/remove duplicate files, automatically organize files, etc.
## 📁 DirectoryOrganizer
_... description of the subcategory ..._

* [classifier](nan) [❌ ❌ 🖥️CLI] - Organize files in your current directory, by classifying them into folders of music, PDFs, images, etc.

## 📁 DuplicateFileFinder
_... description of the subcategory ..._

* [rmlint](nan) [❌ ❌ 🖥️CLI] - Recursively scan a directory tree looking for duplicate and broken files; it outputs statistics and save the list of files in JSON format and produces a shell script that can be inspected before running it to delete the desire files.

## 📁 FilenameSanitizer
_... description of the subcategory ..._

* [detox](https://github.com/dharple/detox) [❌ ❌ 🖥️CLI] - Easily clean up filenames; it replaces characters like spaces with standard equivalents and UTF-8 or Latin-1 (or CP 1252) characters with more handy ones.

## 📁 ModernFileManager
_... description of the subcategory ..._

* [FClones](nan) [❌ ❌ 🖥️CLI] - Efficient Duplicate File Finder.

## 📁 deduplication
_... description of the subcategory ..._

* [smash](nan) [❌ ❌ 🖥️CLI] - Smash through to find duplicate files super fast by slicing files intelligently.

## 📁 directory organizer
_... description of the subcategory ..._

* [Dext](nan) [❌ ❌ 🖥️CLI] - (Directories by Extensions) is a script that moves (or copies) files of the same extension into a folder.

## 📁 duplicate finder
_... description of the subcategory ..._

* [duple](nan) [❌ ❌ 🖥️CLI] - Find and remove duplicate files.

## 📁 file cleanup
_... description of the subcategory ..._

* [czkawka](https://qarmin.github.io/czkawka/) [❌ ❌ 🖥️CLI] - Remove unnecessary files from your computer

## 📁 file deduplication
_... description of the subcategory ..._

* [backdown](nan) [❌ ❌ 🖥️CLI] - Safely and ergonomically remove duplicate files

## 📁 file organizers
_... description of the subcategory ..._

* [organize-cli](nan) [❌ ❌ 🖥️CLI] - Organize your files automatically.

## 📁 folder organizer
_... description of the subcategory ..._

* [Framed](nan) [❌ ❌ 🖥️CLI] - A CLI tool that simplifies the organization and management of files and directories in a reusable and architectural manner.

## 📁 gamified file manager
_... description of the subcategory ..._

* [inventory](nan) [❌ ❌ 🖥️TUI] - Move files like an old text adventure.

## 📁 metadata remover
_... description of the subcategory ..._

* [mat2](nan) [❌ ❌ 🖥️CLI] - Metadata removal tool, supporting a wide range of commonly used file formats.

# file-explorer
[Back to TOC](#📚-contents)

Show directory trees and navigate through the file system (but not full-featured file managers)
## 📁 DirectoryTreePrinter
_... description of the subcategory ..._

* [tree](http://mama.indstate.edu/users/ice/tree/) [❌ ❌ 🖥️CLI] - Recursive directory listing command that produces a depth indented list of files.

## 📁 ModernFileManager
_... description of the subcategory ..._

* [twf](nan) [❌ ❌ 🖥️TUI] - Standalone tree view file explorer.
* [xplr](nan) [❌ ❌ 🖥️TUI] - A hackable, minimal, fast TUI file explorer, stealing ideas from nnn and fzf.

## 📁 directory viewers
_... description of the subcategory ..._

* [tre](nan) [❌ ❌ 🖥️TUI] - `tree` command improved with git awareness, editor aliasing, and colors.

## 📁 enhanced cat
_... description of the subcategory ..._

* [alder](nan) [❌ ❌ 🖥️CLI] - Directory tree visualizer.

## 📁 file browser
_... description of the subcategory ..._

* [kupo](nan) [❌ 🌐 🖥️TUI] - A terminal file browser, kupo!

## 📁 file explorer
_... description of the subcategory ..._

* [Hop!](nan) [❌ ❌ 🖥️TUI] - File explorer designed to be fast, simple and user-friendly, running on any operating system.

## 📁 file manager
_... description of the subcategory ..._

* [browsr](nan) [❌ 🌐 🖥️TUI] - A pleasant file explorer that can browse the contents of local and remote filesystems with your keyboard or mouse; remotes include GitHub, over SSH, in AWS S3, Google Cloud Storage, or Azure Blob Storage.
* [Rust-Traverse](nan) [❌ ❌ 🖥️TUI] - Rust traverse is a terminal based file explorer. It is inspired by the NNN file manager. It uses Ratatui for the terminal UI, with Crossterm for the terminal backend.

## 📁 terminal file explorer
_... description of the subcategory ..._

* [ictree](nan) [❌ ❌ 🖥️TUI] - Like tree but interactive.

## 📁 tui file explorer
_... description of the subcategory ..._

* [tere](nan) [❌ ❌ 🖥️TUI] - Terminal file explorer that is a faster alternative to using cd and ls to browse folders in your terminal.

# file-handling
[Back to TOC](#📚-contents)

Tools for managing files and directories (copy, move, extraction from compressed archives, change permissions, etc.)
## 📁 ArchiveAutoExtractor
_... description of the subcategory ..._

* [dtrx](https://brettcsmith.org/2007/dtrx/) [❌ ❌ 🖥️CLI] - (Do The Right eXtraction) aims at taking "all the hassle out of extracting archives"; allows using one command to extract archives in different formats, recursive extraction (files into file) and extracts files into dedicated directories.

## 📁 FileInspectorCLI
_... description of the subcategory ..._

* [file-type-cli](nan) [❌ ❌ 🖥️CLI] - Detect the file type of a file or stdin.

## 📁 ModernFileManager
_... description of the subcategory ..._

* [conan](nan) [❌ ❌ 🖥️CLI] - Find clue about the type of the file.

## 📁 ProgressCopyTool
_... description of the subcategory ..._

* [gcp](nan) [❌ ❌ 🖥️CLI] - (Goffi's cp) - an advanced file copier tool, heavily inspired from the traditional `cp` command, but with some additional features: Displays the copy progress indicator, with estimated time, current file speed; logs of all actions; resume of interrupted copy processes.

## 📁 ShellSyncBackup
_... description of the subcategory ..._

* [PathPicker](https://facebook.github.io/PathPicker/) [❌ ❌ 🖥️TUI] - A tool from Facebook that parses the output from a command and presents a UI to select files and directories, can be used to apply a command of a interactively selected files or to move across directories.

## 📁 TemporaryPasteCLI
_... description of the subcategory ..._

* [pcopy](nan) [❌ 🌐 🖥️CLI] - A temporary file host, nopaste and clipboard across machines. It can be used from the Web UI, via a CLI or without a client by using curl.

## 📁 archive manager
_... description of the subcategory ..._

* [TUI Archiver](https://www.nexus0.net/pub/sw/tuiarchiver/) [❌ ❌ 🖥️CLI 🖥️TUI] - A TUI/CLI application to list / manage archives. Can be used stand-alone and has some features for integrating with TUI file managers

## 📁 cloud storage
_... description of the subcategory ..._

* [gcstree](nan) [❌ 🌐 🖥️CLI] - Tree command for GCS (Google Cloud Storage).

## 📁 compression
_... description of the subcategory ..._

* [ouch](nan) [❌ ❌ 🖥️CLI] - Painless compression and decompression in the terminal.

## 📁 copy progress monitor
_... description of the subcategory ..._

* [progress](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Monitor the progress of common Coreutils command-line tools (`cp`, `mv`, `dd`, `tar`, `rsync`, etc.); it uses a ncurses interface to display the percentage of data copied; it works by reading from system files and retrieving the necessary information for the estimation.

## 📁 directory visualizer
_... description of the subcategory ..._

* [treegen](nan) [❌ ❌ 🖥️CLI] - ASCII tree directory and file structure generator.

## 📁 downloads organizer
_... description of the subcategory ..._

* [dlorg](nan) [❌ ❌ 🖥️TUI] - Powerful and intuitive that automatically organizes your cluttered Downloads folder into a neatly structured directory system.

## 📁 enhanced cat
_... description of the subcategory ..._

* [pycp](nan) [❌ ❌ 🖥️CLI] - cp and mv with a progress bar.
* [xcp](nan) [❌ ❌ 🖥️CLI] - Extended cp.

## 📁 file deployer
_... description of the subcategory ..._

* [dotbins](nan) [❌ ❌ 🖥️CLI] - Keep updated binaries in your dotfiles.

## 📁 file permissions
_... description of the subcategory ..._

* [unix-permissions](nan) [❌ ❌ 🖥️CLI] - Swiss Army knife for Unix permissions.

## 📁 file transfer
_... description of the subcategory ..._

* [qcp](nan) [❌ 🌐 🖥️CLI] - Quick File Copy using QUIC.

## 📁 file utilities
_... description of the subcategory ..._

* [Fast Files](nan) [❌ ❌ 🖥️CLI] - ff is a bash script which is a combination of `mkdir` and `touch`. It can create directory structures and files simultaneously and lists the created objects using `eza`, `lsd`, or `ls`.

## 📁 filesystem sandbox
_... description of the subcategory ..._

* [ForkFS](nan) [❌ ❌ 🖥️CLI] - ForkFS allows you to sandbox a process's changes to your file system.

## 📁 filesystem tools
_... description of the subcategory ..._

* [compsize](nan) [❌ ❌ 🖥️CLI] - Find compression type/ratio on a file or set of files on a btrfs file system.

## 📁 gui-easy-editor
_... description of the subcategory ..._

* [vidir](nan) [❌ ❌ 🖥️CLI] - vidir allows editing of the contents of a directory in a text editor.

## 📁 library browser
_... description of the subcategory ..._

* [lib-x](nan) [❌ ❌ 🖥️TUI] - Browse your calibre library from the terminal.

## 📁 log management
_... description of the subcategory ..._

* [logrotate](nan) [❌ ❌ 🖥️CLI] - Rotate, compress and mail logs.

## 📁 media streamer
_... description of the subcategory ..._

* [zip-stream-cli](nan) [❌ 🌐 🖥️CLI] - A tool that allows to stream and display the contents of various file types from a remote ZIP archive directly in your terminal. With support for images, audio files, text, PDFs, and more,

## 📁 shell
_... description of the subcategory ..._

* [doppelganger](nan) [❌ ❌ 🖥️CLI] - Save and load your shell environment to create doppelganger shells!

## 📁 symlink tools
_... description of the subcategory ..._

* [symlinks](nan) [❌ ❌ 🖥️CLI] - Symlinks is a simple tool that helps find and remedy problematic symbolic links on a system.

## 📁 system monitor
_... description of the subcategory ..._

* [Snoop](nan) [❌ ❌ 🖥️CLI] - A command-line utility for Linux that provides information about files in a directory.

## 📁 vcs client
_... description of the subcategory ..._

* [choof](nan) [❌ ❌ 🖥️CLI] - Choof is a fast and minimal CLI tool for managing files, built with Bubble Tea for Linux.

# file-manager
[Back to TOC](#📚-contents)

Applications for interactively managing files and directories
## 📁 DualPaneFileManager
_... description of the subcategory ..._

* [lfm](https://inigo.katxi.org/devel/lfm/) [❌ ❌ 🖥️TUI] - (Last File Manager) - a file manager written in Python; it comes with lots of features, including 1-pane or 2-pane view, files filters and bookmarks, tree view, virtual file-systems to open compressed archives, search in files, customizable keybindings and themes.

## 📁 LightweightFileManager
_... description of the subcategory ..._

* [ncursesFM](nan) [❌ ❌ 🖥️TUI] - File manager written in C, rather complete in terms of features, especially lightweight and responsive.
* [rnr](nan) [❌ ❌ 🖥️TUI] - The RNR File Manager (RNR's Not Ranger) is a text based file manager that combines the best features of Midnight Commander and Ranger.

## 📁 ModalFileManager
_... description of the subcategory ..._

* [vifm](https://vifm.info/) [❌ ❌ 🖥️TUI] - "ncurses based file manager with vi like keybindings/modes/options/commands/configuration, which also borrows some useful ideas from mutt" (cit.).

## 📁 ModernFileManager
_... description of the subcategory ..._

* [cfiles](nan) [❌ ❌ 🖥️TUI] - ncurses file manager written in C with vim like keybindings
* [felix](nan) [❌ ❌ 🖥️TUI] - TUI file manager with vim-like key mapping
* [fman](nan) [❌ ❌ 🖥️TUI] - TUI File Manager
* [goful](nan) [❌ ❌ 🖥️TUI] - Goful is a CUI file manager written in Go.
* [joshuto](nan) [❌ ❌ 🖥️TUI] - ranger-like terminal file manager
* [lf](nan) [❌ ❌ 🖥️TUI] - lf (as in "list files") is a terminal file manager written in Go with a heavy inspiration from ranger file manager.
* [nnn](nan) [❌ ❌ 🖥️TUI] - "The unorthodox terminal file manager" - a tiny, nearly 0-config and fast file manager supporting all the operations on files and directories.
* [superfile](nan) [❌ ❌ 🖥️TUI] - Pretty fancy and modern file manager.

## 📁 TerminalFileManager
_... description of the subcategory ..._

* [hunter](nan) [❌ 🌐 🖥️TUI] - Ranger-like file browser written in rust.

## 📁 ViKeybindingsFileManager
_... description of the subcategory ..._

* [ranger](https://ranger.github.io/) [❌ ❌ 🖥️TUI] - File manager with vi key bindings, curses interface with a view on the directory hierarchy, comes with a file launcher that automatically determines which program to use for opening a given file type.

## 📁 VisualFileManager
_... description of the subcategory ..._

* [Midnight Commander](http://www.midnight-commander.org/) [❌ ❌ 🖥️TUI] - A visual file manager, full-screen text mode application that allows you to copy, move and delete files and whole directory trees and search for files; includes an internal viewer and editor.

## 📁 file manager
_... description of the subcategory ..._

* [fzfm](nan) [❌ ❌ 🖥️TUI] - A command-line fuzzy finder file manager.
* [Yazi](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Blazing fast terminal file manager written in Rust, based on async I/O.

## 📁 project manager
_... description of the subcategory ..._

* [projectable](nan) [❌ ❌ 🖥️TUI] - A TUI file manager built for projects.

## 📁 shell
_... description of the subcategory ..._

* [clifm](nan) [❌ ❌ 🖥️CLI] - A CLI-based, shell-like, and non-curses terminal file manager written in C: simple, fast, extensible, and lightweight as hell.

## 📁 terminal file manager
_... description of the subcategory ..._

* [TUIFI Manager](nan) [❌ ❌ 🖥️TUI] - A cross-platform terminal-based termux-oriented file manager (and component), meant to be used with a Uni-Curses project or as is.
* [walk](nan) [❌ ❌ 🖥️TUI] - Terminal file manager.

## 📁 terminal file managers
_... description of the subcategory ..._

* [fff](nan) [❌ ❌ 🖥️TUI] - Fast, simple file manager written in bash.

# file-renamer
[Back to TOC](#📚-contents)

Utilities to rename files and directories: address multiple items with one command, interactively edit the name within an editor, etc.
## 📁 BulkRenamer
_... description of the subcategory ..._

* [rename](https://www.kernel.org/pub/linux/utils/util-linux/) [❌ ❌ 🖥️CLI] - Included in `util-linux`, allows bulk rename of files with regex support.

## 📁 BulkRenamerCLI
_... description of the subcategory ..._

* [F2](nan) [❌ ❌ 🖥️CLI] - Cross-platform command-line tool for batch renaming files and directories quickly and safely.
* [Tempren](nan) [❌ ❌ 🖥️CLI] - A powerful file renaming utility that uses flexible template expressions to create new file paths and names.

## 📁 InteractiveRenamer
_... description of the subcategory ..._

* [renameutils](http://www.nongnu.org/renameutils/) [❌ ❌ 🖥️CLI] - A set of programs to change file and directory names by editing them in-place, I find `imv` especially useful to edit a filename at the program prompt.

## 📁 Translation
_... description of the subcategory ..._

* [mmv](nan) [❌ ❌ 🖥️CLI] - Rename multiple files using your $EDITOR. The command name is named after multi-mv.

## 📁 enhanced cat
_... description of the subcategory ..._

* [nomino](nan) [❌ ❌ 🖥️CLI] - Batch rename utility for developers.

## 📁 file manager
_... description of the subcategory ..._

* [Ren](nan) [❌ ❌ 🖥️CLI] - Ren is a command-line utility that takes find-formatted lines via standard input, and batch renames them.

## 📁 file renamer
_... description of the subcategory ..._

* [moove](nan) [❌ ❌ 🖥️CLI] - Manipulate file names and locations using a text editor.

## 📁 file renamers
_... description of the subcategory ..._

* [rename-cli](nan) [❌ ❌ 🖥️TUI] - File renamer with TUI interface and preview.

## 📁 gui-easy-editor
_... description of the subcategory ..._

* [massren](nan) [❌ ❌ 🖥️CLI] - Easily rename multiple files using your text editor.
* [mmv-c](nan) [❌ ❌ 🖥️CLI] - Interactively rename files with your favorite editor.

## 📁 image renamer
_... description of the subcategory ..._

* [VisioNomicon](nan) [🤖 ❌ 🖥️CLI] - A utility that leverages GPT-4V to rename image files based on their content.

## 📁 music file tools
_... description of the subcategory ..._

* [Musort](nan) [❌ ❌ 🖥️CLI] - Rename multiple audio/music files based on the ID3 tag at once.

## 📁 search tools
_... description of the subcategory ..._

* [Bren](https://www.byteptr.com/bren/) [❌ ❌ 🖥️CLI] - Bren is a command line tool for GNU/Linux (and many others). It has support for GNU Guile scripting. Bren is simple, fast, and it's written in C.

# file-system
[Back to TOC](#📚-contents)

File systems with specific features; e.g., the possibility to add tags and labels to files
## 📁 FileTaggerCLI
_... description of the subcategory ..._

* [wutag](nan) [❌ ❌ 🖥️CLI] - CLI Tool for tagging and organizing files by tags.

## 📁 RemoteFilesystemMounting
_... description of the subcategory ..._

* [sshfs](nan) [❌ ❌ 🖥️CLI] - Locally mount a remote file-system through SSH and access files and directory as they would be on the local machine.

## 📁 TagBasedVirtualFS
_... description of the subcategory ..._

* [TMSU](http://tmsu.org/) [❌ ❌ 🖥️CLI] - A simple tool for tagging files, providing a virtual filesystem for a tag-based view of your files from within any other program.

## 📁 deployment tools
_... description of the subcategory ..._

* [ipfs-deploy](nan) [❌ 🌐 🖥️CLI] - Zero-Config CLI to Deploy Static Websites to IPFS [IPFS](https://en.wikipedia.org/wiki/InterPlanetary_File_System).

# file-watch
[Back to TOC](#📚-contents)

Services that watch files for changes and perform actions when something happens
## 📁 DirectoryWatcher
_... description of the subcategory ..._

* [watcher](nan) [❌ ❌ 🖥️CLI] - Watches all the files present in a directory and whenever a file is changed or a file is created/deleted from the directory, it runs a specified command.

## 📁 FileWatcherCLI
_... description of the subcategory ..._

* [watchexec](nan) [❌ ❌ 🖥️CLI] - Executes commands in response to file modifications.

## 📁 ProcessMonitorTUI
_... description of the subcategory ..._

* [Viddy](nan) [❌ ❌ 🖥️TUI] - Modern watch command. Time machine and pager etc.

## 📁 ShellSyncBackup
_... description of the subcategory ..._

* [wfh](nan) [❌ 🌐 🖥️CLI] - Continuously watches your local directories and rsync them against a remote host.

## 📁 file monitor
_... description of the subcategory ..._

* [rwatch](nan) [❌ ❌ 🖥️TUI] - A Rust re-implementation of the classic Unix watch command that allows you to run a command repeatedly and watch its output.

## 📁 file watcher
_... description of the subcategory ..._

* [reflex](nan) [❌ ❌ 🖥️CLI] - Reflex is a small tool to watch a directory and rerun a command when certain files change.

## 📁 file watchers
_... description of the subcategory ..._

* [Chokidar CLI](nan) [❌ ❌ 🖥️CLI] - Fast cross-platform command line utility to watch file system changes.

# financial
[Back to TOC](#📚-contents)

Personal ledger trackers, currency converters, and tools to manage and track cryptocurrencies
## 📁 Accounting
_... description of the subcategory ..._

* [abandon](nan) [❌ ❌ 🖥️CLI] - A text based, double-entry accounting system inspired by Ledger with infinite precision arithmetic. Made in Java. Includes a GUI.
* [ledger](http://ledger-cli.org/) [❌ ❌ 🖥️CLI] - A powerful, double-entry accounting system; it uses a simple yet powerful text syntax to specify the items to account.

## 📁 AccountingCLI
_... description of the subcategory ..._

* [hledger](https://hledger.org/) [❌ ❌ 🖥️CLI] - A is fast, reliable, free, multicurrency double-entry accounting software to track money, investments, cryptocurrencies, time, or any other quantifiable commodity; uses a future-proof plain text file format.

## 📁 CloudSyncManager
_... description of the subcategory ..._

* [Cloudcash](nan) [❌ 🌐 🖥️CLI] - Check your cloud spending from the CLI, from Waybar, and from the macOS menu bar!

## 📁 CryptoTUI
_... description of the subcategory ..._

* [cointop](nan) [❌ 🌐 🖥️TUI] - A fast and lightweight interactive terminal based UI application for tracking cryptocurrencies.

## 📁 FinanceCLI
_... description of the subcategory ..._

* [Lakshmi](nan) [❌ ❌ 🖥️CLI] - Investing library and command-line interface inspired by the Bogleheads philosophy.
* [Quoter](nan) [❌ 🌐 🖥️CLI] - The console based stock quote tool.

## 📁 TerminalFinanceTracker
_... description of the subcategory ..._

* [Ticker](nan) [❌ 🌐 🖥️TUI] - Terminal stock watcher and stock position tracker.

## 📁 accounting
_... description of the subcategory ..._

* [beancount](https://beancount.github.io/) [❌ 🌐 🖥️CLI] - Double-entry bookkeeping computer language that lets you define financial transaction records in a text file, read them in memory, generate a variety of reports from them, and provides a web interface.

## 📁 bitcoin cli
_... description of the subcategory ..._

* [bits](nan) [❌ ❌ 🖥️CLI] - CLI tool and pure Python library for Bitcoin.

## 📁 budget tracking
_... description of the subcategory ..._

* [budget-cli](https://www.joshcanhelp.com/budget-cli/) [❌ ❌ 🖥️CLI] - Import, de-dupe, categorize, and report on financial transactions.

## 📁 currency converters
_... description of the subcategory ..._

* [cash-cli](nan) [❌ 🌐 🖥️CLI] - Convert Currency Rates.
* [moeda](nan) [❌ 🌐 🖥️CLI] - A foreign exchange rates and currency conversion using the command line.

## 📁 enhanced cat
_... description of the subcategory ..._

* [mop](nan) [❌ ❌ 🖥️TUI] - Stock market tracker for hackers.

## 📁 exchange rates
_... description of the subcategory ..._

* [ecb-rates](nan) [❌ 🌐 🖥️CLI] - Fetch exchage rates from the European Central Bank.

## 📁 invoice generator
_... description of the subcategory ..._

* [Invoice](nan) [❌ ❌ 🖥️CLI] - Generate invoices from the command line.

## 📁 log viewer
_... description of the subcategory ..._

* [paycon](nan) [❌ ❌ 🖥️CLI] - Converts pay amounts between different time units.

# find
[Back to TOC](#📚-contents)

Search the filesystem looking for files with specific characteristics, e.g., names; alternatives to `find`
## 📁 FastFileLocator
_... description of the subcategory ..._

* [plocate](https://plocate.sesse.net/) [❌ ❌ 🖥️CLI] - A much faster locate; plocate is a locate based on posting lists, completely replacing mlocate with a much faster (and smaller) index.

## 📁 FastFindAlternative
_... description of the subcategory ..._

* [fd](nan) [❌ ❌ 🖥️CLI] - A simple, fast, and user-friendly alternative to find. Written in Rust.

## 📁 enhanced cat
_... description of the subcategory ..._

* [friendly-find](nan) [❌ ❌ 🖥️CLI] - Usable replacement for find.

## 📁 file finder
_... description of the subcategory ..._

* [rawhide](nan) [❌ ❌ 🖥️CLI] - File finder that uses C expressions to specify the filenames.

## 📁 file search
_... description of the subcategory ..._

* [bfs](nan) [❌ ❌ 🖥️CLI] - A breadth-first version of the UNIX find command.

## 📁 fuzzy finders
_... description of the subcategory ..._

* [happyfinder](nan) [❌ ❌ 🖥️CLI] - (another) Fuzzy file finder for the command line.

## 📁 fuzzy‑search
_... description of the subcategory ..._

* [Findpick](nan) [❌ ❌ 🖥️TUI] - General purpose file picker combining "find" command with a fuzzy finder.

## 📁 grep alternative
_... description of the subcategory ..._

* [gret](nan) [❌ ❌ 🖥️CLI] - A command-line utility designed to search through directories and files for a regex expression that matches.

# flashcard
[Back to TOC](#📚-contents)

Manage decks of flashcards and Anki decks
## 📁 FlashcardTrainerTUI
_... description of the subcategory ..._

* [flash-tui](nan) [❌ ❌ 🖥️TUI] - Flashcard app for the terminal.
* [speki](nan) [❌ ❌ 🖥️CLI] - Manage flashcards in the terminal similar to anki.

## 📁 anki tool
_... description of the subcategory ..._

* [ToRRential Card processor](nan) [❌ ❌ 🖥️CLI] - A command-line program to add a card to Anki using AnkiConnect API.

## 📁 cli learning tools
_... description of the subcategory ..._

* [hardv](nan) [❌ ❌ 🖥️CLI] - A CLI flashcard app for UNIX-compatible systems, conforming to the UNIX philosophy.

## 📁 flashcard tool
_... description of the subcategory ..._

* [GoCard](nan) [❌ ❌ 🖥️CLI] - A lightweight file-based spaced repetition system (SRS) that uses plain Markdown files for flashcards. Perfect for developers who prefer text files, Git version control, and keyboard-driven interfaces.

## 📁 flashcard tools
_... description of the subcategory ..._

* [mdfc](nan) [❌ ❌ 🖥️TUI] - Easily create and study flashcards using a Markdown file with spaced repetition.

## 📁 flashcards
_... description of the subcategory ..._

* [py_flashcards](nan) [❌ ❌ 🖥️TUI] - Text-only CLI flashcards parsed from Markdown file.
* [revise-tui](nan) [❌ ❌ 🖥️TUI] - A TUI Anki client. Revise is a command-line program used to schedule the review of items using spaced repetition.

## 📁 nextcloud tool
_... description of the subcategory ..._

* [tui-deck](nan) [❌ 🌐 🖥️TUI] - A TUI frontend for Nextcloud Deck app.

## 📁 vocabulary trainer
_... description of the subcategory ..._

* [vocage](nan) [❌ ❌ 🖥️CLI] - Vocage is a minimalistic terminal-based vocabulary-learning tool. It presents flashcards using a spaced-repetition algorithm (e.g. Leitner). Data is stored in a simple plain-text tab-separated values format (TSV).

# font
[Back to TOC](#📚-contents)

Utilities to manage system fonts and to generate text using ASCII-art-like characters
## 📁 ascii art
_... description of the subcategory ..._

* [cfonts](nan) [❌ ❌ 🖥️CLI] - А command line tool for generating ANSI fonts in the console.

## 📁 ascii-text-rendering
_... description of the subcategory ..._

* [FIGlet](http://www.figlet.org/) [❌ ❌ 🖥️CLI] - Not exactly a font manager, but a nice program for making large letters out of ordinary text; an astonishing number of different fonts is available.

## 📁 font manager
_... description of the subcategory ..._

* [fnt](nan) [❌ 🌐 🖥️CLI] - apt for fonts, the missing font manager for macOS/Linux.

## 📁 visual-effects-rendering
_... description of the subcategory ..._

* [toilet](http://caca.zoy.org/wiki/toilet) [❌ ❌ 🖥️CLI] - Tries to improve `FIGlet`; can load FIGlet fonts; supports Unicode input and output, color fonts and output, and various output formats, including HTML, IRC and ANSI; uses `libcaca` to produce nice textual effects.

# funny
[Back to TOC](#📚-contents)

Miscellaneous of tools that provide some funny/aesthetical functionality (animations, funny quotes, original message visualization, etc.)
## 📁 AsciiSpeechGenerato
_... description of the subcategory ..._

* [cowsay](https://en.wikipedia.org/wiki/Cowsay) [❌ ❌ 🖥️CLI] - Generate an ASCII art of a cow with a bubble containing the specified message (I provide the Wikipedia link since at the moment the link to the author's homepage results to be unreachable).

## 📁 AsciiSpeechGenerator
_... description of the subcategory ..._

* [cowthink](https://en.wikipedia.org/wiki/Cowsay) [❌ ❌ 🖥️CLI] - Same as `cowsay`, but uses a "think" bubble instead of a speech bubble.

## 📁 EmojiPickerCLI
_... description of the subcategory ..._

* [Limoji](nan) [❌ ❌ 🖥️CLI] - Limoji is an open source tool that makes it easy to choose between hundreds of cool ASCII emoticons and share them with your friends.

## 📁 FunCLI
_... description of the subcategory ..._

* [ponysay](nan) [❌ ❌ 🖥️CLI] - Pony rewrite of cowsay.

## 📁 MatrixVideoConfCLI
_... description of the subcategory ..._

* [matrix-webcam](nan) [❌ 🌐 🖥️CLI] - Take your video conference from within the matrix.

## 📁 PokemonFetcherCLI
_... description of the subcategory ..._

* [pokeget](nan) [❌ 🌐 🖥️CLI] - A bash script you can use to display cool sprites of Pokemon in your terminal.

## 📁 QuoteGeneratorCLI
_... description of the subcategory ..._

* [fortune](http://software.clapper.org/fortune/) [❌ ❌ 🖥️CLI] - Generates random messages fetched from a quotation database.

## 📁 cli fun
_... description of the subcategory ..._

* [pyjokes](nan) [❌ ❌ 🖥️CLI] - One line jokes for programmers (jokes as a service).
* [Russhian Roulette](nan) [❌ ❌ 🖥️CLI] - 1/6 chance of posting your SSH private key on pastebin (do you really want to try?).

## 📁 enhanced cat
_... description of the subcategory ..._

* [yosay](nan) [❌ ❌ 🖥️CLI] - Like cowsay, but for yeoman.

## 📁 fun
_... description of the subcategory ..._

* [bollywood](nan) [❌ ❌ 🖥️TUI] - Runs terminal screencasts in multiple panes, resulting in another real-time Hollywood-style real-time hacking terminal.
* [hollywood](nan) [❌ ❌ 🖥️TUI] - Runs a script turning your Linux terminal into a Hollywood style real-time hacking terminal.

## 📁 fun / novelty
_... description of the subcategory ..._

* [daktilo](nan) [❌ ❌ 🖥️CLI] - Turn your keyboard into a typewriter adding sounds at each keystroke.

## 📁 funny aliases
_... description of the subcategory ..._

* [HARRY_POTTER_ALIASES](nan) [❌ ❌ 🖥️TUI] - Harry Potter-themed aliases a magical journey through the wizarding world of terminal commands.

## 📁 funny tools
_... description of the subcategory ..._

* [kyun](nan) [❌ ❌ 🖥️CLI] - Kyun is a low productivity, low fidelity, low customizablity text editor that has its focus firm on user discomfort.

## 📁 terminal animation
_... description of the subcategory ..._

* [clouddrift](nan) [❌ 🌐 🖥️TUI] - Soft clouds drifting across your terminal.

## 📁 terminal drawing tool
_... description of the subcategory ..._

* [Draw](nan) [❌ ❌ 🖥️TUI] - draw is an simple drawing tool in the terminal. Hold your mouse down and move it across the screen to draw anything you want!

## 📁 text decoration
_... description of the subcategory ..._

* [boxes](nan) [❌ ❌ 🖥️CLI] - Boxes is a command line filter program which draws ASCII art boxes around your input text.

# games
[Back to TOC](#📚-contents)

Board games, puzzles, roguelikes, role-play, adventures, card games, etc.
## 📁 APIClientCLI
_... description of the subcategory ..._

* [Flapioca](nan) [❌ ❌ 🖥️CLI] - A Flappy Bird-inspired terminal game written in Go.

## 📁 AdvancedCalculators
_... description of the subcategory ..._

* [Slash'EM](http://slashem.sourceforge.net/) [❌ ❌ 🖥️TUI] - Rogue-like game derived from `nethack` offering extra features, monsters, and items; includes a GUI version.

## 📁 GameCLI
_... description of the subcategory ..._

* [hangman](nan) [❌ ❌ 🖥️CLI] - A Go TUI Hangman game built with the lovely BubbleTea framework.
* [Minesweeper Game](nan) [❌ ❌ 🖥️CLI] - A small command line Minesweeper Game.
* [othello-cli](nan) [❌ ❌ 🖥️CLI] - othello-cli is a CLI version of Othello (Reversi) written in Rust. You can play against another player, the AI, or watch two AIs play each other.
* [sssnake](nan) [❌ ❌ 🖥️CLI] - (Smart and sexy snake) The classic snake game for the terminal that can plays itself and be use like a screensaver.

## 📁 GameTUI
_... description of the subcategory ..._

* [Pokete](nan) [❌ ❌ 🖥️TUI] - A terminal based Pokemon like game.

## 📁 TUI RogueGame
_... description of the subcategory ..._

* [Angband](https://rephial.org/) [❌ ❌ 🖥️TUI] - Angband is a free, single-player dungeon exploration game.

## 📁 TerminalBoardGames
_... description of the subcategory ..._

* [terminal_board_games](nan) [❌ ❌ 🖥️TUI] - Board games for the terminal.

## 📁 TerminalChessAI
_... description of the subcategory ..._

* [chs](nan) [🤖 ❌ 🖥️TUI] - Play chess against the Stockfish engine in your terminal.

## 📁 TerminalGame
_... description of the subcategory ..._

* [crappybird-py](nan) [❌ ❌ 🖥️TUI] - Flappy bird.
* [Language-games](nan) [❌ ❌ 🖥️TUI] - Dead simple games made with word vectors.
* [minesweeper](nan) [❌ ❌ 🖥️TUI] - Cross-platform terminal based minesweeper.
* [Terminal Phase](https://dustycloud.org/blog/terminal-phase-1.0/) [❌ ❌ 🖥️TUI] - A space shooter game you can play in your terminal.
* [usolitaire](nan) [❌ ❌ 🖥️TUI] - Solitaire in your terminal.

## 📁 TerminalGame(Minesweeper)
_... description of the subcategory ..._

* [freesweep](http://www.upl.cs.wisc.edu/~hartmann/sweep/) [❌ ❌ 🖥️TUI] - A Minesweeper clone for the terminal which allows you to configure settings such as table rows and columns up to 1024x1024!), percentage of bombs, colors, and also has a high scores table.

## 📁 TerminalGame(PuzzlePlatformer)
_... description of the subcategory ..._

* [Oldrunner](http://culot.org/public/Code/oldrunner.html) [❌ ❌ 🖥️TUI] - Character-based remake of Lode Runner, includes all the original 150 levels.

## 📁 TerminalGame(Roguelike)
_... description of the subcategory ..._

* [Nethack](http://nethack.org/) [❌ ❌ 🖥️TUI] - Single player rogue-like dungeon exploration game.

## 📁 TerminalGame(SimulationStrategy)
_... description of the subcategory ..._

* [Dwarf fortress](http://www.bay12games.com/dwarves/) [❌ ❌ 🖥️TUI] - A fantasy game using ASCII art graphical representation of the game environment, it features a rich environment with many options and possibilities.

## 📁 TerminalGame(SurvivalRPG)
_... description of the subcategory ..._

* [Cataclysm: Dark Days Ahead](https://cataclysmdda.org/) [❌ ❌ 🖥️TUI] - Open source turn-based survival RPG development project.

## 📁 TerminalGame(Tetris)
_... description of the subcategory ..._

* [bastet](http://fph.altervista.org/prog/bastet.html) [❌ ❌ 🖥️TUI] - (Bastard Tetris) implements the classical Tetris but with a logic to generate the next block which maximizes the difficulty for the player.

## 📁 TerminalGameCLI
_... description of the subcategory ..._

* [mazter](nan) [❌ ❌ 🖥️CLI] - A maze in your terminal.

## 📁 TerminalGameTUI
_... description of the subcategory ..._

* [anonymine](https://oskog97.com/projects/anonymine/) [❌ ❌ 🖥️TUI] - Curses mode minesweeper without guessing and other original features.
* [greed](http://www.catb.org/~esr/greed/) [❌ ❌ 🖥️TUI] - A game in which the goal is to move and consume all the numbers in a table.

## 📁 WordleGameTUI
_... description of the subcategory ..._

* [terdle](nan) [❌ ❌ 🖥️TUI] - Wordle implemented in Rust.

## 📁 ascii fps game
_... description of the subcategory ..._

* [terminal-doom](nan) [❌ ❌ 🖥️TUI] - Play DOOM in modern terminals.

## 📁 chess
_... description of the subcategory ..._

* [chess-tui](nan) [❌ ❌ 🖥️TUI] - Play chess from your terminal.

## 📁 cli game
_... description of the subcategory ..._

* [escaping-figures-game-cli](nan) [❌ ❌ 🖥️TUI] - Count figure's occurrences in the escaping figures matrix.
* [guess-word-cli](nan) [❌ ❌ 🖥️CLI] - Find out a source word which characters was shuffled and moreover an extra character was added to bring some complexity.
* [rebels-in-the-sky](nan) [❌ 🌐 🖥️CLI] - P2P terminal game about spacepirates playing basketball across the galaxy.

## 📁 enhanced cat
_... description of the subcategory ..._

* [clidle](nan) [❌ ❌ 🖥️CLI] - Wordle, now over SSH.
* [rpg-cli](nan) [❌ ❌ 🖥️CLI] - Your filesystem as a dungeon!

## 📁 game
_... description of the subcategory ..._

* [2048-cli](nan) [❌ ❌ 🖥️TUI] - A 2048 clone that run in the terminal.
* [Cemetery Escape](nan) [❌ ❌ 🖥️TUI] - A game in which you must escape the cemetery. Search tombstones to find the key. Then head for the door, but watch out for ghosts.
* [gg](nan) [❌ ❌ 🖥️TUI] - A collection of games you can play in your terminal; written in Go.
* [tui-sudoku](nan) [❌ ❌ 🖥️TUI] - tui-sudoku is a configurable terminal interface sudoku game, with quite a few features.

## 📁 game editor
_... description of the subcategory ..._

* [shellphone](nan) [❌ ❌ 🖥️TUI] - Terminal based Terraria player file editor.

## 📁 interactive fiction
_... description of the subcategory ..._

* [Frotz](https://davidgriffith.gitlab.io/frotz/) [❌ ❌ 🖥️CLI] - Frotz is an interpreter for Infocom games and other Z-machine games.

## 📁 irc bot game
_... description of the subcategory ..._

* [blackjack](nan) [❌ ❌ 🖥️CLI] - IRC bot to play blackjack.

## 📁 minesweeper
_... description of the subcategory ..._

* [go-sweep](nan) [❌ ❌ 🖥️TUI] - Minesweeper game in the command line programmed in Go.

## 📁 puzzle game
_... description of the subcategory ..._

* [tuifoop](nan) [❌ ❌ 🖥️TUI] - Terminal puzzle game with the goal of removing as many cells as possible (or even all cells) from a grid. A terminal clone of Swell Foop.

## 📁 shell
_... description of the subcategory ..._

* [GameShell](nan) [❌ ❌ 🖥️TUI] - GameShell was devised as a tool to help university students to engage with a real shell, in a way that encourages learning while also having fun.

## 📁 terminal chess
_... description of the subcategory ..._

* [cli-chess](nan) [❌ 🌐 🖥️TUI] - A highly customizable way to play chess in your terminal. Play online (via Lichess.org) and offline against the Fairy-Stockfish engine. All Lichess variants are supported.

## 📁 terminal game
_... description of the subcategory ..._

* [asterion](nan) [❌ ❌ 🖥️TUI] - Find your way through an inifinite maze in this multiplayer ssh game. Beware of the minotaurs!
* [Dino](nan) [❌ ❌ 🖥️TUI] - A C++ and ncurses rendering of the popular chrome dinosaur game on the terminal.
* [gambit](nan) [❌ ❌ 🖥️TUI] - Chess board in your terminal.
* [Maze of Me](nan) [🤖 ❌ 🖥️CLI] - A deeply personal psychological game powered by AI and real user data.
* [nc2048](nan) [❌ ❌ 🖥️TUI] - A ncurses 2048 game that can be played in the terminal.
* [rooshk](nan) [❌ ❌ 🖥️TUI] - A command line game in which you act as god over a sandbox world.
* [sku](nan) [❌ ❌ 🖥️TUI] - Simple TUI written in go to play sudoku in the terminal.
* [sshattrick](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Play Hattrick in your terminal over SSH.
* [T-RexC](nan) [❌ ❌ 🖥️TUI] - Simple Console Google T-Rex Game.
* [term-asteroids](nan) [❌ ❌ 🖥️TUI] - An Asteroids-like game, running in a terminal, written in PHP.
* [terminordle](nan) [❌ 🌐 🖥️TUI] - Inspired by the popular online game wordle made, you can play a pretty close replica of the original locally or multiplayer over the network.
* [wordle-curses](nan) [❌ ❌ 🖥️CLI] - A simple TUI wordle game with curses.

## 📁 terminal games
_... description of the subcategory ..._

* [Durak](nan) [❌ ❌ 🖥️TUI] - Durak card game for two in a terminal.
* [Solitaire TUI](nan) [❌ ❌ 🖥️TUI] - Klondike solitaire for the terminal.
* [Terminal Roulette](nan) [❌ ❌ 🖥️TUI] - Your own roulette table in the terminal.

## 📁 tetris game
_... description of the subcategory ..._

* [tetrs](nan) [❌ ❌ 🖥️TUI] - Tetromino game engine and terminal application to play Tetris, written in Rust.

## 📁 tui chess client
_... description of the subcategory ..._

* [cheezee](nan) [❌ ❌ 🖥️TUI] - Chess TUI client built for Linux.

## 📁 word games
_... description of the subcategory ..._

* [Words](nan) [❌ ❌ 🖥️CLI] - A set of word-based puzzle games for the CLI while you wait for the build to run.

## 📁 wordle solver
_... description of the subcategory ..._

* [Wordle Solver](nan) [❌ ❌ 🖥️CLI] - A bash script that can solve wordle riddles.

# git
[Back to TOC](#📚-contents)

Tools to support and extend the functionalities of the `git` version tracker
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [Git Commit Vanity Hash Solver](nan) [❌ ❌ 🖥️CLI] - Neat tool to find a 'vanity' hash for a given git commit. Make all your commits hashes start with the prefix c0ffee, cafe, badc0de5 or whatever makes you happy!

## 📁 CloudSyncManager
_... description of the subcategory ..._

* [gh](https://cli.github.com/) [❌ ❌ 🖥️CLI] - GitHub's official tool to manage repos, issues, projects, gists and much more.

## 📁 CommitHelperCLI
_... description of the subcategory ..._

* [git-cz](nan) [❌ ❌ 🖥️CLI] - Semantic Git commits.

## 📁 CommitMessageHelperCLI
_... description of the subcategory ..._

* [rcz](nan) [❌ ❌ 🖥️CLI] - A tool to write a commit message based on “Conventional Commits”.

## 📁 DistributedVersionControl
_... description of the subcategory ..._

* [git](https://git-scm.com/) [❌ ❌ 🖥️CLI] - The winner across all the existing file versioning tools, distributed versioning, fully controllable from the command-line, plenty of configuration and usage options, behind a number of related project that leverage git as backend.

## 📁 GitEnhancerCLI
_... description of the subcategory ..._

* [gitsummary](nan) [❌ ❌ 🖥️CLI] - A better git status that lists stashes, file statuses, branch list, all nicely formatted with color.

## 📁 GitFzfCLI
_... description of the subcategory ..._

* [gh-f](nan) [❌ 🌐 🖥️CLI] - The ultimate, compact and snappy fzf extension for gh CLI.

## 📁 GitInterface(TUI)
_... description of the subcategory ..._

* [grv](nan) [❌ ❌ 🖥️TUI] - Git Repository Viewer - A terminal based interface for viewing Git repositories. It allows refs, commits, and diffs to be viewed, searched and filtered.
* [tig](nan) [❌ ❌ 🖥️TUI] - An ncurses-based text-mode interface for `git` that can act as a repository browser, but can also assist in staging changes for commit at chunk level.

## 📁 GitRemoteHelperCLI
_... description of the subcategory ..._

* [git-remote-aws](nan) [❌ 🌐 🖥️CLI] - Management of encrypted git hosting.

## 📁 GitRepoManagerCLI
_... description of the subcategory ..._

* [gita](nan) [❌ ❌ 🖥️CLI] - A command-line tool to manage multiple git repositories.

## 📁 GitSearchCLI
_... description of the subcategory ..._

* [gh-s](nan) [❌ 🌐 🖥️CLI] - Search GitHub repositories interactively.

## 📁 GitSecretManagerCLI
_... description of the subcategory ..._

* [git-secret](nan) [❌ ❌ 🖥️CLI] - A bash tool which stores private data inside a git repo; it uses users' public keys, allowing trusted users to access encrypted data using PGP and their secret keys.

## 📁 GitServerTUI
_... description of the subcategory ..._

* [Soft Serve](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - Self-hostable Git server for the command line. One distinguished feature is the possibility to create new repositories with a push.

## 📁 GitStatistics
_... description of the subcategory ..._

* [fzf-git.sh](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - bash and zsh key bindings for Git objects, powered by fzf.
* [git-all-branches](nan) [❌ ❌ 🖥️CLI] - Improved visualization of git branches (`git branch -a`).
* [git-bug](nan) [❌ ❌ 🖥️CLI] - Distributed, offline-first bug tracker embedded in git, with bridges.
* [git-extras](nan) [❌ ❌ 🖥️CLI] - Little git extras like git-ignore, git-setup, git-changelog, git-release, git-effort and more.
* [git-heatgrid](nan) [❌ ❌ 🖥️CLI] - Visualize git commits as a calendar heatmap.
* [git-peek](nan) [❌ 🌐 🖥️CLI] - git peek is the fastest way to open a remote git repository in your local text editor.
* [git-quick-stats](nan) [❌ ❌ 🖥️CLI] - A simple and efficient way to access various statistics in a git repository.
* [git-stats](nan) [❌ ❌ 🖥️CLI] - Local git statistics including GitHub-like contributions calendars.
* [GitUI](nan) [❌ ❌ 🖥️TUI] - The comfort of a git GUI but right in your terminal, with keyboard only control, scalable UI, and features all the necessary operations of git.

## 📁 GitStatisticsCLI
_... description of the subcategory ..._

* [stargazer](nan) [❌ 🌐 🖥️CLI] - GitHub stats from the command line.

## 📁 GitTUIWrapper
_... description of the subcategory ..._

* [forgit](nan) [❌ ❌ 🖥️TUI] - A utility tool powered by fzf for using git interactively.

## 📁 GitVisualizerCLI
_... description of the subcategory ..._

* [onefetch](nan) [❌ ❌ 🖥️CLI] - Git repository summary on your terminal.

## 📁 GitforLargeFiles
_... description of the subcategory ..._

* [git-annex](https://git-annex.branchable.com/) [❌ ❌ 🖥️CLI] - Manages files with `git`, without checking the file contents into git; very useful to manage large/binary files.

## 📁 SelfHostedGitServer
_... description of the subcategory ..._

* [Gitea](https://gitea.com/) [❌ 🌐 🖥️CLI] - Single binary self-hosted Git service.

## 📁 cd helper
_... description of the subcategory ..._

* [travelgrunt](nan) [❌ ❌ 🖥️CLI] - cd inside [mono]repos without fatigue.

## 📁 changelog tools
_... description of the subcategory ..._

* [git-cliff](nan) [❌ ❌ 🖥️CLI] - A highly customizable Changelog Generator that follows Conventional Commit specifications.

## 📁 dotfiles manager
_... description of the subcategory ..._

* [patchy](nan) [❌ 🌐 🖥️CLI] - A tool which makes it easy to declaratively manage personal forks by automatically merging pull requests.

## 📁 enhanced cat
_... description of the subcategory ..._

* [czg](nan) [❌ ❌ 🖥️CLI] - Interactively generate standardized commit messages.
* [gh-stars](nan) [❌ 🌐 🖥️CLI] - A GitHub CLI extension to show repository stargazers.
* [sad](nan) [❌ ❌ 🖥️CLI] - CLI search and replace. Show you a nice diff of proposed changes before you commit them.

## 📁 git TUI tools
_... description of the subcategory ..._

* [git commander](nan) [❌ ❌ 🖥️TUI] - A git tool with an easy interactive terminal interface.

## 📁 git analytics
_... description of the subcategory ..._

* [mergestat-lite](nan) [❌ ❌ 🖥️CLI] - A command-line tool for running SQL queries on git repositories and related data sources.

## 📁 git assistant
_... description of the subcategory ..._

* [giq](nan) [🤖 ❌ 🖥️CLI] - Git CLI with AI-powered commit messages and insights; it is a drop-in replacement for git with the same commands.

## 📁 git automation
_... description of the subcategory ..._

* [gacp](nan) [❌ ❌ 🖥️CLI] - git add, commit and push in one go.

## 📁 git autosync
_... description of the subcategory ..._

* [Git Auto Sync](nan) [❌ ❌ 🖥️CLI] - Automatically commits changes to a git repository, and always keep that repository up to date.

## 📁 git clients
_... description of the subcategory ..._

* [gitlab-cli](nan) [❌ 🌐 🖥️CLI] - Create GitLab merge requests.

## 📁 git commit tools
_... description of the subcategory ..._

* [semantic-git-commit-cli](nan) [❌ ❌ 🖥️CLI] - Ensure semantic commits messages. With emoji support.

## 📁 git diff viewer
_... description of the subcategory ..._

* [dunk](nan) [❌ ❌ 🖥️CLI] - Prettier git diffs in the terminal.
* [mamediff](nan) [❌ ❌ 🖥️TUI] - A TUI editor for managing unstaged and staged Git diffs.

## 📁 git export
_... description of the subcategory ..._

* [Export Pull Requests](nan) [❌ ❌ 🖥️CLI] - Export pull requests and/or issues to a CSV file. Supports GitHub, GitLab, and Bitbucket.

## 📁 git helper
_... description of the subcategory ..._

* [git-recall](nan) [❌ ❌ 🖥️CLI] - A simple tool that allows you to easily go through your commits and check what you or other contributors in your team did.
* [mkgit](nan) [❌ ❌ 🖥️CLI] - This Bash script automates the process of creating a new GitHub repository, initializing it with a README file, and pushing the initial commit to the remote repository. The script prompts the user for a repository name and utilizes the GitHub API to create a new public repository.

## 📁 git helpers
_... description of the subcategory ..._

* [git-cc](nan) [❌ ❌ 🖥️CLI] - A git extension to help write conventional commits.
* [gitnr](nan) [❌ ❌ 🖥️CLI] - Create `.gitignore` files using one or more templates from TopTal, GitHub or your own collection.

## 📁 git hook
_... description of the subcategory ..._

* [unreal-git-hook](nan) [❌ ❌ 🖥️CLI] - Mix of git-hook and Unreal Tournament announcer.

## 📁 git profile
_... description of the subcategory ..._

* [git-identity](nan) [❌ ❌ 🖥️CLI] - Automated git alias management.

## 📁 git tool
_... description of the subcategory ..._

* [automate-git-commands](nan) [❌ ❌ 🖥️CLI] - Automates many of the common uses of git, ssh key generation, and ssh configuration.
* [ur-commit-mentor](nan) [🤖 ❌ 🖥️CLI] - A CLI tool that analyzes git commits and provides AI-powered code review insights (for now only works with Claude API).

## 📁 git tools
_... description of the subcategory ..._

* [git absorb](nan) [❌ ❌ 🖥️CLI] - git commit --fixup, but automatic.
* [git-booster-cli](nan) [❌ ❌ 🖥️CLI] - Improve your git workflow with customizable and runnable blocks.
* [git-fuzzy](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Interactive `git` with the help of `fzf`.

## 📁 git tui
_... description of the subcategory ..._

* [Lazygit](nan) [❌ ❌ 🖥️TUI] - A simple terminal UI for git commands that simplify the execution of many operations making them interactive.

## 📁 github dashboard
_... description of the subcategory ..._

* [gh-dash](nan) [❌ 🌐 🖥️TUI] - A beautiful CLI dashboard for GitHub.

## 📁 github graph
_... description of the subcategory ..._

* [Kusa](nan) [❌ ❌ 🖥️CLI] - Displays GitHub contribution graphs.

## 📁 github prs tracker
_... description of the subcategory ..._

* [prs](nan) [❌ 🌐 🖥️TUI] - Stay updated on PRs without leaving the terminal.

## 📁 repo cleaner
_... description of the subcategory ..._

* [BFG Repo-Cleaner](nan) [❌ ❌ 🖥️CLI] - Removes large or troublesome blobs like git-filter-branch does, but faster.

## 📁 secret scanner
_... description of the subcategory ..._

* [gitleaks](nan) [❌ ❌ 🖥️CLI] - Tool for detecting and preventing hardcoded secrets like passwords, api keys, and tokens in git repos.

## 📁 sourcehut git client
_... description of the subcategory ..._

* [hut](nan) [❌ 🌐 🖥️CLI] - A CLI tool for sr.ht.

# graphics
[Back to TOC](#📚-contents)

Applications to process images, colors, and ASCII art
## 📁 BackupAutomationWrapper
_... description of the subcategory ..._

* [svgcleaner](nan) [❌ ❌ 🖥️CLI] - Clean up your SVG files from the unnecessary data.

## 📁 ColorToolCLI
_... description of the subcategory ..._

* [pastel](nan) [❌ ❌ 🖥️CLI] - A command-line tool to generate, analyze, convert and manipulate colors.

## 📁 FractalCLI
_... description of the subcategory ..._

* [mandelbrot-cli](nan) [❌ ❌ 🖥️CLI] - Multiplatform terminal mandelbrot set explorer.

## 📁 ImageEditingConversion
_... description of the subcategory ..._

* [ImageMagick](http://www.imagemagick.org/script/index.php) [❌ ❌ 🖥️CLI] - Software suite to create, edit, compose, or convert bitmap images; it handles many file formats (including PDF and SVG) and provides processing tools to "resize, flip, mirror, rotate, distort, shear and transform images, adjust image colors, apply various special effects, or draw text, lines, polygons, ellipses and Bézier curves".

## 📁 ImageProcessorCLI
_... description of the subcategory ..._

* [GraphicsMagick](http://www.graphicsmagick.org/) [❌ ❌ 🖥️CLI] - Swiss army knife of image processing.

## 📁 ImageToASCII
_... description of the subcategory ..._

* [jp2a](https://csl.name/jp2a/) [❌ ❌ 🖥️CLI] - Command-line tool that converts images to ASCII art in the Linux terminal.

## 📁 ImageViewer(ASCII)
_... description of the subcategory ..._

* [Aewan](http://aewan.sourceforge.net/) [❌ ❌ 🖥️TUI] - Aewan is a multi-layered ASCII graphics/animation editor. It produces stand-alone cat-able ASCII art files and an easy-to-parse format for integration into terminal applications.
* [Artem](nan) [❌ ❌ 🖥️TUI] - Convert images from multiple formats (JPG, PNG, WEBP, etc.) to ASCII art, written in Rust.
* [chafa](nan) [❌ ❌ 🖥️CLI] - Terminal graphics for the 21 st century.
* [img2ascii](nan) [❌ ❌ 🖥️CLI] - Convert images to ASCII art.
* [kakikun](nan) [❌ ❌ 🖥️TUI] - Kakikun is a tool to paint, draw and create ASCII art in your terminal using Unicode characters.
* [LinuxLogo](https://sourceforge.net/projects/linuxlogo/) [❌ ❌ 🖥️CLI] - Display the Linux distribution logo in ASCII format.

## 📁 SVGSlideExporterCLI
_... description of the subcategory ..._

* [inklayers](nan) [❌ ❌ 🖥️CLI] - A command line program that exports layers from an SVG file. It can be used to create slide shows by editing a single SVG file.

## 📁 ScreenshotUtility
_... description of the subcategory ..._

* [scrot](nan) [❌ ❌ 🖥️CLI] - SCReenshot - simple screenshot tool. Main features: window and retangular area capturing export to PNG JPG GIF and others.

## 📁 ai image search
_... description of the subcategory ..._

* [rclip](nan) [🤖 🌐 🖥️CLI] - AI-Powered Command-Line Photo Search Tool.

## 📁 ascii art
_... description of the subcategory ..._

* [ArTTY](nan) [❌ ❌ 🖥️TUI] - Pixel art with optional system info, similar to Neofetch.
* [durdraw](nan) [❌ ❌ 🖥️TUI] - Versatile ASCII and ANSI Art text editor for drawing in the Linux/Unix/macOS terminal, with animation, 256 and 16 colors, Unicode and CP437, and customizable themes.

## 📁 ascii diagram
_... description of the subcategory ..._

* [Diagon](nan) [❌ ❌ 🖥️CLI] - Diagon is an interactive interpreter, that transforms Markdown-style expression into an ASCII-art representation.

## 📁 ascii paint
_... description of the subcategory ..._

* [BlockPaint](nan) [❌ ❌ 🖥️TUI] - BlockPaint is a painting program that allows you to draw pixel graphics in the terminal using the mouse.

## 📁 ascii renderer
_... description of the subcategory ..._

* [3D-renderer](nan) [❌ ❌ 🖥️TUI] - A console-based 3D renderer that uses ASCII characters to display and rotate 3D shapes.

## 📁 ascii screenshot tool
_... description of the subcategory ..._

* [LinuxSSTool](nan) [❌ ❌ 🖥️CLI] - A simple script that takes a screenshot and adds a gradated border using ImageMagick.

## 📁 barcode scanner
_... description of the subcategory ..._

* [zbar](https://zbar.sourceforge.net/) [❌ ❌ 🖥️CLI] - ZBar reads bar codes from various sources, such as video streams and image files. It supports many popular ypes of bar codes including QR Codes.

## 📁 color picker
_... description of the subcategory ..._

* [pik](nan) [❌ ❌ 🖥️TUI] - Color picker for terminal.

## 📁 command-line translator
_... description of the subcategory ..._

* [givegif](nan) [❌ 🌐 🖥️CLI] - GIFs on the command line.
* [imgp](nan) [❌ ❌ 🖥️CLI] - A command line image resizer and rotator for JPEG and PNG images. It can resize (or thumbnail) and rotate thousands of images in a go, at lightning speed, while saving significantly on storage.

## 📁 diagram scripting
_... description of the subcategory ..._

* [D2](nan) [❌ ❌ 🖥️CLI] - D2 is a modern diagram scripting language that turns text to diagrams.

## 📁 enhanced cat
_... description of the subcategory ..._

* [imgcat](nan) [❌ ❌ 🖥️TUI] - Tool to output images in the terminal. Built with bubbletea.

## 📁 gif editors
_... description of the subcategory ..._

* [gifsicle](nan) [❌ ❌ 🖥️CLI] - Create, manipulate, and optimize GIF images and animations.

## 📁 gif tools
_... description of the subcategory ..._

* [gifgen](nan) [❌ ❌ 🖥️CLI] - Simple high quality GIF encoding.

## 📁 graph visualization
_... description of the subcategory ..._

* [Graphviz](https://graphviz.org/) [❌ ❌ 🖥️CLI 🖥️TUI] - Graphviz is open source graph visualization software. It contains several command line tools to generate and manipulate graphs.

## 📁 image optimizer
_... description of the subcategory ..._

* [rimage](nan) [❌ ❌ 🖥️TUI] - A powerful Rust image optimization CLI tool.

## 📁 image preview
_... description of the subcategory ..._

* [catnip](nan) [❌ ❌ 🖥️CLI] - An Image picker using pure bash (C and Go version in the works) and kittys icat and Chafa's Sixel protocol.

## 📁 image processing
_... description of the subcategory ..._

* [Korkut](nan) [❌ ❌ 🖥️CLI] - Quick and simple image processing with the following functions: optimize, convert, crop, resize, rotate, watermark, flip.

## 📁 image tool
_... description of the subcategory ..._

* [gowall](nan) [❌ ❌ 🖥️CLI] - A tool to convert a Wallpaper's color scheme / palette, image to pixel art, color palette extraction, image upsacling with Adversarial Networks  and more image processing features.

## 📁 map viewers
_... description of the subcategory ..._

* [MapSCII](nan) [❌ 🌐 🖥️TUI] - A Braille & ASCII world map renderer for your console

## 📁 maps
_... description of the subcategory ..._

* [Mercator](nan) [❌ ❌ 🖥️TUI] - OpenStreetMap but as terminal user interface (TUI) program.

## 📁 meme generator
_... description of the subcategory ..._

* [greentext](nan) [❌ ❌ 🖥️CLI] - A CLI tool for creating green-text memes.

## 📁 screenshot decorators
_... description of the subcategory ..._

* [deviceframe](nan) [❌ 🌐 🖥️CLI] - Put device frames around mobile/web/progressive app screenshots.

## 📁 screenshot tools
_... description of the subcategory ..._

* [haylxon](nan) [❌ ❌ 🖥️CLI] - Blazing-fast tool to grab screenshots of your domain list right from terminal.

## 📁 space visualizer
_... description of the subcategory ..._

* [astroterm](nan) [❌ ❌ 🖥️TUI] - A planetarium for your terminal. Explore stars, planets, constellations, and more!

## 📁 svg color modifier
_... description of the subcategory ..._

* [svgshift](nan) [❌ ❌ 🖥️CLI] - Command-line utility to quickly adjust the colors in an svg file. Allows for quick and easy color manipulation of svg files by adjusting RGB and HSL values.

## 📁 svg optimizers
_... description of the subcategory ..._

* [SVGO](nan) [❌ ❌ 🖥️CLI] - SVG Optimizer is a Node.js-based tool for optimizing SVG vector graphics files.

## 📁 syntax highlighting
_... description of the subcategory ..._

* [colout](nan) [❌ ❌ 🖥️CLI] - colout read lines of text stream on the standard input and output characters matching a given regular expression pattern in given color and style.

## 📁 terminal image
_... description of the subcategory ..._

* [TermImg](nan) [❌ ❌ 🖥️CLI] - termimg tries to draw images into terminals. The rectangular drawing area is given in cell coordinates (not pixels). Origin is the upper-left corner.

## 📁 terrain generator
_... description of the subcategory ..._

* [TerrainGenerator](nan) [❌ ❌ 🖥️TUI] - 2D Terrain Generator to create procedural 2D worlds and maps.

# history
[Back to TOC](#📚-contents)

Programs to replace or improve the management of command line history
## 📁 command-line translator
_... description of the subcategory ..._

* [Bevel](nan) [❌ ❌ 🖥️CLI] - Command line history in an SQLite database for effective reuse.

## 📁 history manager
_... description of the subcategory ..._

* [atuin](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Atuin replaces your existing shell history with a SQLite database, and records additional context for your commands. Additionally, it provides optional and fully encrypted synchronization of your history between machines, via an Atuin server.
* [hstr](nan) [❌ ❌ 🖥️TUI] - Manage the shell history. It has a powerful visual search and execution of previous commands, and history editing capabilities.

## 📁 productivity
_... description of the subcategory ..._

* [hiSHtory](nan) [❌ 🌐 ❌] - A better shell history that stores context (directory, succeeded or failed, how long it took, etc). The history is stored locally and end-to-end encrypted for syncing to other computers.

# launcher
[Back to TOC](#📚-contents)

Applications to launch/execute programs, either interactively, automatically, in parallel, etc.
## 📁 ApplicationLauncherTUI
_... description of the subcategory ..._

* [rofi](nan) [❌ ❌ 🖥️TUI] - A window switcher, application launcher and dmenu replacement.

## 📁 CLI task runner
_... description of the subcategory ..._

* [Mxflow-cli](nan) [❌ ❌ 🖥️CLI] - A modern, general purpose CLI task runner with human-readable YAML config file.

## 📁 CommandOrchestratorCLI
_... description of the subcategory ..._

* [sake](nan) [❌ 🌐 🖥️CLI] - A command runner for local and remote hosts. You define servers and tasks in sake.yaml file and then run the tasks on the servers.

## 📁 FileWatcherCLI
_... description of the subcategory ..._

* [Gaze](nan) [❌ ❌ 🖥️CLI] - Runs a command, right after you save a file.

## 📁 MultiCommandRunnerTUI
_... description of the subcategory ..._

* [mprocs](nan) [❌ ❌ 🖥️TUI] - mprocs runs multiple commands in parallel and shows output of each command separately.
* [procmux](nan) [❌ ❌ 🖥️TUI] - A TUI utility for running multiple commands in parallel in easily switchable terminals.

## 📁 app launcher
_... description of the subcategory ..._

* [Sway-Talisman](nan) [❌ ❌ 🖥️CLI] - Terminal application launcher in scratchpad, minimalist and native.

## 📁 batch queue
_... description of the subcategory ..._

* [task-spooler](http://vicerveza.homeunix.net/~viric/soft/ts/) [❌ ❌ 🖥️CLI] - A Unix batch system that can be used to add the Linux commands to the queue and execute them one after the other in numerical order (ascending order, to be precise). This can be very useful when you have to run a lot of commands, but you don't want to waste time waiting for one command to finish and run the next command. You can queue it all up and Task Spooler will execute them one by one. In the mean time, you can do other activities.

## 📁 build tool
_... description of the subcategory ..._

* [Task](https://taskfile.dev/) [❌ ❌ 🖥️CLI] - A task runner / simpler Make alternative written in Go.

## 📁 command palette
_... description of the subcategory ..._

* [Marker](nan) [❌ ❌ 🖥️TUI] - The terminal command palette.

## 📁 file watchers
_... description of the subcategory ..._

* [entr](nan) [❌ ❌ 🖥️CLI] - Event Notify Test Runner - Run an arbitrary command when files change.

## 📁 launcher
_... description of the subcategory ..._

* [lmt](nan) [❌ ❌ 🖥️TUI] - A program that can be used to run applications with resource limits enforced using cgroupsv2 on Linux; it allows setting limits on CPU usage, memory usage, and the number of cores for a process.
* [menu.sh](nan) [❌ ❌ 🖥️TUI] - A lightweight menu and launcher for text-mode consoles. Menus are described with YAML and sub-menus are supported.
* [paneru](nan) [❌ ❌ 🖥️TUI] - Launcher panel from the terminal.
* [taverner](nan) [❌ ❌ 🖥️TUI] - CLI launcher menu for games (or anything), the UNIX way.

## 📁 parallel execution
_... description of the subcategory ..._

* [parallel](https://www.gnu.org/software/parallel/) [❌ ❌ 🖥️CLI] - A shell tool from GNU for executing jobs in parallel using one or more computers, it can split the input and pipe it into commands in parallel.

## 📁 shell
_... description of the subcategory ..._

* [climenu](nan) [❌ ❌ 🖥️CLI] - Compact application for creating shell menus with executable entries. Use it to build straightforward static shortcut menus or dynamically generate advanced menus for more complex programs.
* [shell2http](nan) [❌ 🌐 🖥️CLI] - Executing shell commands via HTTP server.

## 📁 shell launcher
_... description of the subcategory ..._

* [hypershell](nan) [❌ 🌐 🖥️CLI] - Spawn shells anywhere. Fully peer-to-peer, authenticated, and end-to-end encrypted.

## 📁 task manager
_... description of the subcategory ..._

* [pueue](nan) [❌ ❌ 🖥️TUI] - Pueue is a command-line task management tool for sequential and parallel execution of long-running tasks.

## 📁 task runner
_... description of the subcategory ..._

* [foy](nan) [❌ ❌ 🖥️CLI] - A simple, light-weight, type-friendly and modern task runner for general purpose.
* [mk](nan) [❌ ❌ 🖥️TUI] - Interactive task runner for Makefile or Taskfile.yml, designed to interactively execute make commands. It provides a user-friendly interface to select and run predefined commands, making it easier to manage and execute build tasks.

## 📁 vagrant helper
_... description of the subcategory ..._

* [Violet](nan) [❌ ❌ 🖥️TUI] - Colorful TUI frontend to run Vagrant commands.

# ls
[Back to TOC](#📚-contents)

List directory content and files, with colors or icons; alternatives to `ls`
## 📁 EnhancedLsRewrite
_... description of the subcategory ..._

* [lsd](nan) [❌ ❌ 🖥️CLI] - This project is a rewrite of GNU ls with lots of added features like colors, icons, tree-view, more formatting options etc. The project is heavily inspired by the super colorls project.

## 📁 GitStatistics
_... description of the subcategory ..._

* [ll](nan) [❌ ❌ 🖥️CLI] - ls with git status.

## 📁 ModernFileManager
_... description of the subcategory ..._

* [eza](nan) [❌ ❌ 🖥️CLI] - eza is a modern, _maintained_ replacement for `ls`, built on `exa`.

## 📁 RustLsReplacement
_... description of the subcategory ..._

* [exa](https://the.exa.website/) [❌ ❌ 🖥️CLI] - Replacement for 'ls' written in Rust, with colors and several additional "views". As of today, the README says it is currently unmaintained and the only maintainer is unreachable. See `eza` for a maintained fork. 
* [nat](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Complete replacement for the `ls` command.
* [pretty-ls](nan) [❌ ❌ 🖥️CLI] - Rust ls clone with pretty colors.

## 📁 enhanced cat
_... description of the subcategory ..._

* [colorls](nan) [❌ ❌ 🖥️CLI] - A Ruby script that colorizes the `ls` output with color and icons.

## 📁 ls color
_... description of the subcategory ..._

* [vivid](nan) [❌ ❌ 🖥️CLI] - A themeable LS_COLORS generator with a rich filetype datebase.

## 📁 ls color tool
_... description of the subcategory ..._

* [lscoltui](nan) [❌ ❌ 🖥️TUI] - A TUI tool for changing the colours of ls.

## 📁 tree viewer
_... description of the subcategory ..._

* [stree](nan) [❌ ❌ 🖥️CLI] - A CLI tool designed to visualize the directory tree structure of an S3 bucket.

# markdown
[Back to TOC](#📚-contents)

Utilities to display, convert and reformat Markdown files
## 📁 MarkdownBookBuilder
_... description of the subcategory ..._

* [mdBook](nan) [❌ ❌ 🖥️CLI] - Create book from Markdown files.

## 📁 MarkdownTUI
_... description of the subcategory ..._

* [glow](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - TUI that renders Markdown files, with keybindings similar to `less` and support for styles and cloud encrypted storing

## 📁 MarkdownViewer(GUI/CLI)
_... description of the subcategory ..._

* [Terminal Markdown Viewer](nan) [❌ ❌ 🖥️CLI] - Python based Markdown viewer with themes source code highlighting and a directory change monitor.

## 📁 knowledge base
_... description of the subcategory ..._

* [mdt](nan) [❌ ❌ 🖥️TUI] - MarkDown in the Terminal. A Markdown viewer with themes defined by JSON files and interactive mode to open links and word-wrapping adaptable to the terminal width.

## 📁 markdown parser
_... description of the subcategory ..._

* [lowdown](https://kristaps.bsd.lv/lowdown/) [❌ ❌ 🖥️CLI] - Markdown translator (HTML5, roff, LaTeX, gemini, OpenDocument, and terminal output)

## 📁 markdown preview
_... description of the subcategory ..._

* [Grip](nan) [❌ ❌ 🖥️CLI] - GitHub Readme Instant Preview - Preview Markdown files as GitHub would render them.

## 📁 markdown tool
_... description of the subcategory ..._

* [mdformat](nan) [❌ ❌ 🖥️CLI] - Mdformat is an opinionated Markdown formatter that can be used to enforce a consistent style in Markdown files.

## 📁 markdown tools
_... description of the subcategory ..._

* [DocToc](nan) [❌ ❌ 🖥️CLI] - Generates table of contents for Markdown files inside local git repository. Links are compatible with anchors generated by GitHub or other sites.

## 📁 markdown viewer
_... description of the subcategory ..._

* [Frogmouth](nan) [❌ 🌐 🖥️TUI] - A Markdown viewer / browser for the terminal.
* [mdcat](nan) [❌ ❌ 🖥️CLI] - cat for Markdown

# monitor
[Back to TOC](#📚-contents)

Applications to display the usage of system resources: network, memory, power, etc.
## 📁 BenchmarkCLI
_... description of the subcategory ..._

* [hyperfine](nan) [❌ ❌ 🖥️CLI] - A command-line benchmarking tool.

## 📁 DiskInspectorCLI
_... description of the subcategory ..._

* [dysk](https://dystroy.org/dysk) [❌ ❌ 🖥️CLI] - A thing to get information on your mounted disks

## 📁 IO monitor
_... description of the subcategory ..._

* [pv](http://www.ivarch.com/programs/pv.shtml) [❌ ❌ 🖥️CLI] - The pv command is used to monitor the progress of data through pipe.

## 📁 ImageViewer(ASCII)
_... description of the subcategory ..._

* [neofetch](nan) [❌ ❌ 🖥️CLI] - Neofetch is a CLI system information tool written in BASH. Neofetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice. Currently abandoned.
* [screenFetch](nan) [❌ ❌ 🖥️CLI] - It can be used to generate one of those nifty terminal theme information + ASCII distribution logos. It auto-detects the distribution and display an ASCII version of that distribution's logo and some valuable information to the right.

## 📁 LogViewerTUI
_... description of the subcategory ..._

* [The Logfile Navigator](https://lnav.org/) [❌ ❌ 🖥️TUI] - An advanced and colorful log file viewer with TUI interface.

## 📁 SystemHardwareInspector
_... description of the subcategory ..._

* [dmidecode](https://www.nongnu.org/dmidecode/) [❌ ❌ 🖥️CLI] - System information utility.

## 📁 battery monitor
_... description of the subcategory ..._

* [senzu](nan) [❌ ❌ 🖥️CLI] -  CLI tool to get the battery percentage.

## 📁 load monitor
_... description of the subcategory ..._

* [ttyload](http://www.daveltd.com/src/util/ttyload/) [❌ ❌ 🖥️TUI] - Lightweight utility that offers a color-coded graph of load averages over time, enabling a graphical tracking of system average load.

## 📁 log viewer
_... description of the subcategory ..._

* [multitail](https://www.vanheusden.com/multitail/) [❌ ❌ 🖥️TUI] - Open multiple log files in a single terminal window and monitor them in real-time.

## 📁 memory usage
_... description of the subcategory ..._

* [smem](https://www.selenic.com/smem/) [❌ ❌ 🖥️CLI] - Python program that reports memory usage; it can report the "proportional set size" (PSS), a meaningful representation of the amount of memory used by libraries and applications in a virtual memory system; it has built-in chart generation.

## 📁 monitoring
_... description of the subcategory ..._

* [updo](nan) [❌ 🌐 🖥️CLI] - Uptime monitoring CLI tool with alerting and advanced settings.

## 📁 neofetch
_... description of the subcategory ..._

* [HyFetch](nan) [❌ ❌ 🖥️CLI] - A fork of the abandoned [Neofetch](https://github.com/dylanaraps/neofetch), HyFetch displays information about your system next to an image, your OS logo, or any ASCII file of your choice.

## 📁 network grep
_... description of the subcategory ..._

* [ngrep](http://ngrep.sourceforge.net/) [❌ ❌ 🖥️CLI] - (Network grep) applies the `grep` logic to the network layer, allowing to match regular expressions against data payloads of packets; it recognizes IPv4/6, TCP, UDP, ICMPv4/6, IGMP and Raw across Ethernet, PPP, SLIP, FDDI, Token Ring and null interfaces.

## 📁 network scanner
_... description of the subcategory ..._

* [ptrstream](nan) [❌ ❌ 🖥️CLI] - High-performance distributed PTR record scanner with real-time streaming output.

## 📁 packet analyzer
_... description of the subcategory ..._

* [tcpterm](nan) [❌ ❌ 🖥️TUI] - tcpterm is a packet visualizer in TUI.

## 📁 power monitor
_... description of the subcategory ..._

* [powertop](https://01.org/powertop) [❌ ❌ 🖥️TUI] - A `top`-like utility to monitor the sources of power consumption, allows turning on/off many components, quite useful to track possible power-related issues.

## 📁 ram info
_... description of the subcategory ..._

* [ramfetch](nan) [❌ ❌ 🖥️CLI] - A fetch which displays memory info using /proc/meminfo.

## 📁 resource monitor
_... description of the subcategory ..._

* [noti](nan) [❌ ❌ 🖥️CLI] - Monitor a process and trigger a notification.
* [slurm](nan) [❌ 🌐 🖥️TUI] - Yet another network load monitor.
* [tmon](nan) [❌ ❌ 🖥️TUI] - A tiny system monitor for Linux.
* [whowatch](https://www.tecmint.com/whowatch-monitor-linux-users-and-processes-in-real-time/) [❌ ❌ 🖥️TUI] - Monitor Linux Users and Processes in Real Time.

## 📁 serial monitor
_... description of the subcategory ..._

* [aserial](nan) [❌ ❌ 🖥️TUI] - A serial monitor with error/warning highlighting and scrollable interface.

## 📁 syscall monitor
_... description of the subcategory ..._

* [sysdig](https://www.sysdig.org/) [❌ ❌ 🖥️CLI 🖥️TUI] - A TUI for capturing system calls and events from the Linux kernel. Allows you to save, filter, and analyze the data. Like `strace` + `tcpdump` + `htop` + `iftop` + `lsof` + Wireshark for the entire system.

## 📁 system fetcher
_... description of the subcategory ..._

* [fastfetch](nan) [❌ ❌ 🖥️TUI] - An actively maintained, feature-rich and performance oriented, neofetch like system information tool.
* [nitchplusplus](nan) [❌ ❌ 🖥️TUI] - A fast system information fetch tool.
* [tinyfetch](nan) [❌ ❌ 🖥️TUI] - Python and system information command-line fetch tool.

## 📁 system info
_... description of the subcategory ..._

* [Batfetch](nan) [❌ ❌ 🖥️TUI] - A command-line tool that displays detailed information about the battery of your device in a clean and organized way.
* [Fastfetch](nan) [❌ ❌ 🖥️CLI] - Like Neofetch, but much faster because written in C.
* [GFetch](nan) [❌ ❌ 🖥️CLI] - A simple fetch script written in Python.
* [macchina](nan) [❌ ❌ 🖥️TUI] - Fast, minimal and customizable system information frontend.
* [zfxtop](nan) [❌ ❌ 🖥️TUI] - Self described as “fetch top written by bubbletea enjoyer”.

## 📁 system information
_... description of the subcategory ..._

* [inxi](http://smxi.org/docs/inxi.htm) [❌ ❌ 🖥️CLI] - A comprehensive system information script; provides information about CPU, graphics, audio and network devices, drives and partitions, sensors; implemented as a Bash script.

## 📁 system monitor
_... description of the subcategory ..._

* [glances](https://nicolargo.github.io/glances/) [❌ ❌ 🖥️TUI] - A comprehensive and detailed system monitor; monitored parameters include: CPU, memory, load, process list, network interfaces, disk I/O, sensors, filesystems, docker, system info, uptime.
* [llmtop](nan) [🤖 ❌ 🖥️TUI] - A system monitoring tool powered by LLMs that provides real-time insights about your system's performance.

## 📁 terminal sharing
_... description of the subcategory ..._

* [sntop](nan) [❌ ❌ ❌] - A simple network top for monitoring connectivity.

# monitor-top
[Back to TOC](#📚-contents)

Programs to list and monitor currently running processes; alternatives to the `top` command
## 📁 FastFindAlternative
_... description of the subcategory ..._

* [ytop](nan) [❌ ❌ 🖥️TUI] - TUI system monitor written in Rust.

## 📁 IO monitor
_... description of the subcategory ..._

* [iotop](http://guichaz.free.fr/iotop/) [❌ ❌ 🖥️TUI] - "A Python program with a top like UI used to show of behalf of which process is the I/O going on".

## 📁 ResourceMonitorTUI
_... description of the subcategory ..._

* [tiptop](nan) [❌ ❌ 🖥️TUI] - A command-line system monitoring tool in the spirit of top, written in Python. It displays various interesting system stats and graphs them. Works on all operating systems.

## 📁 gpu monitor
_... description of the subcategory ..._

* [amdgpu-top](nan) [❌ ❌ 🖥️TUI] - A tool that display AMD GPU utilization and information, gathered from performance counters (GRBM, GRBM2), sensors, fdinfo, and AMDGPU driver.
* [gputop](nan) [❌ ❌ 🖥️CLI] - A simple command-line utility for querying and monitoring GPU status.
* [nvtop](nan) [❌ ❌ 🖥️TUI] - A top like task monitor for AMD, Intel and NVIDIA GPUs, that can handle multiple GPUs and print information about them in a htop-familiar way.
* [radeontop](nan) [❌ ❌ 🖥️TUI] - View your AMD GPU utilization, both for the total activity percent and individual blocks.

## 📁 process monitor
_... description of the subcategory ..._

* [PCtrl](nan) [❌ ❌ 🖥️TUI] - Robust, featureful, easy-to-use and powerful process manager.
* [top](nan) [❌ ❌ 🖥️TUI] - The classical Unix utility that provides a rolling display of top CPU using processes.

## 📁 process viewer
_... description of the subcategory ..._

* [htop](http://hisham.hm/htop/) [❌ ❌ 🖥️TUI] - An interactive process viewer for Unix; improves the UI of `top`, by adding real-time meters and colors.
* [nvitop](nan) [❌ ❌ 🖥️TUI] - An interactive NVIDIA-GPU process viewer and beyond, the one-stop solution for GPU process management.

## 📁 process viewer,
_... description of the subcategory ..._

* [procs](nan) [❌ ❌ 🖥️TUI] - A modern replacement for ps written in Rust.

## 📁 resource monitor
_... description of the subcategory ..._

* [atop](https://www.atoptool.nl/index.php) [❌ ❌ 🖥️TUI] - Atop is TUI performance monitor for Linux; it reports the activity of all processes (even if processes have finished during the interval), daily logging of system and process activity for long-term analysis, overloaded system resources, etc.
* [bashtop](nan) [❌ ❌ 🖥️TUI] - Resource monitor that shows usage and stats for processor, memory, disks, network, and processes.
* [below](nan) [❌ ❌ 🖥️TUI] - A time traveling resource monitor for modern Linux systems
* [bottom](nan) [❌ ❌ 🖥️TUI] - Yet another cross-platform graphical process/system monitor.
* [bpytop](nan) [❌ ❌ 🖥️TUI] - Linux/macOS/FreeBSD resource monitor with a nice interface.
* [gotop](nan) [❌ ❌ 🖥️TUI] - A terminal based graphical activity monitor inspired by gtop and vtop.
* [nmon](https://nmon.sourceforge.io/pmwiki.php) [❌ ❌ 🖥️TUI] - Nigel's performance Monitor for Linux.

## 📁 system monitor
_... description of the subcategory ..._

* [Btop++](nan) [❌ ❌ 🖥️TUI] - Resource monitor that shows usage and stats for processor, memory, disks, network, and processes. C++ version and continuation of [bashtop](https://github.com/aristocratos/bashtop) and [bpytop](https://github.com/aristocratos/bpytop).
* [gtop](nan) [❌ ❌ 🖥️TUI] - System monitoring dashboard for terminal written in Node.js.
* [s-tui](nan) [❌ ❌ 🖥️TUI] - Stress-Terminal UI, s-tui, monitors CPU temperature, frequency, power, and utilization in a graphical way from the terminal.
* [ttop](nan) [❌ ❌ 🖥️TUI] - top-like system monitoring tool with TUI, historical data service and triggers.
* [vtop](nan) [❌ ❌ 🖥️TUI] - Alternative to top with several additional stats.
* [zenith](nan) [❌ ❌ 🖥️TUI] - Sort of like top or htop but with zoom-able charts, CPU, GPU, network, and disk usage

## 📁 task manager
_... description of the subcategory ..._

* [TTV](nan) [❌ ❌ 🖥️TUI] - terminal-task-viewer: a lightweight terminal tool to manage processes in Unix machines.

# music
[Back to TOC](#📚-contents)

Music players, podcast, synthesizers, downloaders, online radios
## 📁 AudioMixer
_... description of the subcategory ..._

* [Alsamixer](http://www.alsa-project.org/main/index.php/Main_Page) [❌ ❌ 🖥️TUI] - ALSA mixer with curses interfaces.

## 📁 AudioMixerCLI
_... description of the subcategory ..._

* [pulsemixer](nan) [❌ ❌ 🖥️TUI] - CLI and curses mixer for PulseAudio.

## 📁 LightweightAudioPlayer
_... description of the subcategory ..._

* [bash_radio_player](nan) [❌ 🌐 🖥️TUI] - Terminal Radio Player using mpv and fzf.
* [cTune](nan) [❌ 🌐 🖥️TUI] - A ncurses based internet radio player written in C for Linux.
* [cue](nan) [❌ ❌ 🖥️CLI] - A command-line music player.
* [dzr](nan) [❌ ❌ 🖥️CLI] - Command Line deezer.com Player for Linux, BSD, Android, Windows.
* [jammer](nan) [❌ 🌐 🖥️TUI] - Multiplatform light-weight TUI music player with Soundcloud & Youtube support, with effects.
* [lowfi](nan) [❌ 🌐 🖥️TUI] - A music player through your terminal, with the option to open YouTube in the browser.
* [MOC](https://moc.daper.net/) [❌ ❌ 🖥️TUI] - (music on console) - a powerful and easy to use console audio player, user interface a la Midnight Commander, plenty of features, fully controllable from the keyboard.
* [Mp3blaster](http://www.mp3blaster.org/?m=1) [❌ ❌ 🖥️TUI] - Audio player for the text console.
* [mpg123](http://mpg123.org/) [❌ ❌ 🖥️CLI] - Quick `mp3` sound file player; no visual interface, just a command-line audio file player for `mp3` files.
* [mps-youtube](nan) [❌ 🌐 🖥️TUI] - A curses player for music tracks from YouTube; it allows searching for songs and playlists; it downloads the video, extracts the audio track and plays it; handles local playlists and many configuration parameters.
* [MusicPlayerPlus](nan) [❌ 🌐 🖥️CLI] - Featureful ncurses based MPD client inspired by ncmpc with integration for Beets, spectrum visualization,Bandcamp/Soundcloud, asciimatics, cantata, and more.
* [musikcube](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A cross-platform, terminal-based audio engine, library, player and server written in C++.
* [PyRadio](nan) [❌ 🌐 🖥️TUI] - Curses based internet radio player.
* [radio-active](nan) [❌ 🌐 🖥️TUI] - Internet radio player with 40k+ stations.
* [Siren](https://www.kariliq.nl/siren/) [❌ ❌ 🖥️TUI] - Siren is a text-based audio player for UNIX-like operating systems.
* [sonicradio](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A TUI radio player making use of Radio Browser API and Bubbletea.
* [spotify-player](nan) [❌ 🌐 🖥️TUI] - spotify-player is a fast, easy to use, and configurable terminal music player having feature parity with the official Spotify application.
* [termusic](nan) [❌ ❌ 🖥️TUI] - Terminal Music Player written in Rust.
* [Tizonia](nan) [❌ 🌐 🖥️CLI] - Command-line cloud music player for Linux with support for Spotify, Google Play Music, YouTube, SoundCloud, TuneIn, iHeartRadio, Plex servers and Chromecast devices.

## 📁 MusicAppFramework
_... description of the subcategory ..._

* [kord](nan) [❌ ❌ ❌] - A Python framework that provides programmers with a simple API for the creation of music-based applications.

## 📁 MusicDownloaderCLI
_... description of the subcategory ..._

* [Instant Music Downloader](nan) [❌ ❌ 🖥️CLI] - Instantly download any song!

## 📁 MusicLibraryManager
_... description of the subcategory ..._

* [beets](nan) [❌ ❌ 🖥️CLI] - Beets is the media library management system for obsessive music geeks: catalogs your collection, automatically improving its metadata as it goes.

## 📁 PodcastClientTUI
_... description of the subcategory ..._

* [castero](nan) [❌ 🌐 🖥️TUI] - A TUI podcast client for the terminal.

## 📁 SpotifyClientTUI
_... description of the subcategory ..._

* [Spotify TUI](nan) [❌ ❌ 🖥️TUI] - A Spotify client for the terminal written in Rust.

## 📁 TerminalAudioPlayer(ogg)
_... description of the subcategory ..._

* [ogg123](https://www.xiph.org/downloads/) [❌ ❌ 🖥️CLI] - Quick `ogg` sound file player; no visual interface, just a command-line audio file player for the free and open `ogg` file format.

## 📁 TerminalMusicPlayer
_... description of the subcategory ..._

* [cmus](https://cmus.github.io/) [❌ ❌ 🖥️TUI] - A fast and lightweight audio player with configurable keybindings and playlist support.

## 📁 TerminalMusicPlayer(MPD)
_... description of the subcategory ..._

* [ncmpcpp](https://rybczak.net/ncmpcpp/) [❌ 🌐 🖥️TUI] - NCurses Music Player Client (Plus Plus) - featureful ncurses based MPD client inspired by ncmpc. Relevant features: tag editor, playlist editor, easy to use search engine, media library, music visualizer, ability to fetch artist info from [last.fm](https://www.last.fm/), new display mode, alternative user interface, ability to browse and add files from outside of MPD music directory.

## 📁 TerminalMusicVisualizer
_... description of the subcategory ..._

* [Tera](nan) [❌ ❌ 🖥️TUI] - Terminal Radio: an easy-to-use CLI music player to play favorite music, radio stations and explore various radio stations from the terminal only.

## 📁 TextToSpeech
_... description of the subcategory ..._

* [espeak](http://espeak.sourceforge.net/) [❌ ❌ 🖥️CLI] - A compact open source software speech synthesizer for English and other languages.

## 📁 YouTubeAudioCLI
_... description of the subcategory ..._

* [muCLIar](nan) [❌ 🌐 🖥️CLI] - YouTube automator bringing you your music right on your CLI.

## 📁 YouTubeToMP3Downloader
_... description of the subcategory ..._

* [yt-audio](nan) [❌ 🌐 🖥️CLI] - A simple, configurable youtube-dl wrapper to download and manage YouTube audio.

## 📁 audio player
_... description of the subcategory ..._

* [amused](https://projects.omarpolo.com/amused.html) [❌ ❌ 🖥️TUI] - Minimal music player that composes well, or aims to do so, with other tools thought.
* [kew](nan) [❌ ❌ 🖥️CLI] - A command-line music player with gapless playback and simple playlist management.
* [kmp3](nan) [❌ ❌ 🖥️TUI] - Little music player with some peculiar characteristics.

## 📁 audio visualizer
_... description of the subcategory ..._

* [cli-viz](nan) [❌ ❌ 🖥️TUI] - An audio visualizer that runs in the linux terminal and reacts to the microphone.

## 📁 audiobook manager
_... description of the subcategory ..._

* [BadaBoomBooks](nan) [❌ 🌐 🖥️TUI] - Quickly organize audiobooks using a terminal and web-browser.

## 📁 cli midi
_... description of the subcategory ..._

* [line](nan) [❌ ❌ 🖥️CLI] - Tiny command-line midi sequencer and language for live coding.

## 📁 cli music player
_... description of the subcategory ..._

* [Gomu](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Gomu is intuitive, powerful CLI music player. It has embedded scripting language and event hook to enable user to customize their config extensively.

## 📁 debugging
_... description of the subcategory ..._

* [fme](nan) [❌ ❌ 🖥️CLI] - Flexible metadata editor that allows editing the metadata of music files.

## 📁 media control
_... description of the subcategory ..._

* [mpvc](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A minimal mpc-like CLI and TUI for controlling mpv from the shell.

## 📁 music catalog
_... description of the subcategory ..._

* [discodos](nan) [❌ ❌ 🖥️CLI] - A CLI tool for DJ's and record collectors based on the discogs.com collection feature that allows analyzing and organize DJ sets.

## 📁 music player
_... description of the subcategory ..._

* [maestro-cli](nan) [❌ ❌ 🖥️CLI] - A command-line tool to play songs (or any audio, really) in the terminal.
* [mfp](nan) [❌ ❌ 🖥️CLI] - A command-line utility for playing music mixes for programming & focus (from [musicforprogramming.net](musicforprogramming.net)), unlocking the flow state.
* [opencubicplayer](nan) [❌ ❌ 🖥️TUI] - Open Cubic Player (UNIX fork) is a music visualizer for various tracked music formats (amiga modules, S3M, IT), chiptunes and other formats related to demoscene.
* [pytunes](nan) [❌ 🌐 🖥️CLI] - Self-hosted music streaming service.
* [sptui](nan) [❌ 🌐 🖥️TUI] - Spotify TUI player, written in Go.

## 📁 music scraper
_... description of the subcategory ..._

* [musicScraper](nan) [❌ 🌐 🖥️CLI] - CLI tool for scraping information from musical websites (Rateyourmusic, Metal Archives), with nice album ASCII art.

## 📁 music theory
_... description of the subcategory ..._

* [mzk](nan) [❌ ❌ 🖥️CLI] - Music theory helper.

## 📁 podcast downloader
_... description of the subcategory ..._

* [podboat](https://newsboat.org/) [❌ 🌐 🖥️CLI] - A podcast download manager for text terminals, a companion for the newsboat RSS-reader.

## 📁 podcast ui for newsboat
_... description of the subcategory ..._

* [podbit](nan) [❌ 🌐 🖥️TUI] - Podbit is a replacement for newsboat's standard podboat tool for listening to podcasts. It is minimal, performant and tries to focus just on being a podcast client, rather than an RSS reader.

## 📁 radio player
_... description of the subcategory ..._

* [radio-beats](nan) [❌ 🌐 🖥️TUI] - Rofi-like menu for playing radio stations.

## 📁 spotify client
_... description of the subcategory ..._

* [ncspot](nan) [❌ 🌐 🖥️TUI] - Cross-platform ncurses Spotify client written in Rust, inspired by ncmpc and the likes.

## 📁 youtube client
_... description of the subcategory ..._

* [ytui-music](nan) [❌ 🌐 🖥️TUI] - YouTube client in terminal for music (lightweight YouTube client).

# networking
[Back to TOC](#📚-contents)

Networks and communication tools: bandwidth monitoring, packet inspection, remote connection, VPNs, terminal sharing, etc.
## 📁 BluetoothManagerTUI
_... description of the subcategory ..._

* [bluetuith](nan) [❌ ❌ 🖥️TUI] - A TUI-based Bluetooth connection manager, which can interact with Bluetooth adapters and devices. It aims to be a replacement to most Bluetooth managers, like blueman.

## 📁 HTTPSProxyAnalyzer
_... description of the subcategory ..._

* [mitmproxy](https://mitmproxy.org/) [❌ ❌ 🖥️CLI 🖥️TUI] - An interactive HTTPS proxy.

## 📁 ListManagerCLI
_... description of the subcategory ..._

* [Wishlist](nan) [❌ ❌ 🖥️CLI] - With Wishlist you can have a single entrypoint for multiple SSH endpoints.

## 📁 NetworkToolCLI
_... description of the subcategory ..._

* [Rustcat](nan) [❌ 🌐 🖥️CLI] - Netcat Alternative in Rust.

## 📁 NetworkTrafficMonitor
_... description of the subcategory ..._

* [bandwhich](nan) [❌ ❌ 🖥️TUI] - Terminal bandwidth utilization tool.

## 📁 OpenAPIEditorCLI
_... description of the subcategory ..._

* [Optic](https://www.useoptic.com/) [❌ 🌐 🖥️CLI] - Optic's Open Source tools make OpenAPI and API-first practices easy for any team to adopt.

## 📁 RedditClientTUI
_... description of the subcategory ..._

* [redive](nan) [❌ ❌ 🖥️TUI] - Trace URL redirections in the terminal.

## 📁 SpeedTestCLI
_... description of the subcategory ..._

* [speedtest-net](nan) [❌ 🌐 🖥️CLI] - Test internet connection speed and ping using speedtest.net.

## 📁 ad blocker
_... description of the subcategory ..._

* [adless](nan) [❌ ❌ 🖥️CLI] - Local domains blocker written in Go.

## 📁 api client
_... description of the subcategory ..._

* [TGORQ](nan) [❌ 🌐 🖥️TUI] - Terminal GO ReQuest (TGORQ) is a Vim-like lightweight CLI tool for performing HTTP requests.

## 📁 bandwidth monitor
_... description of the subcategory ..._

* [bmon](nan) [❌ ❌ 🖥️TUI] - A monitoring and debugging tool to capture networking related statistics and prepare them visually in a human friendly way.

## 📁 bluetooth tool
_... description of the subcategory ..._

* [blueutil-tui](nan) [❌ ❌ 🖥️TUI] - TUI for Mac to interact with bluetooth devices via blueutil.

## 📁 cli-to-web
_... description of the subcategory ..._

* [GoTTY](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - Turn CLI tools into web applications; basically, it runs a command and starts a server so that the output can be displayed in a web page.

## 📁 debugging
_... description of the subcategory ..._

* [sslh](nan) [❌ 🌐 🖥️CLI] - A ssl/ssh multiplexer (Applicative Protocol Multiplexer) that allows, for example, to share SSH and HTTPS on the same port.

## 📁 dns client
_... description of the subcategory ..._

* [doggo](https://doggo.mrkaran.dev/) [❌ ❌ 🖥️CLI] - DNS client for humans. Features include: colors, tabular and JSON formats, and reverse DNS lookup.

## 📁 dns tools
_... description of the subcategory ..._

* [dog](nan) [❌ 🌐 🖥️CLI] - dog is a command-line DNS client. It has colorful output, understands normal command-line argument syntax, supports the DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
* [dug](nan) [❌ 🌐 🖥️CLI] - A global DNS propagation checker that gives pretty output.

## 📁 file manager
_... description of the subcategory ..._

* [humble-explorer](nan) [❌ ❌ 🖥️TUI] - Cross-platform, command-line and human-friendly Bluetooth Low Energy scanner.

## 📁 file‑sharing
_... description of the subcategory ..._

* [quickserve](nan) [❌ 🌐 🖥️CLI] - Very simple HTTP server written in Python for quickly sharing files on an ad-hoc basis. Aside from opening a port in your firewall if you have one, it requires no setup and should work with no hassle.

## 📁 grpc client
_... description of the subcategory ..._

* [chiko](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - The ultimate beauty gRPC Client on your Terminal: a simple tool to interact with gRPC services using a beautiful terminal interface.

## 📁 http client
_... description of the subcategory ..._

* [TReq](nan) [❌ 🌐 🖥️CLI] - A CLI tool for effortless HTTP requests.
* [wuzz](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Interactive CLI tool for HTTP inspection.

## 📁 http proxy
_... description of the subcategory ..._

* [hflow](nan) [❌ ❌ 🖥️CLI] - A command-line, debugging http/s proxy server.

## 📁 ip generator
_... description of the subcategory ..._

* [generate-ip](https://generate-ip.org) [❌ ❌ 🖥️CLI] - Randomly generate, format, and validate IPv4 + IPv6 + MAC addresses.

## 📁 ip geolocation
_... description of the subcategory ..._

* [geolocate](https://geolocatejs.org) [❌ ❌ 🖥️CLI] - Fetch IP geolocation data.

## 📁 kubectl port forwarder
_... description of the subcategory ..._

* [kftray](nan) [❌ ❌ 🖥️CLI] - kubectl port-forward on steroids, manage and share multiple k8s port forwards, with support for UDP, proxy through the k8s cluster, and github state sync.

## 📁 load testing
_... description of the subcategory ..._

* [oha](nan) [❌ 🌐 🖥️CLI] - oha is a tiny program that sends some load to a web application and show real-time TUI.

## 📁 log analyzer
_... description of the subcategory ..._

* [goaccess](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - GoAccess is a real-time web log analyzer and interactive viewer, that provides fast and valuable HTTP statistics.

## 📁 mock server
_... description of the subcategory ..._

* [echo](nan) [❌ ❌ 🖥️CLI] - Speedy API emulation facilitated by a reverse proxy and mock JSON server.

## 📁 monitoring
_... description of the subcategory ..._

* [rtop](http://www.rtop-monitor.org/) [❌ ❌ 🖥️CLI] - Simple, agent-less, remote server monitoring tool that works over plain SSH. Written in Go, it does not need any software to be installed on the server that you want to monitor. It works by establishing an SSH session, and running commands on the remote server to collect system metrics.

## 📁 network diagnostics
_... description of the subcategory ..._

* [trippy](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A network diagnostic tool.

## 📁 network info
_... description of the subcategory ..._

* [asn](nan) [❌ 🌐 🖥️CLI] - Server for the following services: ASN, RPKI validity, BGP stats, IPv4v6, Prefix, URL, ASPath, Organization, IP reputation, IP geolocation, IP fingerprinting, Network recon, lookup API server, Web traceroute server.

## 📁 network interface info
_... description of the subcategory ..._

* [nics](nan) [❌ ❌ 🖥️TUI] - Display information about Network Interface Cards (NICs); the same output is presented across platforms.

## 📁 network monitor
_... description of the subcategory ..._

* [gping](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Ping, but with a graph.
* [mtr](nan) [❌ ❌ 🖥️TUI] - mtr combines the functionality of the 'traceroute' and 'ping' programs in a single network diagnostic tool.
* [Termshark](https://termshark.io/) [❌ ❌ 🖥️TUI] - A terminal UI for tshark, inspired by Wireshark.

## 📁 network proxy
_... description of the subcategory ..._

* [zxc](https://hail-hydrant.github.io/zxc/) [❌ 🌐 🖥️CLI] - Terminal based intercepting proxy written in rust with tmux and vim as user interface.

## 📁 network scanner
_... description of the subcategory ..._

* [havn](nan) [❌ 🌐 🖥️CLI] - A fast configurable port scanner with reasonable defaults.
* [netscanner](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - All-in-one network scanning tool.

## 📁 network tools
_... description of the subcategory ..._

* [liboping](nan) [❌ 🌐 🖥️CLI] - Protocol independent ANSI-C ping library and command line utility.
* [tproxy](nan) [❌ 🌐 🖥️CLI] - A CLI tool to proxy and analyze TCP connections.

## 📁 network traffic viewer
_... description of the subcategory ..._

* [oryx](nan) [❌ ❌ 🖥️TUI] - TUI for sniffing network traffic using eBPF on Linux.

## 📁 oauth manager
_... description of the subcategory ..._

* [oama](nan) [❌ ❌ 🖥️CLI] - OAuth credential Manager.

## 📁 packet sender
_... description of the subcategory ..._

* [packemon](nan) [❌ ❌ 🖥️TUI] - TUI tool and Go library for sending packets of arbitrary input and monitoring packets on any network interfaces (default: eth0).

## 📁 parallel ssh tools
_... description of the subcategory ..._

* [PSSH](https://code.google.com/archive/p/parallel-ssh/) [❌ ❌ 🖥️CLI] - Parallelized versions of OpenSSH and related tools, such as pssh, pscp, prsync, pnuke, and pslurp. The project includes psshlib which can be used within custom applications.

## 📁 proxy tool
_... description of the subcategory ..._

* [gg](nan) [❌ 🌐 🖥️CLI] - A command-line tool for one-click proxy in your research and development without installing v2ray or anything else.

## 📁 reconnaissance
_... description of the subcategory ..._

* [recon](nan) [❌ ❌ 🖥️CLI] - Gather public info about network hosts.

## 📁 remote shells
_... description of the subcategory ..._

* [mosh](https://mosh.org/) [❌ 🌐 🖥️CLI] - Remote SSH client that achieve good responsiveness in presence of intermittent connectivity and roaming.

## 📁 remote terminal server
_... description of the subcategory ..._

* [tsshd](nan) [❌ 🌐 🖥️CLI] - The tsshd works like mosh-server, while the "tssh --udp" works like mosh. Supports ssh port forwarding, ssh agent forwarding and X11 forwarding.

## 📁 shell
_... description of the subcategory ..._

* [Kapow!](nan) [❌ ❌ 🖥️CLI] - Say we have a nice cozy shell command that solves our problem. Kapow! lets us easily turn that into an HTTP API.
* [xxh](nan) [❌ 🌐 🖥️CLI] - Bring your favorite shell wherever you go through the ssh.

## 📁 sip analyzer
_... description of the subcategory ..._

* [sngrep](nan) [❌ ❌ 🖥️TUI] - Ncurses SIP Messages flow viewer.

## 📁 smb tools
_... description of the subcategory ..._

* [SMBScan](nan) [❌ ❌ 🖥️CLI] - SMBScan is a tool to enumerate file shares on an internal network.

## 📁 socket monitor
_... description of the subcategory ..._

* [neoss](nan) [❌ ❌ 🖥️CLI] - User-friendly and detailed socket statistics with a Terminal UI.

## 📁 ssh file transfer client
_... description of the subcategory ..._

* [trzsz-ssh](nan) [❌ 🌐 🖥️CLI] - An ssh client designed as a drop-in replacement for the openssh client. It aims to provide complete compatibility with openssh, mirroring all its features, while also offering additional useful features. Such as login prompt, batch login, remember password, automated interaction, trzsz, zmodem(rz/sz), udp mode like mosh, etc.

## 📁 ssh manager
_... description of the subcategory ..._

* [ggh](nan) [❌ ❌ 🖥️CLI] - Recall your SSH sessions, also searching your SSH config file.
* [SSM](nan) [❌ ❌ 🖥️CLI] - A simple SSH manager.

## 📁 ssh tools
_... description of the subcategory ..._

* [ssh-menu](nan) [❌ ❌ 🖥️TUI] - A very simple terminal tool that renders an interactive menu with your ssh profiles listed.
* [sshed](nan) [❌ ❌ 🖥️CLI] - sshed is a ssh config editor and bookmarks manager.
* [sshto](nan) [❌ ❌ 🖥️CLI] - Small bash script to manage your ssh connections. It builds menu (via dialog) from your ~/.ssh/config. It can not only connect but also to run commands, copy files, tunnel ports.

## 📁 static server
_... description of the subcategory ..._

* [serve](nan) [❌ ❌ 🖥️CLI] - Serves a static site, single page application, or just a static file, and provides a neat interface for listing the directory's contents.

## 📁 subnetting tools
_... description of the subcategory ..._

* [ipcalc](http://jodies.de/ipcalc) [❌ ❌ 🖥️CLI] - Takes an IP address and netmask and calculates the resulting broadcast, network, Cisco wildcard mask, and host range.

## 📁 system information
_... description of the subcategory ..._

* [wavemon](nan) [❌ ❌ 🖥️TUI] - wavemon is an ncurses-based monitoring application for wireless network devices on Linux.

## 📁 tcp client
_... description of the subcategory ..._

* [turl](nan) [❌ ❌ 🖥️CLI] - tURL is a command-line tool to make plain TCP-based requests.

## 📁 terminal API client
_... description of the subcategory ..._

* [ATAC](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Arguably a Terminal API Client. It is based on well-known clients such as Postman, Insomnia, or even Bruno, but inside your terminal without any specific graphical environment needed; free, account-less, and offline for now and forever.

## 📁 terminal sharing
_... description of the subcategory ..._

* [sshs](nan) [❌ ❌ 🖥️TUI] - Terminal user interface for SSH.
* [sshx](nan) [❌ 🌐 🖥️CLI] - Fast, collaborative live terminal sharing over the web.
* [termishare](nan) [❌ 🌐 🖥️CLI] - Peer to peer terminal sharing.
* [TStream](nan) [❌ ❌ 🖥️CLI] - Live streaming from the terminal. Requires the connection to a central server, from which the streaming is dispatched.
* [ttyd](nan) [❌ 🌐 🖥️CLI] - Share your terminal over the web.

## 📁 tunnelCLI / port forwarder
_... description of the subcategory ..._

* [bore](nan) [❌ 🌐 🖥️CLI] - A simple CLI tool for making tunnels to localhost.

## 📁 tunneling
_... description of the subcategory ..._

* [Tunnelmole](nan) [❌ 🌐 🖥️CLI] - Connect to local servers from anywhere.

## 📁 vpn
_... description of the subcategory ..._

* [sshuttle](nan) [❌ ❌ 🖥️CLI] - Transparent proxy server that works as a poor man's VPN. Forwards over ssh. Doesn't require admin. Works with Linux and macOS. Supports DNS tunneling.

## 📁 vpn tools
_... description of the subcategory ..._

* [tunblkctl](nan) [❌ ❌ 🖥️CLI] - Command-line frontend for Tunnelblick.
* [xiringuito](nan) [❌ 🌐 🖥️CLI] - VPN made easy! No configuration. No VPN servers. No hassle. Using SSH capabilities.

## 📁 web server
_... description of the subcategory ..._

* [darkhttpd](https://unix4lyfe.org/darkhttpd/) [❌ 🌐 🖥️CLI] - Darkhttpd is a simple, fast HTTP 1.1 web server for static content. It does not support PHP or CGI etc but is designed to serve static content, which it does very well.
* [quark](https://tools.suckless.org/quark/) [❌ 🌐 🖥️CLI] - quark is an extremely small and simple HTTP GET/HEAD-only web server for static content.

## 📁 web tools
_... description of the subcategory ..._

* [ttfb](nan) [❌ 🌐 🖥️CLI] - ttfb is a CLI-Tool to measure the TTFB (time to first byte) of HTTP requests.

## 📁 websocket
_... description of the subcategory ..._

* [websocat](nan) [❌ 🌐 🖥️CLI] - Netcat, curl and socat for WebSockets.

## 📁 wifi manager
_... description of the subcategory ..._

* [impala](nan) [❌ ❌ 🖥️TUI] - TUI for managing wifi networks and connections on Linux.

## 📁 xmpp server
_... description of the subcategory ..._

* [ejabberd](https://www.ejabberd.im/) [❌ ❌ 🖥️CLI] - ejabberd is an XMPP application server and an MQTT broker, written mainly in the Erlang programming language.
* [Prosody](https://prosody.im/) [❌ ❌ 🖥️CLI] - Prosody is a modern XMPP communication server. It aims to be easy to set up and configure, and efficient with system resources.

# note-taking
[Back to TOC](#📚-contents)

Tools to take, organize and manage notes
## 📁 CLIJournal
_... description of the subcategory ..._

* [dn](nan) [❌ ❌ 🖥️CLI] - Daily notes command line tool.

## 📁 EvernoteClientCLI
_... description of the subcategory ..._

* [Geeknote](nan) [❌ ❌ 🖥️CLI] - A command line client for Evernote that can be use on Linux, FreeBSD and OS X.

## 📁 NoteTakingCLI
_... description of the subcategory ..._

* [cadmus](nan) [❌ ❌ 🖥️CLI] - Shell Scripts to Facilitate Effective Note Taking.
* [jot](nan) [❌ ❌ 🖥️CLI] - Jot is a feature-stripped version of Obsidian focused on rapid note management through the terminal. It uses the same format of storage as Obsidian.
* [posce](nan) [❌ ❌ 🖥️CLI] - A note-taking toolkit for your command line.

## 📁 NoteTakingTUI
_... description of the subcategory ..._

* [Terminal velocity](https://vhp.github.io/terminal_velocity/) [❌ ❌ 🖥️TUI] - A fast, cross-platform note-taking application for the UNIX terminal.

## 📁 NotesCLI
_... description of the subcategory ..._

* [Noted](nan) [❌ ❌ 🖥️CLI] - Notes library, with viewer and shortcuts to add, delete and edit notes.

## 📁 TerminalKnowledgeBase
_... description of the subcategory ..._

* [Clipboard](https://getclipboard.app/) [❌ ❌ 🖥️CLI] - An easy-to-use information management tool that acts like an external brain.

## 📁 calendar & notes
_... description of the subcategory ..._

* [lazyorg](nan) [❌ ❌ 🖥️TUI] - Simple terminal-based calendar and note-taking app.

## 📁 cli kanban notes
_... description of the subcategory ..._

* [tb.go](nan) [❌ ❌ 🖥️TUI] - Tasks, boards & notes for the command-line habitat.

## 📁 command-line translator
_... description of the subcategory ..._

* [sncli](nan) [❌ 🌐 🖥️CLI] - A Python application that gives you access to your Simplenote account via the command line.

## 📁 journal
_... description of the subcategory ..._

* [jrnl](nan) [❌ ❌ 🖥️CLI] - jrnl is a simple journal application for the command line to easily create, search, and view journal entries; journals are stored as human-readable plain text, and can also be encrypted using AES encryption.
* [TUI-Journal](nan) [❌ ❌ 🖥️TUI] - Terminal-based application written in Rust that allows you to write and manage your journal/notes with a nice user interface.

## 📁 knowledge base
_... description of the subcategory ..._

* [kb](nan) [❌ ❌ 🖥️CLI] - A minimalist knowledge base manager.
* [nb](nan) [❌ 🌐 🖥️CLI] - A command line and local web note-taking, bookmarking, archiving, and knowledge base application.
* [rucola](nan) [❌ ❌ 🖥️TUI] - Terminal-based markdown note manager.
* [Standard Unix Notes](nan) [❌ ❌ 🖥️CLI] - GPG Encrypted Notes/Notebook manager for BSD/Linux.

## 📁 markdown viewer
_... description of the subcategory ..._

* [meudeus](nan) [❌ ❌ 🖥️TUI] - A skim-based `*.md` explore and surf tool.

## 📁 note taking
_... description of the subcategory ..._

* [mn](nan) [❌ ❌ 🖥️CLI] - A dead simple note-taking script.
* [tdo](nan) [❌ ❌ 🖥️CLI] - Fast and Simple Note Taking.

## 📁 note-taking
_... description of the subcategory ..._

* [FuzPad](nan) [🤖 ❌ 🖥️TUI] - A minimalistic note management solution, powered by fzf.
* [idea](nan) [❌ ❌ 🖥️CLI] - A lightweight tool for keeping ideas in a safe place quick and easy.
* [note](nan) [❌ ❌ 🖥️TUI] - A modern terminal-based note-taking application built with Bubble Tea and Lip Gloss to organize your thoughts with style.
* [note](nan) [❌ ❌ 🖥️TUI] - Minimalistic note taking.
* [zk](nan) [❌ ❌ 🖥️CLI] - zk is a command-line tool helping you to maintain a plain text Zettelkasten or personal wiki.

## 📁 terminal journal
_... description of the subcategory ..._

* [journalC](nan) [❌ ❌ 🖥️TUI] - A simple encrypted terminal journaling book.

## 📁 terminal notes
_... description of the subcategory ..._

* [NoteSH](nan) [❌ ❌ 🖥️TUI] - Sticky notes App in the Terminal, built with Textual, an amazing TUI framework!

## 📁 terminal sharing
_... description of the subcategory ..._

* [dnote](nan) [❌ 🌐 🖥️CLI] - A simple command line notebook for the terminal. It also offers a seamless multi-device sync and a web interface.
* [eureka](nan) [❌ ❌ 🖥️CLI] - Store your ideas without leaving the terminal.

# office
[Back to TOC](#📚-contents)

Programs to manage spreadsheets and to make presentations
## 📁 MarkdownPresenterTUI
_... description of the subcategory ..._

* [mdp](nan) [❌ ❌ 🖥️TUI] - A command-line based Markdown presentation tool.

## 📁 PlaintextPresenterCLI
_... description of the subcategory ..._

* [sent](https://tools.suckless.org/sent/) [❌ ❌ 🖥️CLI] - Simple plain-text presentation tool.

## 📁 TerminalPresentation
_... description of the subcategory ..._

* [Slides](nan) [❌ ❌ 🖥️TUI] - Terminal based presentation tool.

## 📁 calculator
_... description of the subcategory ..._

* [gpa-calculator](nan) [❌ ❌ 🖥️CLI] - GPA calculator CLI app that stores data in local files; written in Go.

## 📁 cli presentation
_... description of the subcategory ..._

* [presenterm](nan) [❌ ❌ 🖥️TUI] - A terminal slideshow tool.

## 📁 code tutorial
_... description of the subcategory ..._

* [tuitorial](nan) [❌ ❌ 🖥️TUI] - Create beautiful terminal-based code tutorials with syntax highlighting and interactive navigation.

## 📁 enhanced cat
_... description of the subcategory ..._

* [Lotus 1-2-3 for Linux](nan) [❌ ❌ 🖥️TUI] - A native port of Lotus 1-2-3 Release 3 to Linux.

## 📁 form sharing
_... description of the subcategory ..._

* [bashform](nan) [❌ 🌐 🖥️TUI] - Create and share forms in the terminal over SSH.

## 📁 markdown slides
_... description of the subcategory ..._

* [Slideck](nan) [❌ ❌ 🖥️TUI] - Present Markdown-powered slide decks in the terminal.

## 📁 pdf tools
_... description of the subcategory ..._

* [PDFtk](https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/) [❌ ❌ 🖥️CLI] - PDFtk is a simple tool for doing everyday things with PDF documents.
* [qpdf](nan) [❌ ❌ 🖥️CLI] - QPDF: A content-preserving PDF document transformer that allows performing several types of operations on PDF files, such as splitting, merging, etc.

## 📁 presentation tool
_... description of the subcategory ..._

* [tui-slides](nan) [❌ ❌ 🖥️TUI] - TerminalpPresentation program with modern TUI.

## 📁 presentation tools
_... description of the subcategory ..._

* [DeckTape](nan) [❌ ❌ 🖥️CLI] - DeckTape is a high-quality PDF exporter for HTML presentation frameworks.
* [pysentation](nan) [❌ ❌ 🖥️CLI] - pysentation is a CLI for displaying Python presentations.

## 📁 presentations
_... description of the subcategory ..._

* [patat](nan) [❌ ❌ 🖥️TUI] - Terminal-based presentations using Pandoc.

## 📁 search tool
_... description of the subcategory ..._

* [ggl](nan) [❌ 🌐 🖥️TUI] - Search the web (google, youtube, gmail, wiki, github, stackoverflow), prompt to send emails, prompt chatGPT, Gemini right from the terminal (command line).

## 📁 spreadsheet calculator
_... description of the subcategory ..._

* [sc-im](nan) [❌ ❌ 🖥️CLI] - (Spreadsheet Calculator Improvised) - an `ncurses` spreadsheet program for terminal. It is rich in functionalities, but the syntax of functions and other details are different from the common spreadsheets such as Excel and Calc, making difficult to "re-cycle" existing knowledge on these programs to work proficiently with sc-im. Nevertheless, a nice piece of software."

## 📁 terminal presentation
_... description of the subcategory ..._

* [tpp](http://www.ngolde.de/tpp.html) [❌ ❌ 🖥️TUI] - (text presentation program) - a ncurses Ruby program that allows producing nice text-based presentation with simple markup language.

## 📁 terminal spreadsheet
_... description of the subcategory ..._

* [Teapot](https://www.syntax-k.de/projekte/teapot/) [❌ ❌ 🖥️TUI] - Compact ncurses-based spreadsheet with original syntax, 3D-style and built-in functions.

# online
[Back to TOC](#📚-contents)

Tools that interact with online resources to provide their services, e.g., searches, wiki, etc.
## 📁 ArchWikiCLI
_... description of the subcategory ..._

* [arch-wiki](nan) [❌ 🌐 🖥️CLI] - Search the Arch Wiki anywhere from the command line.

## 📁 CLICatalog
_... description of the subcategory ..._

* [Awesome CLI](nan) [❌ ❌ 🖥️CLI] - Awesome CLI is a simple command line tool to give you a fancy command line interface to dive into Awesome lists.

## 📁 GoogleSearchCLI
_... description of the subcategory ..._

* [googler](nan) [❌ 🌐 🖥️CLI] - Google Search, Google Site Search, Google News from the terminal.

## 📁 StackOverflowCLI
_... description of the subcategory ..._

* [so](nan) [❌ 🌐 🖥️CLI] - Terminal interface for Stack Overflow.

## 📁 StackOverflowSearchCLI
_... description of the subcategory ..._

* [socli](nan) [❌ 🌐 🖥️CLI] - Stack overflow command line client written in Python. Search and browse stack overflow without leaving the terminal

## 📁 WikipediaCLI
_... description of the subcategory ..._

* [wikit](nan) [❌ 🌐 🖥️CLI] - A command line program for getting Wikipedia summaries easily.

## 📁 awesome list tools
_... description of the subcategory ..._

* [Awesome Finder](nan) [❌ ❌ 🖥️CLI] - Search the awesome lists from the command line.

## 📁 command-line translator
_... description of the subcategory ..._

* [ddgr](nan) [❌ 🌐 🖥️CLI] - A command line utility to search DuckDuckGo (HTML version) from the terminal.

## 📁 fuzzy finder
_... description of the subcategory ..._

* [magic-tape](nan) [❌ ❌ 🖥️CLI] - Magic-tape is an image supporting fuzzy finder command line interface YouTube client.

## 📁 git tool
_... description of the subcategory ..._

* [av](nan) [❌ ❌ 🖥️CLI] - A command line tool to manage stacked PRs with Aviator.

## 📁 github tools
_... description of the subcategory ..._

* [ghfetch](nan) [❌ 🌐 🖥️CLI] - ghfetch is a CLI tool to fetch GitHub user information and show like Neofetch.

## 📁 hackernews tracker
_... description of the subcategory ..._

* [dawson](nan) [❌ 🌐 🖥️CLI] - Track your project's statistics on Hacker News and Github, and get notified on every new interaction.

## 📁 jira tools
_... description of the subcategory ..._

* [Fjira](nan) [❌ 🌐 🖥️CLI] - The fuzziest Jira command line tool in the world.
* [jira-cli](nan) [❌ 🌐 🖥️CLI] - Feature-rich interactive Jira command line.

## 📁 output sharing tools
_... description of the subcategory ..._

* [Seashells](https://seashells.io/) [❌ 🌐 🖥️CLI] - Pipe output to the web.

## 📁 read-later tools
_... description of the subcategory ..._

* [pockyt](nan) [❌ 🌐 🖥️TUI] - Read, manage, and automate the collection of articles in [Pocket](https://getpocket.com), an application for managing a reading list of articles from the Internet.

## 📁 recipe tools
_... description of the subcategory ..._

* [pure-recipe](nan) [❌ 🌐 🖥️CLI] - Input a recipe URL and receive well-formatted, ad-free recipes to your terminal, or save the output to a Markdown file.

## 📁 reddit cleaner
_... description of the subcategory ..._

* [Shreddit](nan) [❌ 🌐 🖥️CLI] - Remove your comment history on Reddit as deleting an account does not do so.

## 📁 subdomain finder
_... description of the subcategory ..._

* [subs](nan) [❌ 🌐 🖥️CLI] - Grab valid subdomains, resolve them, split them and more.

## 📁 terminal messaging
_... description of the subcategory ..._

* [chuckle-cli](nan) [❌ 🌐 🖥️CLI] - An application that utilises an API in order to print out jokes in your terminal.

## 📁 terminal sharing
_... description of the subcategory ..._

* [tuir](nan) [❌ 🌐 🖥️TUI] - Browse Reddit from your terminal.

## 📁 username/email availability checker
_... description of the subcategory ..._

* [socialscan](nan) [❌ 🌐 🖥️CLI] - Python library and CLI for accurately querying username and email usage on online platforms.

## 📁 vcs performance
_... description of the subcategory ..._

* [is-fast](nan) [❌ 🌐 🖥️TUI] - A TUI tool designed for quick and efficient internet searches directly from the terminal, ideal for environments where you don't have easy access to a browser.

## 📁 web scraper
_... description of the subcategory ..._

* [par_scrape](nan) [❌ 🌐 🖥️CLI] - PAR Scrape is a versatile web scraping tool with options for Selenium or Playwright, featuring AI-powered data extraction and formatting.

## 📁 wikipedia client
_... description of the subcategory ..._

* [wiki-tui](nan) [❌ 🌐 🖥️TUI] - A simple and easy to use Wikipedia Text User Interface.
* [Wikipedia-Command-Line-Interface](nan) [❌ 🌐 🖥️CLI] - Use wikipedia in your command prompt.

# option-picker
[Back to TOC](#📚-contents)

Fuzzy finders and generic option pickers in lists of strings
## 📁 TerminalMenu
_... description of the subcategory ..._

* [pmenu](nan) [❌ ❌ 🖥️TUI] - A dynamic terminal-based menu inspired by dmenu.

## 📁 date picker
_... description of the subcategory ..._

* [tui-datepicker](nan) [❌ ❌ 🖥️TUI] - Select date in terminal with vim-motions and copy to buffer.

## 📁 enhanced cat
_... description of the subcategory ..._

* [fzy](nan) [❌ ❌ 🖥️CLI] - Better fuzzy finder.
* [skim](nan) [❌ ❌ 🖥️TUI] - Fuzzy Finder in rust.

## 📁 file search
_... description of the subcategory ..._

* [fss](nan) [❌ ❌ 🖥️CLI] - User-friendly command-line search scripts combining find and grep utilities with fzf previewing and direct actions on specific file types.

## 📁 fuzzy finder
_... description of the subcategory ..._

* [television](nan) [❌ ❌ 🖥️TUI] - Blazing fast general purpose fuzzy finder TUI.

## 📁 fuzzy selector
_... description of the subcategory ..._

* [smenu](nan) [❌ ❌ 🖥️TUI] - Started as a lightweight and flexible terminal menu generator, it evolved into a powerful and versatile CLI selection tool for interactive or scripting use.

## 📁 fuzzy-filter
_... description of the subcategory ..._

* [percol](nan) [❌ ❌ 🖥️TUI] - A Python script that "1) receives input lines from `stdin` or a file, 2) lists the input lines and waits for input that filter/select the line(s), 3) outputs the selected line(s) to `stdout`"; can be used to add interactivity to many regular shell commands.

## 📁 fuzzy‑search
_... description of the subcategory ..._

* [fzf](nan) [❌ ❌ 🖥️TUI] - (FuZzy Finder) - a general-purpose command-line finder with fuzzy search/filter capabilities, good integration with `vim`.

## 📁 fzf selector
_... description of the subcategory ..._

* [tp](nan) [❌ ❌ 🖥️TUI] - Display the result of the commands at every keystroke.

## 📁 interactive selector
_... description of the subcategory ..._

* [choose](nan) [❌ ❌ 🖥️TUI] - NCurses based token selector with a nice terminal user interface for selecting tokens. Selecting a line from the bash history is only one of its use cases.

## 📁 interactive-line-select
_... description of the subcategory ..._

* [pick](nan) [❌ ❌ 🖥️TUI] - Choose one option from a set of choices using an interface with fuzzy search functionality.

## 📁 menu
_... description of the subcategory ..._

* [lSel](nan) [❌ ❌ 🖥️TUI] - Simple no-fuss TUI selection menu for use in scripts.

## 📁 menu builder
_... description of the subcategory ..._

* [shmenu](nan) [❌ ❌ 🖥️TUI] - Menu TUI tool written solely in bash.

## 📁 menu tools
_... description of the subcategory ..._

* [cmenu](nan) [❌ ❌ 🖥️TUI] - Vaguely dmenu-like minimal TUI menu utility, it reads entries from stdin, creates a selection menu, and writes the selected entry to stdout.

## 📁 shell
_... description of the subcategory ..._

* [fuzzysh](nan) [❌ ❌ 🖥️CLI] - Minimalist selector in shell, inspired by fzf.
* [luneta](nan) [❌ ❌ 🖥️CLI] - Interactive filter that can be easily composed within any script.

# organizers
[Back to TOC](#📚-contents)

Calendar and appointment managers
## 📁 EmailSenderCLI
_... description of the subcategory ..._

* [remint](https://sr.ht/~mlaparie/remint/) [❌ ❌ 🖥️CLI] - A simple terminal UI wrapper for D. Skoll's Remind calendar program

## 📁 GoogleContactsCLI
_... description of the subcategory ..._

* [goobook](nan) [❌ 🌐 🖥️CLI] - The purpose of GooBook is to make it possible to use your Google Contacts from the command-line and from MUAs such as Mutt. It can be used from Mutt the same way as abook.

## 📁 TerminalCalendarTasker
_... description of the subcategory ..._

* [calcurse](https://calcurse.org/) [❌ ❌ 🖥️TUI] - A calendar and scheduling application for the command line. It helps keep track of events, appointments and everyday tasks.

## 📁 TimezoneCLI
_... description of the subcategory ..._

* [tz](nan) [❌ ❌ 🖥️CLI] - tz helps you schedule things across time zones. It's an interactive TUI program that displays time across the time zones of your choosing.

## 📁 caldav calendar
_... description of the subcategory ..._

* [caldr](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A lightweight CLI / TUI calendar that supports CalDAV.
* [khal](nan) [❌ 🌐 🖥️TUI] - Calendar that can synchronize with CalDAV servers through [vdirsyncer](https://github.com/pimutils/vdirsyncer).

## 📁 calendar
_... description of the subcategory ..._

* [Calcure](nan) [❌ ❌ 🖥️TUI] - Modern TUI calendar and task manager with customizable interface.
* [plann](nan) [❌ 🌐 🖥️CLI] - Command-line interface to online calendars.

## 📁 calendar sync tools
_... description of the subcategory ..._

* [vdirsyncer](nan) [❌ 🌐 🖥️CLI] - CalDAV synchronization program.

## 📁 calendar tools
_... description of the subcategory ..._

* [avail](nan) [❌ ❌ 🖥️CLI] - Find available times between all your calendars.
* [icsp](nan) [❌ ❌ 🖥️CLI] - Command-line iCalendar (.ics) to CSV utility.

## 📁 contact manager
_... description of the subcategory ..._

* [pbook](nan) [❌ ❌ 🖥️TUI] - A simple phonebook manager for TUI lovers.

## 📁 google calendar client
_... description of the subcategory ..._

* [gcalcli](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - Access Google Calendars; supports the main tasks: create, delete, and list events.

## 📁 knowledge base
_... description of the subcategory ..._

* [buku](nan) [❌ ❌ 🖥️CLI] - A powerful bookmark manager written in Python3 and SQLite3.

## 📁 remind frontend
_... description of the subcategory ..._

* [Wyrd](http://freecode.com/projects/wyrd/) [❌ ❌ 🖥️TUI] - Curses front-end for [Remind](https://www.roaringpenguin.com/products/remind) written in OCaml with vertically scrollable time-table.

## 📁 reminders
_... description of the subcategory ..._

* [peroutine](nan) [❌ ❌ 🖥️CLI] - Remind you of periodical events. The period can be any positive integer of days, so work around the fact that the number of days in a week is prime.

## 📁 rule-based calendar
_... description of the subcategory ..._

* [Remind](https://dianne.skoll.ca/projects/remind/) [❌ ❌ 🖥️CLI] - Calendar that supports complex rules to define events and used a custom, powerful text-based storage format.

## 📁 scheduler
_... description of the subcategory ..._

* [Girok](nan) [❌ ❌ 🖥️TUI] - A powerful and beautiful CLI scheduler.

## 📁 text calendar
_... description of the subcategory ..._

* [pal](http://palcal.sourceforge.net/) [❌ ❌ 🖥️CLI] - Calendar for Unix/Linux systems that can keep track of events; custom, plain text storage format; interesting and fully functional.

## 📁 vcard address book
_... description of the subcategory ..._

* [addrb](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A lightweight CLI / TUI address book that supports CardDAV.
* [khard](nan) [❌ 🌐 🖥️CLI] - vCard address book written in Python. Supports CardDAV.
* [ppl addressbook](http://ppladdressbook.org/) [❌ ❌ 🖥️CLI] - Address book tool that uses the vCard format. Built on top of Ruby and Git

# package-manager
[Back to TOC](#📚-contents)

Package managers to manage/install/uninstall software packages, as source code or binaries
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [getghrel](nan) [❌ 🌐 🖥️CLI] - A user-friendly command-line tool that fetches and installs the latest release assets from GitHub for macOS and Linux; it automatically detects your operating system and architecture, downloads the relevant binary, and unpacks it, ensuring a hassle-free experience.

## 📁 GitforLargeFiles
_... description of the subcategory ..._

* [bin](nan) [❌ ❌ 🖥️CLI] - Manages binary files downloaded from different sources.

## 📁 PackageManagerCLI
_... description of the subcategory ..._

* [nala](nan) [❌ 🌐 🖥️CLI] - apt package manager front-end with cleaner interface.

## 📁 PyPiSearcherCLI
_... description of the subcategory ..._

* [pypi-command-line](nan) [❌ 🌐 🖥️CLI] - A powerful, colorful, beautiful command-line-interface for pypi.org.

## 📁 Translation
_... description of the subcategory ..._

* [pmt](nan) [❌ ❌ 🖥️CLI] - Translator of package names between different package managers of Linux distributions.

## 📁 binary installer
_... description of the subcategory ..._

* [eget](nan) [❌ 🌐 🖥️CLI] - Easily install prebuilt binaries from GitHub.

## 📁 dev env manager
_... description of the subcategory ..._

* [mise](https://mise.jdx.dev/) [❌ ❌ 🖥️CLI] - A development environment setup tool: dev tools, env vars, and task runner. Like `asdf` + `direnv` + `make`.

## 📁 knowledge base
_... description of the subcategory ..._

* [stew](nan) [❌ 🌐 🖥️CLI] - An independent package manager for compiled binaries.

## 📁 kubectl plugin manager
_... description of the subcategory ..._

* [krew](https://krew.sigs.k8s.io/) [❌ ❌ 🖥️CLI] - Find and install kubectl plugins.

## 📁 package manager
_... description of the subcategory ..._

* [app](nan) [❌ ❌ 🖥️CLI] - A cross-platform package management assistant with super powers.
* [aptitude](nan) [❌ ❌ 🖥️TUI] - A TUI front-end to APT, the Debian package manager.
* [flatpak-cli](nan) [❌ ❌ 🖥️CLI] - A command line program to search and install flatpaks from the flathub repository using a fzf like interface.
* [hysp](nan) [❌ ❌ 🖥️CLI] - An independent package manager that every hacker deserves.
* [JAPM](nan) [❌ ❌ 🖥️TUI] - A package manager that uses curses to provide a friendly UI
* [upt](nan) [❌ 🌐 🖥️CLI] - Universal Package-management Tool for any OS.

## 📁 package manager frontend
_... description of the subcategory ..._

* [pm-jesus](nan) [❌ ❌ 🖥️TUI] - Package manager front-end.

## 📁 runtime managers
_... description of the subcategory ..._

* [asdf](https://asdf-vm.com/) [❌ ❌ 🖥️CLI] - Manage multiple runtime versions with a single CLI tool.

## 📁 shell
_... description of the subcategory ..._

* [Shell Bling Ubuntu](nan) [❌ ❌ 🖥️CLI] - A few scripts to be run on a fresh-off-the-presses Ubuntu VM, in order to get its shell nice 'n purdy.

## 📁 system info
_... description of the subcategory ..._

* [cli-tools-info](nan) [❌ ❌ 🖥️CLI] - An overview of your CLI tools, if they are installed and what version they are on.

## 📁 system updater
_... description of the subcategory ..._

* [topgrade](nan) [❌ 🌐 🖥️CLI] - Upgrade all the things.

# password-manager
[Back to TOC](#📚-contents)

Programs to store and manage collections of passwords and other login/authentication information
## 📁 EncryptedPasswordManager
_... description of the subcategory ..._

* [gopass](https://www.gopass.pw/) [❌ ❌ 🖥️CLI] - gopass is a rewrite of the pass password manager in Go with the aim of making it cross-platform and adding additional features. The target audience are professional developers and sysadmins (and especially teams of those) who are well versed with a command line interface.
* [hide](nan) [❌ ❌ 🖥️CLI] - AES-256 bit encrypted password manager with all encrypted passwords stored locally on your machine
* [kpcli](http://kpcli.sourceforge.net/) [❌ ❌ 🖥️CLI] - A command line interface for KeePass databases.
* [password-store](https://www.passwordstore.org/) [❌ ❌ 🖥️CLI] - With pass, each password lives inside a GPG encrypted file whose filename is the title of the website or resource that requires the password. These encrypted files may be organized into meaningful folder hierarchies, copied from computer to computer, and, in general, manipulated using standard command line file management utilities.
* [SpicyPass](nan) [❌ ❌ 🖥️CLI] - A light-weight password manager with a focus on simplicity and security.

## 📁 PasswordGeneratorCLI
_... description of the subcategory ..._

* [dpg](nan) [❌ ❌ 🖥️CLI] - The Deterministic Password Generator - Generates passwords based on a master password and the indication of the website/service/username, without the need of storing anything.

## 📁 PasswordManagerCLI
_... description of the subcategory ..._

* [Bitwarden CLI](https://bitwarden.com/help/cli/) [❌ 🌐 🖥️CLI] - Command-line interface for Bitwarden, a multi-platform password manager targeted to companies and enterprises.

## 📁 PasswordWrapperCLI
_... description of the subcategory ..._

* [passfzf](nan) [❌ ❌ 🖥️CLI] - A simple fzf wrapper for pass (the UNIX password-store). It allows fuzzy finding your pass passwords to copy, show, edit, delete, rename and duplicate them.

## 📁 bitwarden cli
_... description of the subcategory ..._

* [rbw](nan) [❌ 🌐 🖥️CLI] - Unofficial command line client for Bitwarden that is “stateful”, i.e., it does not require the manual lock and unlock of the client.

## 📁 enhanced cat
_... description of the subcategory ..._

* [cpass](nan) [❌ ❌ 🖥️TUI] - Another console UI for pass.

## 📁 password generator
_... description of the subcategory ..._

* [generate-pw](https://generatepw.org) [❌ ❌ 🖥️CLI] - Randomly generate cryptographically-secure passwords.

## 📁 password manager
_... description of the subcategory ..._

* [keydex](nan) [❌ ❌ 🖥️CLI] - Manage KeePass databases from your terminal.
* [kpxhs](nan) [❌ ❌ 🖥️TUI] - Interactive KeePass database TUI viewer written in Haskell.
* [pa](nan) [❌ ❌ 🖥️CLI] - A simple password manager; encryption via age, written in portable POSIX shell.
* [pash](nan) [❌ ❌ 🖥️CLI] - A simple password manager using GPG written in POSIX sh.
* [pass](nan) [❌ ❌ 🖥️CLI] - POSIX password manager that keeps passwords inside GPG encrypted files inside a simple directory tree.
* [passage](nan) [❌ ❌ 🖥️CLI] - A fork of [password-store](https://www.passwordstore.org) that uses [age](https://age-encryption.org) as a backend instead of GnuPG.
* [titan](https://www.byteptr.com/titan/) [❌ ❌ 🖥️CLI] - Password management belongs to the command line, deep into the Unix heartland, the shell. Titan is written in C and is available under the MIT license.
* [tresor](nan) [❌ ❌ 🖥️TUI] - A KeePass TUI written in Go using Bubble Tea.

## 📁 secrets manager
_... description of the subcategory ..._

* [teller](nan) [❌ 🌐 🖥️CLI] - Cloud native secrets management for developers - never leave your command line for secrets.

## 📁 secure archive manager
_... description of the subcategory ..._

* [safe.sh](nan) [❌ ❌ 🖥️CLI] - Pure Bash script to manage secure archives; simple and clean; uses [gnugpg](https://gnupg.org/) for encryption/decryption, thus can leverage tools like [GPG Agent](https://www.gnupg.org/documentation/manuals/gnupg/Invoking-GPG_002dAGENT.html).

# pastebin
[Back to TOC](#📚-contents)

Services that allows online sharing of text and other content
## 📁 PastebinCLI
_... description of the subcategory ..._

* [GoCatGo](nan) [❌ 🌐 🖥️CLI] - GoCatGo is another pastebin tool with a super focus on transparency.

## 📁 pastebin
_... description of the subcategory ..._

* [paste69](nan) [❌ 🌐 🖥️CLI] - Simple CURL-able pastebin.

## 📁 terminal sharing
_... description of the subcategory ..._

* [feuille](nan) [❌ 🌐 🖥️CLI] - A fast, dead-simple socket-based pastebin.

# productivity
[Back to TOC](#📚-contents)

Applications for improving own productivity that do not deserve (at the moment) a specific category; e.g., resume generators and mind maps
## 📁 DirectionsQueryCLI
_... description of the subcategory ..._

* [gdir](nan) [❌ 🌐 🖥️CLI] - A command line tool which queries Google Directions. The tool displays results as human-readable text.

## 📁 GoogleScraperCLI
_... description of the subcategory ..._

* [tuxi](nan) [❌ 🌐 🖥️CLI] - A CLI tool that scrapes Google search results and SERPs that provides instant and concise answers.

## 📁 Translation
_... description of the subcategory ..._

* [gtt](nan) [❌ 🌐 🖥️TUI] - Google Translate TUI (Originally), now supporting Apertium, Argos, Bing, ChatGPT, DeepL, DeepLX, Google, Reverso.

## 📁 VaccineCertViewerCLI
_... description of the subcategory ..._

* [ancv](nan) [❌ 🌐 🖥️CLI] - Renders your (JSON) resume/CV for online & pretty terminal display.

## 📁 mind‑mapping
_... description of the subcategory ..._

* [h-m-m](nan) [❌ ❌ 🖥️TUI] - h-m-m (pronounced like the interjection "hmm") is a simple, fast, keyboard-centric terminal-based tool for working with mind maps.

## 📁 notifications
_... description of the subcategory ..._

* [telert](https://github.com/navig-me/telert) [❌ 🌐 🖥️CLI] - Lightweight CLI and Python utility that sends alerts (Telegram, Slack, Teams, Desktop, Audio) when commands complete.

## 📁 speed reading
_... description of the subcategory ..._

* [speedread](nan) [❌ ❌ 🖥️TUI] - A simple terminal-based open source Spritz-alike filter that shows input text as a per-word RSVP (rapid serial visual presentation) aligned on optimal reading points.

## 📁 task manager
_... description of the subcategory ..._

* [classis](nan) [❌ ❌ 🖥️TUI] - An easy CLI for the terminal fans out there who want to access Open Assistant's API through the terminal or want to use the API in their own applications.

## 📁 terminal dashboard
_... description of the subcategory ..._

* [wtf](nan) [❌ ❌ 🖥️TUI] - The personal information dashboard for your terminal, including todos, calendar, JIRA, etc.

## 📁 time tools
_... description of the subcategory ..._

* [zeitkatze](nan) [❌ ❌ 🖥️CLI] - Simplest stopwatch in a Linux console.

## 📁 tui utils
_... description of the subcategory ..._

* [TUI apps](nan) [❌ ❌ 🖥️TUI] - A repository containing a couple of one-script programs, mainly dedicated to training/learning CLI tools such as grep, awk, etc.

# programming
[Back to TOC](#📚-contents)

Tools for developers, including debuggers, testing, line counters, boilerplate and license generators, etc.
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [scons](nan) [❌ ❌ 🖥️CLI] - Software construction tool.

## 📁 BenchmarkingCLI
_... description of the subcategory ..._

* [temci](nan) [❌ ❌ 🖥️CLI] - Advanced benchmarking tool written in Python 3 that supports setting up an environment for benchmarking and the generation of visually appealing reports.

## 📁 CodeStatsCLI
_... description of the subcategory ..._

* [cloc](nan) [❌ ❌ 🖥️CLI] - Tool for counting blank lines, comment lines, and physical lines of source code in many programming languages.
* [scc](nan) [❌ ❌ 🖥️CLI] - Sloc Cloc and Code (scc) is a codebase statistics counter. Goal is to be the fastest code counter possible, but also perform COCOMO calculation like sloccount and to estimate code complexity similar to cyclomatic complexity calculators. In short one tool to rule them all.
* [Tokei](nan) [❌ ❌ 🖥️CLI] - Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language.

## 📁 DeterministicDebugger
_... description of the subcategory ..._

* [rr](https://rr-project.org/) [❌ ❌ 🖥️CLI] - Debug the recording, deterministically, as many times as you want.

## 📁 DevToolboxCLI
_... description of the subcategory ..._

* [Kool](nan) [❌ ❌ 🖥️CLI] - CLI tool that brings the complexities of modern software development making these environments lightweight, fast and reproducible.

## 📁 GDBEnhancerTUI
_... description of the subcategory ..._

* [gdb-dashboard](nan) [❌ ❌ 🖥️TUI] - Modular visual interface for GDB in Python.

## 📁 ImageViewer(ASCII)
_... description of the subcategory ..._

* [chars](nan) [❌ ❌ 🖥️CLI] - Display names and codes for various ASCII (and Unicode) characters / code points.

## 📁 LightweightTextViewer
_... description of the subcategory ..._

* [o](nan) [❌ ❌ 🖥️CLI] - Agentic Design Framework, automate with natural language, build agents in seconds, self-generate new features.

## 📁 OfflineDocsetSearcher
_... description of the subcategory ..._

* [dasht](http://sunaku.github.io/dasht/man/man0/README.html) [❌ ❌ 🖥️CLI] - Search in 200+ offline documentation sets API docs offline, in your terminal or browser.

## 📁 RegexRefactorTool
_... description of the subcategory ..._

* [fastmod](nan) [❌ ❌ 🖥️CLI] - A tool to assist you with large-scale codebase refactors, and it supports most of codemod's options. It is focused on improving the use case "I want to use interactive mode to make sure my regex is correct, and then I want to apply the regex everywhere".

## 📁 StaticAnalyzerCLI
_... description of the subcategory ..._

* [Cppcheck](http://cppcheck.net/) [❌ ❌ 🖥️CLI] - Static analysis tool for C/C++ code providing unique code analysis to detect bugs and focuses on detecting undefined behavior and dangerous coding constructs.
* [Frama-C](https://frama-c.com/) [❌ ❌ 🖥️CLI] - Open source extensible and collaborative platform dedicated to source-code analysis of C software. Frama-C can assist from the navigation through unfamiliar projects up to the certification of critical software.

## 📁 advanced grep
_... description of the subcategory ..._

* [grex](nan) [❌ ❌ 🖥️CLI] - A command-line tool for generating regular expressions from user-provided test cases.
* [pire](nan) [❌ ❌ 🖥️CLI] - Python Interactive Regular Expressions.

## 📁 api testing
_... description of the subcategory ..._

* [stepci](nan) [❌ ❌ 🖥️CLI] - Automated API Testing and Quality Assurance.

## 📁 argument parser
_... description of the subcategory ..._

* [argbash](nan) [❌ ❌ 🖥️CLI] - Bash argument parsing code generator.

## 📁 assembly visualizers
_... description of the subcategory ..._

* [cgasm](nan) [❌ ❌ 🖥️TUI] - Pronounced “SeekAzzem”, it is a standalone, offline terminal-based tool with no dependencies that gives me x86 assembly documentation.

## 📁 benchmark dashboard
_... description of the subcategory ..._

* [bencher](nan) [❌ ❌ 🖥️TUI] - Continuous benchmarking, Bencher allows you to track the performance of your code or binary over time and catch performance regressions before you release.

## 📁 build tool
_... description of the subcategory ..._

* [umake](nan) [❌ ❌ 🖥️CLI] - Makefile linter emphasizing portability, targeting the POSIX make standard.

## 📁 build tools
_... description of the subcategory ..._

* [fmake](nan) [❌ ❌ 🖥️CLI] - Brings `make`s interface to almost any build system.

## 📁 cli generator
_... description of the subcategory ..._

* [bashly](https://bashly.dannyb.co/) [❌ ❌ 🖥️CLI] - Bashly is a command line application (written in Ruby) that lets you generate feature-rich bash command line tools.

## 📁 code bundler
_... description of the subcategory ..._

* [codegrab](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Interactive CLI tool for selecting and bundling code into a single, LLM-ready output file.

## 📁 code runner
_... description of the subcategory ..._

* [lab](nan) [❌ ❌ 🖥️CLI] - Lab helps you experiment with code without friction. Type `lab` with any extension and start coding - it handles files, organization, and cleanup automatically.

## 📁 code submission
_... description of the subcategory ..._

* [CodeMark CLI](nan) [❌ ❌ 🖥️CLI] - Helps you manage coding assignments and tests; easily initialize the configuration, list assignments, fetch and check your code, submit your code for grading, and get AI-powered error recommendations.

## 📁 command-line translator
_... description of the subcategory ..._

* [hors](nan) [❌ 🌐 🖥️CLI] - Instant coding answers via the command line.
* [howdoi](nan) [🤖 🌐 🖥️CLI] - Instant coding answers via the command line.

## 📁 contributor helper
_... description of the subcategory ..._

* [mk](nan) [❌ ❌ 🖥️CLI] - mk is a CLI tool that aims to ease contribution to any open source project by hiding repository implementation details from the casual contributor.

## 📁 debug assistant
_... description of the subcategory ..._

* [ChatDBG](nan) [🤖 ❌ 🖥️CLI] - AI-assisted debugging. Uses AI to answer 'why'.

## 📁 debugging
_... description of the subcategory ..._

* [cgdb](nan) [❌ ❌ 🖥️TUI] - Console front-end to the GNU debugger.
* [termfu](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - A multi-language debugger frontend that allows users to create and switch between custom layouts.

## 📁 dev environment
_... description of the subcategory ..._

* [Flox](nan) [❌ ❌ 🖥️CLI] - Developer environments you can take with you.

## 📁 dev environment manager
_... description of the subcategory ..._

* [devbox](nan) [❌ 🌐 🖥️CLI] - Instant, easy, and predictable development environments.

## 📁 devops tools
_... description of the subcategory ..._

* [DEM](https://www.axemsolutions.io/dem_doc/index.html) [❌ ❌ 🖥️CLI] - Containerized Development Environment Manager for embedded development.

## 📁 enhanced cat
_... description of the subcategory ..._

* [dtool](nan) [❌ ❌ 🖥️CLI] - Collection of development tools.
* [pvcheck](nan) [❌ ❌ 🖥️CLI] - A tool to apply automated testing to programs that produce textual output. The format of the output is very specific, making pvcheck suitable to test programming quizzes.
* [todocheck](nan) [❌ ❌ 🖥️CLI] - Static code analyzer for annotated TODO comments.

## 📁 env manager
_... description of the subcategory ..._

* [dotenvhub](nan) [❌ ❌ 🖥️TUI] - Terminal App to centrally manage .env files. Written in Python powered by Textual.

## 📁 file renamer
_... description of the subcategory ..._

* [nsh](nan) [❌ ❌ 🖥️CLI] - A powerful renaming utility for developers, used to rename Symbols, Phrases in File contents, file names, directory names, recursively, useful specially when you find a better name for your app.

## 📁 go tools
_... description of the subcategory ..._

* [gup](nan) [❌ ❌ 🖥️CLI] - Update binaries installed by "go install" with goroutines.

## 📁 javascript minifier
_... description of the subcategory ..._

* [minify.js](https://minify-js.org) [❌ ❌ 🖥️CLI] - Recursively minify all JavaScript files.

## 📁 leetcode client
_... description of the subcategory ..._

* [Leetcode-go](nan) [❌ 🌐 🖥️CLI] - A simple CLI tool for searching, downloading and submitting problems to LeetCode.

## 📁 live reloader
_... description of the subcategory ..._

* [air](nan) [❌ ❌ 🖥️CLI] - Live reload for Go apps.

## 📁 npm tools
_... description of the subcategory ..._

* [np](nan) [❌ ❌ 🖥️CLI] - A better `npm publish`.

## 📁 release automation
_... description of the subcategory ..._

* [release-it](nan) [❌ ❌ 🖥️CLI] - Automate releases for Git repositories and/or Node.js packages.
* [semantic-release](nan) [❌ ❌ 🖥️CLI] - Automates the whole node.js package release workflow including: determining the next version number, generating the release notes, and publishing the package.

## 📁 scripting
_... description of the subcategory ..._

* [scriptisto](nan) [❌ ❌ 🖥️CLI] - A language-agnostic "shebang interpreter" that enables you to write scripts in compiled languages.

## 📁 shell builder
_... description of the subcategory ..._

* [mush](nan) [❌ ❌ 🖥️CLI] - Mush, a build system for shell.

## 📁 stack tools
_... description of the subcategory ..._

* [rebound](nan) [❌ 🌐 🖥️CLI] - Fetch Stack Overflow results in your terminal when you get an error. Supported languages: Python, Node.js, Ruby, Go, and Java.

## 📁 terminal sharing
_... description of the subcategory ..._

* [nbterm](nan) [❌ ❌ 🖥️TUI] - Jupyter Notebooks in the terminal.

## 📁 vcs tool
_... description of the subcategory ..._

* [llm-fuse](nan) [❌ ❌ 🖥️CLI] - A tool designed to quickly generate an aggregated text file, or multiple files when chunking is enabled, from numerous files within a repository that can then be pasted into a LLM prompt to provide context from multiple source files.

# programming-boilerplate
[Back to TOC](#📚-contents)

Utilities that generate licenses, documentation structure (README files), project directories and other boilerplate for software projects
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [kickstart](nan) [❌ ❌ 🖥️CLI] - Scaffolding tool to get new projects up and running quickly.
* [Proji](nan) [❌ ❌ 🖥️CLI] - Powerful cross-platform CLI project templating tool.

## 📁 changelog generators
_... description of the subcategory ..._

* [clog](nan) [❌ ❌ 🖥️CLI] - Creates a changelog automatically from local git metadata.

## 📁 contributing.md generator
_... description of the subcategory ..._

* [contributing-generator](nan) [❌ ❌ 🖥️TUI] - A generator for the CONTRIBUTING.md, README.md, LICENSE, etc.

## 📁 enhanced cat
_... description of the subcategory ..._

* [license-up](nan) [❌ ❌ 🖥️CLI] - Create a license quickly for a given name.

## 📁 git tools
_... description of the subcategory ..._

* [add-gitignore](nan) [❌ ❌ 🖥️CLI] - Interactively generate a .gitignore for software projects.

## 📁 license generators
_... description of the subcategory ..._

* [legit](nan) [❌ ❌ 🖥️CLI] - Automagically generates a LICENSE file for the current working directory that you are in or a license header for a file where applicable.
* [mklicense](nan) [❌ ❌ 🖥️CLI] - CLI tool for easily generating the text of the most common licenses.

## 📁 project boilerplate
_... description of the subcategory ..._

* [upnup](nan) [❌ ❌ 🖥️CLI] - A command line utility that generates a LICENSE file in the current working directory.

## 📁 project scaffolding 
_... description of the subcategory ..._

* [Cookiecutter](nan) [❌ ❌ 🖥️CLI] - A cross-platform command-line utility that creates projects from cookiecutters (project templates), e.g. Python package projects, C projects.

## 📁 readme generators
_... description of the subcategory ..._

* [readme-md-generator](nan) [❌ ❌ 🖥️CLI] - CLI that generates beautiful README.md files.

## 📁 template generators
_... description of the subcategory ..._

* [boilr](nan) [❌ ❌ 🖥️CLI] - Boilerplate template manager that generates files or directories from template repositories.

# prompt
[Back to TOC](#📚-contents)

Prompts and welcome messages at the command line
## 📁 ShellPromptEnhancer
_... description of the subcategory ..._

* [Starship](https://starship.rs/) [❌ ❌ 🖥️CLI] - The cross-shell prompt for astronauts.

## 📁 ShellPromptTheme
_... description of the subcategory ..._

* [Spaceship](https://spaceship-prompt.sh/) [❌ ❌ 🖥️CLI] - Minimalistic, powerful and extremely customizable Zsh prompt.

## 📁 TerminalStatusLineEnhancer
_... description of the subcategory ..._

* [powerline](nan) [❌ ❌ 🖥️CLI] - Powerline is a statusline plugin for vim, and provides statuslines and prompts for several other applications, including zsh, bash, tmux, IPython, Awesome and Qtile.

## 📁 WelcomeMessageCLI
_... description of the subcategory ..._

* [welcome.sh](nan) [❌ ❌ 🖥️CLI] - A nice little script that greets you on every launch, with some helpful (and customizable!) information.

## 📁 bash tool
_... description of the subcategory ..._

* [Basta!](https://www.kylheku.com/cgit/basta/about/) [❌ ❌ 🖥️CLI] - A small amount of GNU Bash code that maintains a scroll-protected status line at the bottom of the terminal.

## 📁 custom prompt
_... description of the subcategory ..._

* [blaze](nan) [❌ ❌ 🖥️TUI] - A customizable and informative prompt for bash, zsh, fish, on linux distributions.
* [Oh My Posh](https://ohmyposh.dev) [❌ ❌ 🖥️CLI] - From their README: "The most customizable and low-latency cross-platform/shell prompt renderer".

## 📁 shell
_... description of the subcategory ..._

* [Liquid Prompt](nan) [❌ ❌ 🖥️CLI] - Carefully designed prompt with useful information to show changes when it changes, saving time and frustration, and to show meaningful information with minimal visual clutter.
* [synth-shell-prompt](nan) [❌ ❌ 🖥️CLI] - A small eye-candy shell prompt with Git status displaying, a clock, intelligent $PWD shortening, and much more.

## 📁 shell prompt
_... description of the subcategory ..._

* [geometry](nan) [❌ ❌ 🖥️CLI] - A minimalistic, fully customizable Zsh prompt theme with support for asynchronous functions.
* [Polyglot Prompt](nan) [❌ ❌ 🖥️CLI] - A dynamic prompt for `zsh`, `bash`, `ksh93`, `mksh`, `pdksh`, `oksh`, `dash`, `yash`, `busybox ash`, and `osh` that uses basic ASCII symbols (and color, when possible).

## 📁 zsh prompt
_... description of the subcategory ..._

* [Powerlevel10k](nan) [❌ ❌ 🖥️CLI] - A theme for Zsh. It emphasizes speed, flexibility and out-of-the-box experience.
* [Pure](nan) [❌ ❌ 🖥️CLI] - Pretty, minimal, and fast ZSH prompt.

# religion
[Back to TOC](#📚-contents)

Tools to handle religious material, e.g. reading the Holy Bible
## 📁 bible readers
_... description of the subcategory ..._

* [bible](nan) [❌ ❌ 🖥️CLI] - Read the Holy Bible via the command line.

## 📁 cli bible viewer
_... description of the subcategory ..._

* [The Rock](nan) [❌ ❌ 🖥️CLI] - Command line King James bible viewer for Linux systems modeled after Debian's bible-kjv, but with extra features.

## 📁 command-line translator
_... description of the subcategory ..._

* [ltorah](nan) [❌ ❌ 🖥️CLI] - ltorah provides a way to read the ancient hebrew Torah from the command line.

## 📁 text readers
_... description of the subcategory ..._

* [bbl](nan) [❌ ❌ 🖥️CLI] - Read, search Holy Bible in command line.

# rm
[Back to TOC](#📚-contents)

Tools to manage the deletion of files/directories, often with the support of a trash can, i.e., the ability to restore deleted items
## 📁 DataRecovery
_... description of the subcategory ..._

* [RecoverPy](nan) [❌ ❌ 🖥️CLI] - Recover deleted files and overwritten data. It scans every block of the partition. You can even find a string in binary files.

## 📁 FileDeletionTool
_... description of the subcategory ..._

* [trash-cli](nan) [❌ ❌ 🖥️CLI] - Move files and folders to the trash on Linux (XDG trash), macOS (`macOS-trash` library) and Windows (`recycle-bin` library).

## 📁 ShellSyncBackup
_... description of the subcategory ..._

* [testdisk](https://www.cgsecurity.org/wiki/TestDisk) [❌ ❌ ❌] - Lets you undelete files from FAT, exFAT, NTFS, and ext2 filesystems and do many other things, e.g., fix partition tables and recover deleted partitions.

## 📁 command-line translator
_... description of the subcategory ..._

* [rmw](https://remove-to-waste.info/) [🤖 🌐 🖥️CLI] - (ReMove to Waste) is a trashcan/recycle bin utility for the command line. It can move and restore files to and from directories specified in a configuration file.

## 📁 enhanced cat
_... description of the subcategory ..._

* [rip](nan) [❌ ❌ 🖥️CLI] - Move and restore items from the graveyard (by default, `/tmp/graveyard-$USER` if $XDG_DATA_HOME is not set and `$XDG_DATA_HOME/graveyard` otherwise)

## 📁 file management
_... description of the subcategory ..._

* [gtrash](nan) [🤖 ❌ 🖥️TUI] - TUI for moving and restoring items from the XDG trash. Fully compliant with the FreeDesktop.org specification.

## 📁 file recovery
_... description of the subcategory ..._

* [extundelete](https://extundelete.sourceforge.net/) [❌ ❌ 🖥️CLI] - Recover deleted files from an ext3 or ext4 partition through its journal.
* [undelete-btrfs](nan) [❌ ❌ 🖥️CLI] - Automate the generation of path regex for BTRFS restore and attempt the restore for you in 3 levels. The longer a file has existed prior to being deleted, the more likely it is to be recovered.

## 📁 safe delete
_... description of the subcategory ..._

* [del](https://fex.belwue.de/fstools/del.html) [❌ ❌ 🖥️CLI] - Save deleted files to a .del/ subdirectory in the same directory.
* [rm-trash](nan) [❌ ❌ 🖥️CLI] - Meant to be used in place of `rm` in Linux, supporting all its arguments. It can move and restore the files from the XDG trash.
* [trashbhuwan](nan) [❌ ❌ 🖥️TUI] - Trashing CLI application for Linux distros, written in C.

## 📁 shell
_... description of the subcategory ..._

* [Brash](nan) [❌ ❌ 🖥️CLI] - Move and restore items from the XDG trash. Written in pure Bash.

## 📁 trash management
_... description of the subcategory ..._

* [trasher](nan) [❌ ❌ 🖥️TUI] - Delete files to a trash directory instead of deleting them immediately. Uses its own trash instead of the XDG one.

# rss
[Back to TOC](#📚-contents)

RSS feed visualizers, converters, and managers
## 📁 rss
_... description of the subcategory ..._

* [rss-cli](nan) [❌ 🌐 🖥️CLI] - A UNIX-inspired CLI application for interacting with RSS feeds.

## 📁 rss parser
_... description of the subcategory ..._

* [Sfeed](https://codemadness.org/sfeed.html) [❌ ❌ 🖥️CLI] - Sfeed is a RSS and Atom parser (and some format programs). It converts RSS or Atom feeds from XML to a TAB-separated file.

## 📁 rss reader
_... description of the subcategory ..._

* [Canto Curses](nan) [❌ ❌ 🖥️TUI] - Curses frontend for [Canto daemon](https://github.com/themoken/canto-next) for RSS feeds.
* [feedln](nan) [❌ 🌐 🖥️TUI] - A simple terminal RSS reader.
* [Newsraft](nan) [❌ 🌐 🖥️TUI] - Newsraft is a feed reader with ncurses user interface. It is greatly inspired by Newsboat and tries to be its lightweight counterpart.
* [nom](nan) [❌ 🌐 🖥️CLI] - RSS reader for the terminal.
* [rReader](nan) [❌ ❌ 🖥️TUI] - RSS reader client with TUI interface.
* [TermFeed](nan) [❌ 🌐 🖥️TUI] - A simple terminal feed reader.

## 📁 rss readers
_... description of the subcategory ..._

* [Newsboat](https://newsboat.org/) [❌ 🌐 🖥️CLI] - An RSS/Atom feed reader for the text console. It's an actively maintained fork of Newsbeuter.

## 📁 rss tool
_... description of the subcategory ..._

* [openring](nan) [❌ 🌐 🖥️CLI] - A tool for generating a webring from RSS feeds, so you can link to other blogs you like on your own blog.

# science
[Back to TOC](#📚-contents)

Packages for scientific research and science applications, e.g., bibliography and publication management
## 📁 AcademicDownloaderCLI
_... description of the subcategory ..._

* [scholarref](https://adamsgaard.dk/scholarref.html) [❌ 🌐 🖥️CLI] - Tools to never deal with journal webpages again.

## 📁 AlternativeVCS
_... description of the subcategory ..._

* [cobib](nan) [❌ ❌ 🖥️CLI] - Simple, command-line based bibliography management tool.

## 📁 AudioMixer
_... description of the subcategory ..._

* [FAWOC](nan) [❌ ❌ 🖥️CLI] - FAWOC is a TUI program for manually labelling a list of words. It has been developed to support the efficient clustering of documents based on topic modeling algorithms such as Dirichlet Latent Allocation.

## 📁 BibManagerCLI
_... description of the subcategory ..._

* [Pubs](nan) [🤖 ❌ 🖥️CLI] - Pubs organizes your scientific papers together with their bibliographic data and provides command line access to basic and advanced manipulation of your library.

## 📁 ConferenceTrackerCLI
_... description of the subcategory ..._

* [conrad](nan) [❌ 🌐 🖥️CLI] - Track conferences and meetups.

## 📁 bioinformatics
_... description of the subcategory ..._

* [GCTU](nan) [❌ ❌ 🖥️CLI] - A simple command line tool which allows one to convert DNA code sequences to the different RNA sequences.

## 📁 command-line translator
_... description of the subcategory ..._

* [element](nan) [❌ ❌ 🖥️CLI] - Periodic table on the command line.

## 📁 education
_... description of the subcategory ..._

* [periodic-table-cli-py](nan) [❌ ❌ 🖥️CLI] - An interactive Periodic Table of Elements app for the console.

## 📁 enhanced cat
_... description of the subcategory ..._

* [pt.sh](nan) [❌ ❌ 🖥️CLI] - CLI periodic table with search and many properties.
* [slr-kit](nan) [❌ ❌ 🖥️CLI] - Set of CLI tools to assist the writing of Systematic Literature Reviews powered by Natural Language Processing.

## 📁 fun tools
_... description of the subcategory ..._

* [starfetch](nan) [❌ ❌ 🖥️CLI] - Command line tool that displays constellations.

## 📁 game
_... description of the subcategory ..._

* [gol-tui](nan) [❌ ❌ 🖥️TUI] - Conway's Game of Life TUI.

## 📁 knowledge base
_... description of the subcategory ..._

* [bib.awk](nan) [❌ ❌ 🖥️CLI] - Bibliography manager written in awk.
* [bibtools](nan) [❌ ❌ 🖥️CLI] - Command-line bibliography manager.
* [papis](nan) [❌ ❌ 🖥️CLI] - Extensible document and bibliography manager.

## 📁 periodic table
_... description of the subcategory ..._

* [periodic-table-cli](nan) [❌ ❌ 🖥️TUI] - An interactive Periodic Table of Elements app for the console!
* [ptable](nan) [❌ ❌ 🖥️TUI] - A beautiful TUI periodic table for GNU/Linux terminals.

## 📁 reference manager
_... description of the subcategory ..._

* [BibMan](https://ductri.github.io/note/2023/09/27/bibman.html) [❌ ❌ 🖥️TUI] - A TUI bibliography manager. It aims to support only the most basis features as a general bibliography manager.

## 📁 terminal animation
_... description of the subcategory ..._

* [gof-rs](nan) [❌ ❌ 🖥️CLI] - Game of life rendered in your terminal with over 500+ unique patterns to choose from.

## 📁 terminal games
_... description of the subcategory ..._

* [Go-L](nan) [❌ ❌ 🖥️CLI] - Game of Life with different update rules and on a bunch of different topologies (sphere, torus, klein bottle, etc.).

# screen-recorder
[Back to TOC](#📚-contents)

Tools to record the content of the terminal and manage the recording (e.g., converting into animated GIFs)
## 📁 svg generator
_... description of the subcategory ..._

* [terminal-svg-screenshot](nan) [❌ ❌ 🖥️CLI] - A tool for creating beautiful SVG screenshots of terminal output, perfect for documentation and blog posts.

## 📁 terminal animation
_... description of the subcategory ..._

* [agg](nan) [❌ ❌ 🖥️CLI] - agg is a command-line tool for generating animated GIF files from asciicast v2 files produced by `asciinema` terminal recorder.

## 📁 terminal recorder
_... description of the subcategory ..._

* [goscript](nan) [❌ 🌐 🖥️CLI] - Goscript is a tool that records the terminal session (well, any command you run it with) and saves the output in a self contained HTML file that can be run in the browser, to playback the session.
* [t-rec](nan) [❌ 🌐 🖥️CLI] - Blazingly fast terminal recorder that generates animated GIF images for the web written in rust.
* [terminal-recorder](nan) [❌ ❌ 🖥️CLI] - Terminal recorder allows you to record your bash session, and export it to HTML so then you can share it with your friends.
* [terminalizer](nan) [❌ 🌐 🖥️CLI] - Record your terminal and generate animated GIF images or share a web player link [www.terminalizer.com](www.terminalizer.com).
* [termtosvg](nan) [❌ ❌ 🖥️CLI] - A Unix terminal recorder written in Python that renders your command line sessions as standalone SVG animations.
* [ttygif](nan) [❌ ❌ 🖥️CLI] - ttygif converts a ttyrec file into GIF files. It's a stripped down version of ttyplay that screenshots every frame.
* [ttystudio](nan) [❌ ❌ 🖥️CLI] - Record your terminal and compile it to a GIF or APNG without any external dependencies, bash scripts, GIF concatenation, etc.
* [vhs](nan) [❌ ❌ 🖥️CLI] - Write terminal GIFs as code for integration testing and demoing your CLI tools.

## 📁 terminal sharing
_... description of the subcategory ..._

* [asciinema](nan) [❌ ❌ 🖥️CLI] - Terminal session recorder.

# screensaver
[Back to TOC](#📚-contents)

Screen savers with animations for the idle times of the computer
## 📁 TerminalScreensaver
_... description of the subcategory ..._

* [termsaver](http://termsaver.brunobraga.net/) [❌ ❌ 🖥️TUI] - termsaver to enjoy fancy ASCII screensavers like matrix, clock, starwars, and a couple of not-safe-for-work screens.

## 📁 ascii aquarium
_... description of the subcategory ..._

* [lifecycler](nan) [❌ ❌ 🖥️TUI] - An aquarium that runs in your terminal.

## 📁 ascii screensaver
_... description of the subcategory ..._

* [conway-screensaver](nan) [❌ ❌ 🖥️TUI] - A Conways game of life screensaver for the terminal.

## 📁 screensaver
_... description of the subcategory ..._

* [ASCII Saver](nan) [❌ ❌ 🖥️CLI] - Screensaver for terminals.
* [sclocka](nan) [❌ ❌ 🖥️TUI] - The real screensaver/lock for terminals.

## 📁 terminal animations 
_... description of the subcategory ..._

* [pipes.sh](nan) [❌ ❌ 🖥️TUI] - Animated pipes terminal screensaver.

# security
[Back to TOC](#📚-contents)

Cryptography, ciphered archive managers, encrypted file-systems
## 📁 EncryptionCLI
_... description of the subcategory ..._

* [GnuPG](https://gnupg.org/) [❌ ❌ 🖥️CLI] - GnuPG is a complete and free implementation of the OpenPGP standard as defined by RFC4880 (also known as PGP).

## 📁 FastFindAlternative
_... description of the subcategory ..._

* [feroxbuster](nan) [❌ ❌ 🖥️CLI] - A fast, simple, recursive content discovery tool written in Rust.

## 📁 FileSignerCLI
_... description of the subcategory ..._

* [Minisign](nan) [❌ ❌ 🖥️CLI] - A dead simple tool to sign files and verify digital signatures.

## 📁 OneTimeSecretCLI
_... description of the subcategory ..._

* [ots](nan) [❌ ❌ 🖥️CLI] - Share end-to-end encrypted secrets with others via a one-time URL.

## 📁 SecuritySandboxCLI
_... description of the subcategory ..._

* [Firejail](https://firejail.wordpress.com/) [❌ ❌ 🖥️CLI] - A SUID program that reduces the risk of security breaches by restricting the running environment of untrusted applications using Linux namespaces and seccomp-bpf.

## 📁 TOTPAuthenticatorCLI
_... description of the subcategory ..._

* [cotp](nan) [❌ ❌ 🖥️CLI] - Trustworthy, encrypted, command-line TOTP/HOTP authenticator app with import functionality.

## 📁 VimEnhancer
_... description of the subcategory ..._

* [cream](https://z3bra.org/cream/) [❌ ❌ 🖥️TUI] - Encrypt and decrypt streams of data with only a master password. The key is derivated from the password + salt combo, and used to encrypt data byte per byte.

## 📁 cli encryption
_... description of the subcategory ..._

* [enc](nan) [❌ ❌ 🖥️CLI] - A modern and friendly CLI alternative to GnuPG: generate and download keys, encrypt, decrypt, and sign text and files, and more.

## 📁 code signer
_... description of the subcategory ..._

* [quill](https://anchore.com/opensource/) [❌ ❌ 🖥️CLI] - Simple mac binary signing from any platform.

## 📁 encrypted filesystem
_... description of the subcategory ..._

* [encfs](http://www.arg0.net/#!encfs/c1awt) [❌ ❌ 🖥️CLI] - Encrypted filesystem in user-space based on [FUSE](https://it.wikipedia.org/wiki/FUSE), mounts an encrypted directory into a clear one.
* [gocryptfs](https://nuetzlich.net/gocryptfs) [❌ ❌ 🖥️CLI] - An encrypted overlay filesystem written in Go.

## 📁 encryption
_... description of the subcategory ..._

* [age](https://age-encryption.org/) [❌ ❌ 🖥️CLI] - A simple, modern and secure encryption tool with small explicit keys, no config options, and UNIX-style composability.
* [eddy](nan) [❌ ❌ 🖥️CLI] - Simple, fast CLI file encryption tool.

## 📁 encryption module
_... description of the subcategory ..._

* [cipher](nan) [❌ ❌ 🖥️CLI] - An Ash module that makes it easy to perform aes-256-cbc encryption for files and directories.

## 📁 enhanced cat
_... description of the subcategory ..._

* [wifi-password](nan) [❌ ❌ 🖥️CLI] - Get Wi-Fi pass.

## 📁 file encryption
_... description of the subcategory ..._

* [securo](nan) [❌ ❌ 🖥️CLI] - Encrypt and descrypt files and folders using a symmetric encryption.

## 📁 fuzzer
_... description of the subcategory ..._

* [sandsifter](nan) [❌ ❌ 🖥️CLI] - The x86 processor fuzzer.

## 📁 gpg tools
_... description of the subcategory ..._

* [gpg-tui](nan) [❌ ❌ 🖥️TUI] - Manage your GnuPG keys with ease!

## 📁 license manager
_... description of the subcategory ..._

* [grant](https://anchore.com/opensource/) [❌ ❌ 🖥️CLI] - Grant is a tool for generating and managing license security policies for container images.

## 📁 oauth client
_... description of the subcategory ..._

* [OAuth2c](nan) [❌ 🌐 🖥️CLI] - A command-line tool for interacting with OAuth 2.0 authorization servers.

## 📁 package scanner
_... description of the subcategory ..._

* [syft](https://anchore.com/opensource/) [❌ ❌ 🖥️CLI] - Syft is a CLI tool and library for generating a Software Bill of Materials (SBOM) from container images and filesystems.

## 📁 password generator
_... description of the subcategory ..._

* [pgen](nan) [❌ ❌ 🖥️CLI] - Generate passphrases using the wordlists for random passphrases made by the EFF.

## 📁 password manager
_... description of the subcategory ..._

* [safe](https://z3bra.org/safe/) [❌ ❌ 🖥️CLI] - Password protected secret keeper. Secrets are encrypted and stored on disk using a key derivated from your master password - no keys to manage.

## 📁 password recovery
_... description of the subcategory ..._

* [hashcat](https://hashcat.net/hashcat/) [❌ ❌ 🖥️CLI] - A robust and efficient password cracking tool that can help you recover lost passwords, audit password security, benchmark, or just figure out what data is stored in a hash.

## 📁 secret manager
_... description of the subcategory ..._

* [SOPS](nan) [❌ ❌ 🖥️CLI] - SOPS (Secrets OPerationS) is a simple and flexible tool for managing secrets, sops is an editor of encrypted files that supports YAML, JSON, ENV, INI and BINARY formats, encrypting the values but not the keys.

## 📁 secure backups
_... description of the subcategory ..._

* [PaperAge](nan) [❌ ❌ 🖥️CLI] - Easy and secure paper backups of secrets, which takes a text and generates an encrypted QR code to print on paper.

## 📁 security audit
_... description of the subcategory ..._

* [vet](nan) [❌ ❌ 🖥️CLI] - Tool for identifying risks in open source software supply chain.

## 📁 security tools
_... description of the subcategory ..._

* [SSH-Snake](nan) [❌ 🌐 🖥️CLI] - SSH-Snake is a self-propagating, self-replicating, file-less script that automates the post-exploitation task of SSH private key and host discovery.

## 📁 shell
_... description of the subcategory ..._

* [uacme](nan) [❌ ❌ 🖥️CLI] - ACMEv2 client written in plain C with minimal dependencies.

## 📁 ssh vulnerability scan
_... description of the subcategory ..._

* [sshamble](nan) [❌ 🌐 🖥️CLI] - Unexpected exposures in SSH; the tool checks for several common weaknesses in SSH security issues.

## 📁 ssl tools
_... description of the subcategory ..._

* [acmetool](nan) [❌ ❌ 🖥️CLI] - Easy-to-use command line tool for automatically acquiring certificates from ACME servers (such as Let's Encrypt).

## 📁 steganography
_... description of the subcategory ..._

* [Image Steganography Tool](nan) [❌ ❌ 🖥️CLI] - Simple C++ Encryption and Steganography tool that uses Password-Protected-Encryption to secure a file's contents.
* [jdvrif](nan) [❌ ❌ 🖥️CLI] - CLI tool to embed or extract files via a JPG image. Post & share your embedded JPG image on compatible sites.
* [pdvzip](nan) [❌ ❌ 🖥️CLI] - CLI tool to embed a ZIP file within a PNG image to create a tweetable and "executable" PNG-ZIP polyglot file. Post & share your PNG-ZIP image on compatible sites.
* [StegCloak](nan) [❌ ❌ 🖥️CLI] - Hide secrets with invisible characters in plain text securely using passwords
* [van-gonography](nan) [❌ ❌ 🖥️CLI] - Hide your files of any type inside a image of your choice using steganography.

## 📁 vulnerability scanner
_... description of the subcategory ..._

* [grype](https://anchore.com/opensource/) [❌ ❌ 🖥️CLI] - Grype is a vulnerability scanner for container images and filesystems that supports a wide range of package managers.

## 📁 vulnerability viewer
_... description of the subcategory ..._

* [flawz](nan) [❌ ❌ 🖥️TUI] - A Terminal UI for browsing security vulnerabilities (CVEs).

# shells
[Back to TOC](#📚-contents)

Shell programs that enable the interaction through the terminal
## 📁 automation shell
_... description of the subcategory ..._

* [PowerShell](https://microsoft.com/PowerShell) [❌ ❌ 🖥️CLI] - An automation and configuration tool/framework optimized for dealing with structured data, REST APIs, and object models.

## 📁 kornshell
_... description of the subcategory ..._

* [oksh](nan) [❌ ❌ 🖥️CLI] - Portable OpenBSD ksh.

## 📁 modern shell
_... description of the subcategory ..._

* [Oils](https://github.com/oilshell/oil) [❌ ❌ 🖥️CLI] - From their README: "Oils is our upgrade path from bash to a better language and runtime!" 

## 📁 shell
_... description of the subcategory ..._

* [arsh](nan) [❌ ❌ 🖥️CLI] - A statically typed scripting language with shell-like features.
* [Bash](https://www.gnu.org/software/bash/) [❌ ❌ 🖥️CLI] - (Bourne Again SHell) The most widespread system shell to date.
* [Cat9](nan) [❌ ❌ 🖥️TUI] - Cat9 is a user shell script for LASH - a command-line shell that discriminates against terminal emulators, written in Lua.
* [cosh](nan) [❌ ❌ 🖥️CLI] - Concatenative command-line shell.
* [DASH](http://gondor.apana.org.au/~herbert/dash/) [❌ ❌ 🖥️CLI] - DASH is a POSIX-compliant implementation of /bin/sh that aims to be as small as possible. It does this without sacrificing speed where possible.
* [dune](nan) [❌ ❌ 🖥️CLI] - A customizable shell that aims to be cozy.
* [Elvish](nan) [❌ ❌ 🖥️CLI] - Elvish is a versatile interactive shell and expressive programming language, combined into one seamless package.
* [es](https://wryun.github.io/es-shell/) [❌ ❌ 🖥️CLI] - (extensible shell) shell with first class functions, lexical scope, exceptions, and rich return values, based on Plan9's rc.
* [Fish](https://fishshell.com/) [❌ ❌ 🖥️CLI] - "A command line shell for the 90s"; focused on user-friendliness, with powerful autosuggestions, colors, "sane scripting" (w.r.t. to Bash).
* [Ion](nan) [❌ ❌ 🖥️CLI] - Ion is a modern system shell that features a simple, yet powerful, syntax.
* [ksh93](nan) [❌ ❌ 🖥️CLI] - (KornShell) a shell programming language that is compatible with the Bourne Shell in addition and has the major command-entry features of the BSD shell csh.
* [mksh](http://www.mirbsd.org/mksh.htm) [❌ ❌ 🖥️CLI] - (MirBSD Korn Shell) an actively developed free implementation of the Korn Shell programming language and a successor to the Public Domain Korn Shell (pdksh).
* [murex](https://murex.rocks) [❌ ❌ 🖥️CLI] - An intuitive, typed and content aware shell for the 2020s and beyond.
* [N-Commodore](nan) [❌ ❌ 🖥️TUI] - A novel file manager/shell/command-line, where everything is panelized, greppable and remembered.
* [Nushell](nan) [❌ ❌ 🖥️CLI] - A modern shell written in Rust, where all data is structured.
* [Rash](https://rash-lang.org) [❌ ❌ 🖥️CLI] - A shell language, library, and REPL for Racket.
* [Reptyl](nan) [❌ ❌ 🖥️CLI] - A cross-platform command line shell that supports execution of commands in natural language.
* [Tcsh](https://www.tcsh.org) [❌ ❌ 🖥️CLI] - A shell that, at the time of creation, introduced command completion and command line editing.
* [xonsh](https://xon.sh/) [❌ ❌ 🖥️CLI] - The xonsh shell lets you easily mix Python and shell commands in a powerful and simplified approach to the command line.
* [Yash](https://magicant.github.io/yash) [❌ ❌ 🖥️CLI] - Yash (yet another shell) a POSIX-compliant command line shell written in C99.
* [Zsh](http://www.zsh.org/) [❌ ❌ 🖥️CLI] - Alternative shell designed for interactive use.

## 📁 text-based window manager
_... description of the subcategory ..._

* [Twin](nan) [❌ ❌ 🖥️TUI] - Text mode window environment. A "retro" program for embedded or remote systems, that doubles as X11 terminal and text-mode equivalent of VNC server.

# system
[Back to TOC](#📚-contents)

System management tools, such as for brightness control, dotfile and environment variable management, notifications, etc.
## 📁 CloudSyncManager
_... description of the subcategory ..._

* [chezmoi](https://www.chezmoi.io/) [❌ ❌ 🖥️CLI] - Manage your dotfiles across multiple diverse machines, securely.

## 📁 DirectoryOrganizer
_... description of the subcategory ..._

* [direnv](https://direnv.net/) [❌ ❌ 🖥️CLI] - Loads and unloads environment variables depending on the current directory.

## 📁 HardwareController
_... description of the subcategory ..._

* [brightnessctl](nan) [❌ ❌ 🖥️CLI] - Read and control device brightness. Devices, by default, include backlight and LEDs - searched for in corresponding classes.

## 📁 ProcessManagerCLI
_... description of the subcategory ..._

* [fkill-cli](nan) [❌ ❌ 🖥️CLI] - Simple cross-platform process killer.

## 📁 SystemMonitorTUI
_... description of the subcategory ..._

* [systeroid](nan) [❌ ❌ 🖥️TUI] - A more powerful alternative to sysctl(8) with a terminal user interface.

## 📁 autocomplete
_... description of the subcategory ..._

* [argc-completions](nan) [❌ ❌ 🖥️CLI] - Autocompletion for any shell and any command.
* [inshellisense](nan) [🤖 ❌ 🖥️CLI] - IDE style command line auto complete with support for 600+ command line tools.

## 📁 brightness control
_... description of the subcategory ..._

* [Rumos](nan) [❌ ❌ 🖥️CLI] - CLI utility for controlling screen brightness.

## 📁 checksum tools
_... description of the subcategory ..._

* [checksum.sh](https://checksum.sh/) [❌ 🌐 🖥️CLI] - Checksum.sh is a simple way to download, review, and verify install scripts. If the checksum is OK the script will be printed to stdout, which can be piped to sh or elsewhere.

## 📁 clipboard manager
_... description of the subcategory ..._

* [clipy](nan) [❌ ❌ 🖥️TUI] - Manage clipboard history.

## 📁 clipboard tool
_... description of the subcategory ..._

* [clipper](nan) [❌ ❌ 🖥️CLI] - Seamlessly copy file contents to clipboard from command line. Lightweight, cross-platform tool for instant text transfers.

## 📁 command-line translator
_... description of the subcategory ..._

* [has](nan) [❌ ❌ 🖥️CLI] - Checks presence of various command line tools on the PATH and reports their installed version.

## 📁 console sharing
_... description of the subcategory ..._

* [auto-cpufreq](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Automatic CPU speed and power optimizer for Linux, which allows to dynamically change the settings of the CPU to save energy and extend the battery life on laptops.
* [conspy](http://conspy.sourceforge.net/) [❌ ❌ 🖥️CLI] - "Conspy allows a (possibly remote) user to see what is displayed on a Linux virtual console, and send keystrokes to it." 

## 📁 dotfiles manager
_... description of the subcategory ..._

* [YAS-BDSM](nan) [❌ ❌ 🖥️CLI] - YAS-BDSM (Yet Another Stow-Based Dotfiles System Manager): a minimal, UNIX-based, cross-platform, hierarchical dotfiles manager.
* [ydf](nan) [❌ ❌ 🖥️CLI] - A disruptive dotfiles manager+. Be ready to work in just a few minutes on your Fresh OS.

## 📁 enhanced cat
_... description of the subcategory ..._

* [just](nan) [❌ ❌ 🖥️CLI] - Handy way to save and run project-specific commands.
* [mackup](nan) [❌ 🌐 🖥️CLI] - Keep your application settings in sync (OS X/Linux).

## 📁 env manager
_... description of the subcategory ..._

* [rs-env](nan) [❌ ❌ 🖥️CLI] - Hierarchical environment variable management, compiling the resulting set of from a hierarchical list of `<name>.env` files.

## 📁 hardware info
_... description of the subcategory ..._

* [lshw](http://www.ezix.org/project/wiki/HardwareLiSter) [❌ ❌ 🖥️CLI] - A small tool to provide detailed information on the hardware configuration of the machine. It can report exact memory configuration, firmware version, mainboard configuration, CPU version and speed, cache configuration, bus speed, etc.

## 📁 man page viewer
_... description of the subcategory ..._

* [qman](nan) [❌ ❌ 🖥️CLI] - A more modern man page viewer for our terminals.

## 📁 mount tools
_... description of the subcategory ..._

* [bashmount](nan) [❌ ❌ 🖥️CLI] - Tool to mount and unmount removable media from the command-line with a nice interface to list the available options..

## 📁 notification tool
_... description of the subcategory ..._

* [ntfyme](nan) [❌ 🌐 🖥️TUI] - Simple to use, cross platform notification tool which sends you local, gmail, telegram, etc notification when a long running process ends with detailed diagnostics, along with features like tracking for suspended process and terminate them automatically.

## 📁 notifications
_... description of the subcategory ..._

* [Ntfy](nan) [❌ ❌ 🖥️CLI] - Cross-platform Python utility that enables you to automatically get desktop notifications on demand or when long-running commands complete. It can as well send push notifications to your phone once a particular command completes.

## 📁 port killer
_... description of the subcategory ..._

* [killport](nan) [❌ ❌ 🖥️CLI] - A command-line tool to easily kill processes running on a specified port.

## 📁 process killer
_... description of the subcategory ..._

* [Kill](nan) [❌ ❌ 🖥️CLI] - Small bash-only script for killing processes/sending signals.

## 📁 sandbox runner
_... description of the subcategory ..._

* [landrun](nan) [❌ ❌ 🖥️CLI] - Run any Linux process in a secure, unprivileged sandbox using Landlock. Think firejail, but lightweight, user-friendly, and baked into the kernel.

## 📁 shell
_... description of the subcategory ..._

* [rfsh](nan) [❌ ❌ 🖥️CLI] - Run shell scripts in batch, concurrently, fully customized with variable.
* [x-cmd](https://www.x-cmd.com/) [❌ ❌ 🖥️CLI] - A toolset implemented using posix shell and awk offering many interesting features and that is very small in size.

## 📁 shell logger
_... description of the subcategory ..._

* [shournal](nan) [❌ ❌ 🖥️CLI] - Log shell-commands and used files. Snapshot executed scripts. Fully automatic.

## 📁 sound notifier
_... description of the subcategory ..._

* [sysm](nan) [❌ ❌ 🖥️CLI] - Makes your system play custom sounds when any configured system or external event happens.

## 📁 system inspector
_... description of the subcategory ..._

* [dtui](nan) [❌ ❌ 🖥️TUI] - Small TUI for introspecting the state of the system/session dbus.

## 📁 system manager
_... description of the subcategory ..._

* [systemctl-tui](nan) [❌ ❌ 🖥️TUI] - A fast simple TUI for interacting with systemd services and their logs.
* [sysz](nan) [❌ ❌ 🖥️TUI] - fzf terminal UI for systemctl.

## 📁 task killer
_... description of the subcategory ..._

* [fzf-kill](nan) [❌ ❌ 🖥️TUI] - The no-nonsense task killer for your terminal.

## 📁 user management
_... description of the subcategory ..._

* [ugm](nan) [❌ 🌐 🖥️TUI] - A terminal based UNIX user and group browser.

## 📁 vcs benchmark
_... description of the subcategory ..._

* [empiriqa](nan) [❌ ❌ 🖥️CLI] - empiriqa (command name is epiq) is a tool for interactively manipulating UNIX pipelines.

## 📁 viewport tools
_... description of the subcategory ..._

* [viewport-list-cli](nan) [❌ ❌ 🖥️CLI] - Return a list of devices and their viewports.

## 📁 window info tools
_... description of the subcategory ..._

* [active-win-cli](nan) [❌ ❌ 🖥️CLI] - Get the title/id/etc of the active window.

# terminal
[Back to TOC](#📚-contents)

Terminal and terminal multiplexers
## 📁 ProjectNavigatorTUI
_... description of the subcategory ..._

* [mynav](nan) [❌ ❌ 🖥️TUI] - A powerful terminal-based workspace navigator and session manager built in Go, MyNav helps developers organize and manage multiple projects through an intuitive interface, seamlessly integrating with tmux sessions.

## 📁 SessionDetachTool
_... description of the subcategory ..._

* [dtach](nan) [❌ ❌ 🖥️CLI] - A program written in C that emulates the detach feature of screen.

## 📁 TmuxSessionManager
_... description of the subcategory ..._

* [mx](nan) [❌ ❌ 🖥️CLI] - A tmux session manager written as a single Bash script.

## 📁 minimal terminal
_... description of the subcategory ..._

* [st](https://st.suckless.org/) [❌ ❌ 🖥️CLI] - A simple terminal implementation for X.

## 📁 multiplexer
_... description of the subcategory ..._

* [screen](https://www.gnu.org/software/screen/) [❌ ❌ 🖥️TUI] - Terminal multiplexer that split a physical terminal between several processes, typically interactive shells.
* [wezterm](nan) [❌ ❌ 🖥️CLI] - A GPU-accelerated cross-platform terminal emulator and multiplexer implemented in Rust with tons of features.
* [Zellij](nan) [❌ ❌ 🖥️TUI] - A workspace aimed at developers, ops-oriented people and anyone who loves the terminal. At its core, it is a terminal multiplexer.

## 📁 shared-terminal
_... description of the subcategory ..._

* [Tmate](https://tmate.io/) [❌ 🌐 🖥️TUI] - A fork of tmux that allows sharing the terminal with other users. AFAIK, it connects to a centralized server to establish the connection. Someone may see this inconvenient for privacy issues.

## 📁 terminal emulator
_... description of the subcategory ..._

* [alacritty](https://alacritty.org) [❌ ❌ 🖥️CLI] - A GPU-Accelerated terminal emulator that comes with sensible defaults, but allows for extensive configuration.
* [extraterm](https://extraterm.org/) [❌ ❌ 🖥️CLI] - The swiss army chainsaw of terminal emulators.
* [ghostty](nan) [❌ ❌ 🖥️CLI] - A fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration.
* [kitty](https://sw.kovidgoyal.net/kitty/) [❌ ❌ 🖥️CLI] - A fast, feature-rich, GPU based terminal emulator.
* [mlterm](https://mlterm.sourceforge.net/) [❌ ❌ 🖥️CLI] - A very fast low latency terminal emulator with features such as rendering variable width fonts, proper bidirectional support out of the box, a daemon mode, multiple XIM, and true background transparency.

## 📁 terminal manager
_... description of the subcategory ..._

* [dvtm](https://www.brain-dump.org/projects/dvtm) [❌ ❌ 🖥️CLI] - Dynamic console window manager that enables dynamic tiling window management for multiple terminal applications.

## 📁 terminal multiplexer
_... description of the subcategory ..._

* [tmux](https://tmux.github.io/) [❌ ❌ 🖥️TUI] - Terminal multiplexer; born to improve `screen`; client-server architecture, `vi` and `emacs` key-bindings, search in window feature and many more.

## 📁 terminal sharing
_... description of the subcategory ..._

* [abduco](https://www.brain-dump.org/projects/abduco) [❌ ❌ 🖥️CLI] - abduco provides session management i.e. it allows programs to be run independently of their controlling terminal.
* [mtm](nan) [❌ ❌ 🖥️TUI] - Micro Terminal Multiplexer - Simple but usable, stable and minimalistic terminal multiplexer.
* [peaches](nan) [❌ ❌ 🖥️CLI] - A smart switcher for the terminal. Based on tmux.
* [vtm](nan) [❌ ❌ 🖥️TUI] - Virtual terminal multiplexer with window manager and session sharing.
* [warp](nan) [❌ ❌ 🖥️TUI] - Secure and simple terminal sharing.

## 📁 tmux tools
_... description of the subcategory ..._

* [tmux-nested](nan) [❌ ❌ 🖥️CLI] - Plugin for nested tmux workflows.
* [tmux-session](nan) [❌ ❌ 🖥️TUI] - Manage tmux sessions using fzf.

## 📁 wayland terminal
_... description of the subcategory ..._

* [wterm](nan) [❌ ❌ 🖥️CLI] - A native Wayland terminal emulator based on an st fork using wld.

## 📁 window-manager
_... description of the subcategory ..._

* [byobu](http://byobu.co/) [❌ ❌ 🖥️TUI] - A text-based window manager and terminal multiplexer; it features enhanced profiles, convenient keybindings, configuration utilities, and toggle-able system status notifications; compatible with `screen` and `tmux`.

# text-processing
[Back to TOC](#📚-contents)

Text processing utilities to cut or sort lines, find dead links, colorize command output, etc.
## 📁 FileLineDeduperCLI
_... description of the subcategory ..._

* [anew](nan) [❌ ❌ 🖥️CLI] - Tool for adding new lines to files, skipping duplicates.

## 📁 FuzzySelectorCLI
_... description of the subcategory ..._

* [choose](nan) [❌ ❌ 🖥️CLI] - A human-friendly and fast alternative to cut and (sometimes) awk.

## 📁 LinkCheckerCLI
_... description of the subcategory ..._

* [brok](nan) [❌ 🌐 🖥️CLI] - Find broken links in text documents.
* [deadlink](nan) [❌ 🌐 🖥️CLI] - Parses text files for HTTP URLs and checks if they are still valid. Good to use on Markdown documentation files.

## 📁 TextProcessorCLI
_... description of the subcategory ..._

* [tuc](nan) [❌ ❌ 🖥️CLI] - You want to cut on more than just a character, perhaps using negative indexes or format the selected fields as you want... Maybe you want to cut on lines (ever needed to drop first and last line?)... That's where tuc can help.

## 📁 ascii-text-rendering
_... description of the subcategory ..._

* [skroll](https://z3bra.org/skroll/) [❌ ❌ 🖥️CLI] - A small utility that you can use to make a text scroll. Pipe text to it, and it will scroll a given number of letters from right to left.

## 📁 browser utilities
_... description of the subcategory ..._

* [kill-tabs](nan) [❌ ❌ 🖥️CLI] - Kill all Chrome tabs to improve performance, decrease battery usage, and save memory.

## 📁 character frequency
_... description of the subcategory ..._

* [charfreq](nan) [❌ ❌ 🖥️TUI] - Very simple command-line tool that counts (unicode) character frequency from standard input.

## 📁 cli formatter
_... description of the subcategory ..._

* [rich](nan) [❌ ❌ 🖥️CLI] - Rich-CLI is a command line toolbox for fancy output in the terminal, built with [Rich](https://github.com/Textualize/rich).

## 📁 code format checkers
_... description of the subcategory ..._

* [detect-indent-cli](nan) [❌ ❌ 🖥️CLI] - Detect the indentation of code.

## 📁 command-line translator
_... description of the subcategory ..._

* [espanso](nan) [❌ ❌ 🖥️CLI] - Cross-platform Text Expander written in Rust. Not limited to the command line.
* [huniq](nan) [❌ ❌ 🖥️CLI] - Command line utility to remove duplicates from the given input. Note that huniq does not sort the input, it just removes duplicates.
* [hyphertool](nan) [❌ ❌ 🖥️CLI] - Command-line tool for syllabification and hyphenisation for multiple languages.
* [lingua-cli](nan) [❌ ❌ 🖥️CLI] - This is a small command-line tool for language detection, it is a simple wrapper around the lingua-rs library for Rust.
* [stam-tools](nan) [❌ ❌ 🖥️TUI] - A collection of command-line tools for working with STAM, a data-model for stand-off annotations on text.

## 📁 country normalizer
_... description of the subcategory ..._

* [Normalize Country](nan) [❌ ❌ 🖥️CLI] - Convert country names and codes to a standard.

## 📁 data extractor
_... description of the subcategory ..._

* [seaq](nan) [❌ 🌐 🖥️CLI] - seaq (pronounced "seek") allows you to extract text data from the web and process it with your favorite prompt and LLM model, all from your terminal.

## 📁 directory tree
_... description of the subcategory ..._

* [gtree](nan) [❌ ❌ 🖥️CLI] - Using either Markdown or programmatically to generate directory trees and directories, and to verify directories.

## 📁 documentation
_... description of the subcategory ..._

* [toc](nan) [❌ ❌ 🖥️CLI] - Generate a table of contents from the comments of a file.

## 📁 enhanced cat
_... description of the subcategory ..._

* [as-tree](nan) [❌ ❌ 🖥️CLI] - Print a list of paths as a tree of paths.
* [hck](nan) [❌ ❌ 🖥️CLI] - A sharp cut clone.
* [lolcat](nan) [❌ ❌ 🖥️CLI] - Ruby Gem to colorize the output of the cat command.

## 📁 file size tools
_... description of the subcategory ..._

* [gzip-size-cli](nan) [❌ ❌ 🖥️CLI] - Get the gzipped size of a file.

## 📁 fuzzy text matcher
_... description of the subcategory ..._

* [analiticcl](nan) [❌ ❌ 🖥️TUI] - An approximate string matching or fuzzy-matching system for spelling correction, normalisation or post-OCR correction.

## 📁 hashing tools
_... description of the subcategory ..._

* [HASHA CLI](nan) [❌ ❌ 🖥️CLI] - Hashing made simple. Get the hash of text or stdin.

## 📁 html parsers
_... description of the subcategory ..._

* [pup](nan) [❌ ❌ 🖥️CLI] - Parsing HTML at the command line.

## 📁 lexicon matcher
_... description of the subcategory ..._

* [lexmatch](nan) [❌ ❌ 🖥️TUI] - This is a simple lexicon matching tool that, given a lexicon of words or phrases, identifies all matches in a given target text, returning their exact positions. It can be used compute a frequency list for a lexicon, on a target corpus.

## 📁 line selector
_... description of the subcategory ..._

* [Line Select](nan) [❌ ❌ 🖥️CLI] - A powerful utility enabling interactive line selection from stdin, allowing to seamlessly integrate, pause, select, and refine your pipeline, enhancing data processing precision.

## 📁 log debugger
_... description of the subcategory ..._

* [logshark](nan) [❌ ❌ 🖥️CLI] - Logshark is a debugger CLI for JSON logs written in Go.

## 📁 log pattern extractor
_... description of the subcategory ..._

* [logu](nan) [❌ ❌ 🖥️TUI] - Extract patterns from (streaming) unstructured log messages.

## 📁 log viewer
_... description of the subcategory ..._

* [rare](nan) [❌ ❌ 🖥️CLI] - Real-time regex-extraction and aggregation into common formats such as histograms, bar graphs, numerical summaries, tables, and more!
* [swordfish-rs](nan) [❌ 🌐 🖥️CLI] - Mimics real person behavior with real-time typing into terminal uses a screenplay where text and timings are specified.

## 📁 markdown viewer
_... description of the subcategory ..._

* [modo](nan) [❌ ❌ 🖥️CLI] - A cross platform cli app to interact with markdown style checkboxes within any text file.
* [yek](nan) [❌ ❌ 🖥️CLI] - A fast Rust based tool to serialize text-based files in a repository or directory for LLM consumption.

## 📁 ngrams frequency analyzer
_... description of the subcategory ..._

* [Colibri Core](https://proycon.github.io/colibri-core/) [❌ ❌ 🖥️CLI] - A software to quickly and efficiently count and extract patterns (n-grams and more) from large corpus data, to extract various statistics on the extracted patterns, and to compute relations between the extracted patterns.

## 📁 output formatter
_... description of the subcategory ..._

* [hburger](nan) [❌ ❌ 🖥️CLI] - Shorten long strings and paths while preserving readability.

## 📁 pipeline builder
_... description of the subcategory ..._

* [Ultimate Plumber](nan) [❌ ❌ 🖥️TUI] - Helps to interactively and incrementally explore textual data in Linux, by making it easier to quickly build complex pipelines, thanks to a fast feedback loop.

## 📁 scraping
_... description of the subcategory ..._

* [JsonGenius](nan) [❌ 🌐 🖥️CLI] - Self-hosted scraping API that extracts structured data described by a JSON Schema.

## 📁 spell checker
_... description of the subcategory ..._

* [neospeller](nan) [❌ ❌ 🖥️CLI] - Spell checking for different languages comments.

## 📁 syntax highlighting
_... description of the subcategory ..._

* [grc](nan) [❌ ❌ 🖥️CLI] - (Generic Colourizer) - parse a given text stream and to colorize it according to regexp written in configuration files; different patterns can be associated to file types.

## 📁 system info tools
_... description of the subcategory ..._

* [fullname-cli](nan) [❌ ❌ 🖥️CLI] - Get the fullname of the current user.

## 📁 terminal dashboard
_... description of the subcategory ..._

* [squeeze](nan) [❌ ❌ 🖥️CLI] - Enables to extract rich information from any text (raw, JSON, HTML, YAML, etc).
* [toolong](nan) [❌ ❌ 🖥️TUI] - A terminal application to view, tail, merge, and search log files (plus JSONL).

## 📁 text formatter
_... description of the subcategory ..._

* [grits](nan) [❌ ❌ 🖥️CLI] - A simple line-text formatter that makes it simple to parse, filter, and format live logs turning noise into meaningful insights.
* [Output as Format ](nan) [❌ ❌ 🖥️CLI] - Output stdin as GitHub/Slack/Jira etc... formatted code, lists, or quotes.

## 📁 text processing
_... description of the subcategory ..._

* [awk](nan) [❌ ❌ 🖥️CLI] - A historical, general-purpose text file processor, implements a domain-specific language designed for text processing and typically used as a data extraction and reporting tool.

## 📁 text sampler
_... description of the subcategory ..._

* [ssam](nan) [❌ ❌ 🖥️CLI] - Ssam, short for split sampler, splits one or more text-based input files into multiple sets using random sampling. This is useful for splitting data into a training, test and development sets.

## 📁 text tokenizer
_... description of the subcategory ..._

* [ucto](https://languagemachines.github.io/ucto/) [❌ ❌ 🖥️CLI] - Ucto tokenizes text files: it separates words from punctuation, and splits sentences. It has rules (regular-expression based) for several languages.

## 📁 text transformers
_... description of the subcategory ..._

* [to-double-quotes](nan) [❌ ❌ 🖥️CLI] - Convert matching single-quotes to double-quotes.
* [to-single-quotes](nan) [❌ ❌ 🖥️CLI] - Convert matching double-quotes to single-quotes.

## 📁 url parser
_... description of the subcategory ..._

* [trurl](nan) [❌ ❌ 🖥️CLI] - Command line tool for URL parsing and manipulation.

## 📁 vpn tools
_... description of the subcategory ..._

* [wg-cmd](nan) [❌ ❌ 🖥️TUI] - TUI for managing WireGuard configuration files.

# text-search
[Back to TOC](#📚-contents)

Search files and exploring directory trees to look for text or patterns (RegEx) contained in files; alternatives to the `grep` command
## 📁 AdvancedGrepCLI
_... description of the subcategory ..._

* [ripgrep](nan) [❌ ❌ 🖥️CLI] - Recursively searches directories for a regex pattern.
* [ripgrep-all](nan) [❌ ❌ 🖥️CLI] - grep in text files but also search in PDFs, E-Books, office documents, zip, tar.gz, etc.

## 📁 FastFindAlternative
_... description of the subcategory ..._

* [vgrep](nan) [❌ ❌ 🖥️CLI] - User-friendly pager for grep.

## 📁 advanced grep
_... description of the subcategory ..._

* [paragrep](http://software.clapper.org/paragrep/) [❌ ❌ 🖥️CLI] - Greps regular expressions in a text file(s) and prints out the paragraphs containing those expressions, a paragraph is defined as a block of text delimited by an empty or blank line, fully customizable via command line parameters.
* [sift](https://sift-tool.org/) [❌ ❌ 🖥️CLI] - Fast and powerful alternative to `grep`; it targets flexibility and performance: can be as fast as `grep` and allows specifying complex expressions to find text.

## 📁 code analysis
_... description of the subcategory ..._

* [ast-grep](nan) [❌ ❌ 🖥️CLI] - A CLI tool for code structural search, lint and rewriting.

## 📁 code search
_... description of the subcategory ..._

* [ack](http://beyondgrep.com/) [❌ ❌ 🖥️CLI] - A tool like `grep` optimized for programmers; written in Perl, it speeds up searches thanks to skipping non-interesting directories, such as `.git`.
* [ag](nan) [❌ ❌ 🖥️CLI] - (The silver searcher) - a text search utility targeted to source code; it skips versioning systems data directories; it is inspired by `ack`, but faster.

## 📁 file search
_... description of the subcategory ..._

* [zfind](nan) [❌ ❌ 🖥️TUI] - Search for files (even inside tar/zip/7z/rar) using a SQL-WHERE filter.

## 📁 interactive-line-select
_... description of the subcategory ..._

* [ugrep](nan) [❌ ❌ 🖥️TUI] - Ultra fast grep with interactive TUI, fuzzy search, boolean queries, hexdumps and more.

## 📁 natural language
_... description of the subcategory ..._

* [hae](nan) [🤖 ❌ 🖥️CLI] - Like grep but with natural language queries; useful to retrieve paragraphs of text that deal with specific topics.

## 📁 search tool
_... description of the subcategory ..._

* [bookworm](nan) [🤖 🌐 🖥️CLI] - LLM-powered bookmark search engine.

## 📁 semantic text search
_... description of the subcategory ..._

* [semantic-grep](nan) [🤖 🌐 🖥️CLI] - grep for words with similar meaning to the query.

## 📁 text search
_... description of the subcategory ..._

* [hypergrep](nan) [❌ ❌ 🖥️CLI] - Recursively search directories for a regex pattern using Intel Hypescan.
* [krep](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Blazingly fast text search tool with multiple algorithms (Boyer-Moore, KMP, Rabin-Karp), SIMD acceleration, multi-threading, and regex support. Outperforms traditional tools with memory-mapped I/O and hardware optimizations for who need rapid pattern matching at scale.

# text-search-replace
[Back to TOC](#📚-contents)

Tools to search text within files and perform operations on it, such as text replacement; alternatives to `sed`
## 📁 CodeReplaceCLI
_... description of the subcategory ..._

* [amber](nan) [❌ ❌ 🖥️CLI] - Code search / replace tool.

## 📁 code refactoring
_... description of the subcategory ..._

* [srgn](nan) [❌ ❌ 🖥️CLI] - A code surgeon for precise text and code transplantation. A marriage of `tr`/`sed`, `rg` and `tree-sitter`.

## 📁 enhanced cat
_... description of the subcategory ..._

* [sd](nan) [❌ ❌ 🖥️CLI] - s[earch] & d[isplace] - An intuitive find & replace CLI a possible replacement for sed.

## 📁 search tools
_... description of the subcategory ..._

* [Rep](nan) [❌ ❌ 🖥️CLI] - Rep is a command-line utility that takes grep-formatted lines via standard input, and performs a find-and-replace on them.

## 📁 tabular-sql-query
_... description of the subcategory ..._

* [teip](nan) [❌ ❌ 🖥️CLI] - Select partial standard input and replace with the result of another command.

## 📁 text replace
_... description of the subcategory ..._

* [repgrep](nan) [❌ ❌ 🖥️CLI] - A replacer that uses ripgrep for finding and provides an interactive interface to replace the text.

# time-tracker
[Back to TOC](#📚-contents)

Time and habit trackers to measure the amount of time spent on different activities
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [habitctl](nan) [❌ ❌ 🖥️CLI] - Minimalist command line tool you can use to track and examine your habits.

## 📁 HabitTrackerTUI
_... description of the subcategory ..._

* [dijo](nan) [❌ ❌ 🖥️TUI] - Scriptable, curses-based, digital habit tracker.

## 📁 TimeTrackerCLI
_... description of the subcategory ..._

* [Bartib](nan) [❌ ❌ 🖥️CLI] - Easy to use time tracking tool for the command line. It saves a log of all tracked activities as a plain-text file and allows you to create flexible reports.

## 📁 automatic time tracker
_... description of the subcategory ..._

* [arbtt](http://arbtt.nomeata.de/) [❌ ❌ 🖥️CLI] - (automatic, rule-based time tracker) runs in the background, collecting information regarding open windows, focused ones, etc.; it can be configured to display statistics on the collected data, e.g., figuring out the time spent on one specific window.

## 📁 command-line translator
_... description of the subcategory ..._

* [hours](nan) [❌ ❌ 🖥️TUI] - A no-frills time tracking toolkit for command line nerds.

## 📁 enhanced cat
_... description of the subcategory ..._

* [Watson](nan) [❌ ❌ 🖥️CLI] - Time tracking CLI to know how much time you are spending on your projects. It can generate nice reports for clients.

## 📁 habit tracker
_... description of the subcategory ..._

* [cations](nan) [❌ ❌ 🖥️TUI] - Lightweight, user-friendly habit tracker and productivity tool; terminal-based CLI application.
* [yacht](nan) [❌ ❌ 🖥️TUI] - Yet another command line habit tracker written in Rust.

## 📁 habit trackers
_... description of the subcategory ..._

* [habitmap](nan) [❌ ❌ 🖥️CLI] - A command-line app to track your habits and visualise how committed you are to making or maintaining them with colorful heatmaps.

## 📁 load monitor
_... description of the subcategory ..._

* [Timewarrior](nan) [❌ ❌ 🖥️CLI] - A time tracking utility that offers simple stopwatch features as well as sophisticated calendar-based backfill, along with flexible reporting.

## 📁 pomodoro
_... description of the subcategory ..._

* [pom](nan) [❌ ❌ 🖥️TUI] - Pomodoro timer for the terminal.
* [Productivity Timer](nan) [❌ ❌ 🖥️TUI] - A CLI/TUI Pomodoro timer and todo (coming soon) application for keyboard addicts and terminal fans that makes you more productive.
* [tmux-pomodoro-plus](nan) [❌ ❌ 🖥️TUI] - Pomodoro technique into your tmux workflow

## 📁 pomodoro tracker
_... description of the subcategory ..._

* [aimssh](nan) [❌ ❌ 🖥️TUI] - SSH Pomodoro app.

## 📁 productivity
_... description of the subcategory ..._

* [Timer-CLI](nan) [❌ ❌ 🖥️CLI] - A very simple countdown timer.

## 📁 time trackers
_... description of the subcategory ..._

* [Timetrap](nan) [❌ ❌ 🖥️CLI] - A simple command line time tracker written in Ruby. It provides an easy-to-use command line interface for tracking what you spend your time on.
* [utt](nan) [❌ ❌ 🖥️CLI] - Ultimate Time Tracker - A simple command-line time tracker written in Python.

## 📁 time tracking
_... description of the subcategory ..._

* [doing](nan) [❌ ❌ 🖥️CLI] - A command line tool for remembering what you were doing and tracking what you've done.
* [Moro](nan) [❌ ❌ 🖥️CLI] - A command line tool for tracking work hours, as simple as it can get.
* [zeit](nan) [❌ ❌ 🖥️CLI] - A command line tool for tracking time spent on activities.

## 📁 time-tracker
_... description of the subcategory ..._

* [tim:r](nan) [❌ ❌ 🖥️TUI] - A TUI for organizing your time: Pomodoro Countdown counter.
* [Timet](https://frankvielma.github.io/posts/timet-a-powerful-command-line-tool-for-tracking-your-time/) [❌ ❌ 🖥️CLI] - A lightweight, local time tracker with SQLite storage, offering features like Pomodoro integration, block time and tag distribution plots, detailed statistics, and CSV/iCalendar export.

## 📁 timers
_... description of the subcategory ..._

* [MyTimer](nan) [❌ ❌ 🖥️CLI] - Simple timer for the terminal with timer-mode and alarm.

# todo-manager
[Back to TOC](#📚-contents)

Todo list and task managers
## 📁 ForensicsCLI
_... description of the subcategory ..._

* [tsk](nan) [❌ ❌ 🖥️CLI] - Terminal task management app with an emphasis on simplicity, efficiency and ease of use.

## 📁 GitBackedTodoCLI
_... description of the subcategory ..._

* [dstask](nan) [❌ ❌ 🖥️CLI] - Single binary terminal-based TODO manager with git-based sync + Markdown notes per task.

## 📁 TaskManagerCLI
_... description of the subcategory ..._

* [devtodo](https://swapoff.org/devtodo.html) [❌ ❌ 🖥️CLI] - A hierarchical command-line task manager, with data storage in JSON format.
* [topydo](nan) [❌ ❌ 🖥️CLI] - A powerful todo list application for the console, using the todo.txt format.
* [Ultralist](https://ultralist.io/) [❌ ❌ 🖥️CLI] - A simple, powerful, open source task management system for the command line.

## 📁 TodoListTUI
_... description of the subcategory ..._

* [todotxt-machine](https://pypi.org/project/todotxt-machine/) [❌ ❌ 🖥️TUI] - Interface for todo.txt.

## 📁 TwitterClientCLI
_... description of the subcategory ..._

* [t](nan) [❌ 🌐 🖥️CLI] - A command-line todo list manager for people that want to finish tasks, not organize them.

## 📁 command-line translator
_... description of the subcategory ..._

* [CLI-Manager](nan) [❌ ❌ 🖥️CLI] - Command Line Interface for managing tasks locally on the fly.
* [taskbook](nan) [❌ ❌ 🖥️CLI] - Tasks, boards & notes for the command-line habitat.

## 📁 feature-rich todo manager
_... description of the subcategory ..._

* [TaskWarrior](https://taskwarrior.org/) [❌ ❌ 🖥️CLI 🖥️TUI] - Todo manager with advanced features, dedicated synchronization server available, many plugins and related tools, healthy software project.

## 📁 hierarchical todo manager
_... description of the subcategory ..._

* [TuDu](https://code.meskio.net/tudu/) [❌ ❌ 🖥️TUI] - Manage hierarchical todos. Each task has a title, a long text description, a deadline (tudu warns you when the date is close), and a scheduled date. There are categories and priorities.

## 📁 interactive todo.txt
_... description of the subcategory ..._

* [todo.txt-more](nan) [❌ ❌ 🖥️CLI] - Extensions for todo.txt: interactive rofi/fzf control, sync github issues, better colors, time tracking... and more!

## 📁 kanban
_... description of the subcategory ..._

* [boards](nan) [❌ ❌ 🖥️CLI] - Recursive kanban boards based around the filesystem.
* [kabmat](nan) [❌ ❌ 🖥️TUI] - TUI program for managing kanban boards with vim-like keybindings.

## 📁 knowledge base
_... description of the subcategory ..._

* [grit](nan) [❌ ❌ 🖥️CLI] - A multitree-based personal task manager.
* [omm](nan) [❌ ❌ 🖥️TUI] - "on-my-mind" is a keyboard-driven task manager for the command line.
* [taskell](nan) [❌ ❌ 🖥️TUI] - Interactive kanban board/task manager.

## 📁 note-taking
_... description of the subcategory ..._

* [memo](https://www.byteptr.com/memo/) [❌ ❌ 🖥️CLI] - Memo is a Unix-style note-taking software for POSIX compatible systems.

## 📁 plain-text todo manager
_... description of the subcategory ..._

* [todo.txt](http://todotxt.org/) [❌ ❌ 🖥️CLI] - Minimalistic todo manager that uses a simple plain text file to keep track of items, implemented as a shell script.

## 📁 project-based todo manager
_... description of the subcategory ..._

* [Yokadi](https://yokadi.github.io/) [❌ ❌ 🖥️CLI] - Project-based todo manager: every task must be specified with a mandatory project indication. Tasks are stored within a SQLlite DB. Written in Python.

## 📁 python todo manager
_... description of the subcategory ..._

* [iKog](https://sites.google.com/site/henspace/ikog/) [❌ ❌ 🖥️CLI] - A fully-featured task manager encapsulated within a Python script (just carry around the script to retain all the TODOs). When the script is run, a Python shell is opened, where task-related commands can be entered (ADD, LIST, etc.); a pity that commands are uppercase, which requires the annoying use of the Shift key.

## 📁 shell history
_... description of the subcategory ..._

* [Redo.vc](https://redo.vc) [❌ ❌ 🖥️CLI] - Redo.vc is a tool for command line fans that allows you to track your tasks. It is a full-featured todo manager with tagging, projects, recurring tasks and much more, all stored in a JSON file so it is super portable and tooling new apps for the data format is super easy.

## 📁 task manager
_... description of the subcategory ..._

* [kanban-python](nan) [❌ ❌ 🖥️TUI] - Kanban Terminal App written in Python.
* [taskwarrior-tui](nan) [❌ ❌ 🖥️TUI] - A terminal user interface for taskwarrior.

## 📁 terminal sharing
_... description of the subcategory ..._

* [mdt](nan) [❌ ❌ 🖥️TUI] - A simple command-line Markdown todo list manager inspired by t.

## 📁 text calendar
_... description of the subcategory ..._

* [xit](nan) [❌ ❌ 🖥️CLI] - A plain-text file format for todos and check lists. So, not really a program, but I believe it is worth to list :-)

## 📁 todo manager
_... description of the subcategory ..._

* [cursedtodo](nan) [❌ ❌ 🖥️TUI] - A minimalist, terminal base todo manager storing tasks as .ics files for storage.
* [Dooit](nan) [❌ ❌ 🖥️TUI] - Todo manager with interactive and beautiful UI, and vim keybindings.
* [geek-life](nan) [❌ ❌ 🖥️TUI] - A full-featured TUI task manager.
* [mayhem](nan) [❌ ❌ 🖥️TUI] - A minimal TUI based task tracker.
* [td](nan) [❌ ❌ 🖥️TUI] - Simple & elegant To Do list manager written In Bash.
* [Todoman](nan) [❌ ❌ 🖥️CLI] - A simple, standards-based, CLI todo (aka: task) manager.

## 📁 todo managers
_... description of the subcategory ..._

* [td-cli](nan) [❌ ❌ 🖥️CLI] - A command line todo manager, where you can organize and manage your todos across multiple projects.

## 📁 todoist client
_... description of the subcategory ..._

* [todoclist](nan) [❌ ❌ 🖥️TUI] - Simple CLI app for check your tasks from todoist.

## 📁 wishlist
_... description of the subcategory ..._

* [wish](nan) [❌ ❌ 🖥️TUI] - A delightful wish list manager to keep track of your dreams and desires!

# torrent
[Back to TOC](#📚-contents)

Clients and download managers using the BitTorrent protocol
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [Transmission](https://transmissionbt.com/) [❌ 🌐 🖥️CLI] - Fast, easy and free BitTorrent client.

## 📁 RPGClientTUI
_... description of the subcategory ..._

* [Transgression TUI](nan) [❌ ❌ 🖥️TUI] - A remote TUI client for the Transmission BitTorrent program.

## 📁 TUIBitTorrentClient
_... description of the subcategory ..._

* [rtorrent](nan) [❌ 🌐 🖥️TUI] - BitTorrent client uses ncurses and is ideal for use with tmux, screen or dtach.

## 📁 TorrentClient
_... description of the subcategory ..._

* [Deluge](http://deluge-torrent.org/) [❌ 🌐 🖥️CLI 🖥️TUI] - A lightweight, Free Software, cross-platform BitTorrent client; a terminal curses interface, web interface and command line client can connect to a running daemon to manage torrent downloads.

## 📁 TorrentClientCLI
_... description of the subcategory ..._

* [torrentCLI](nan) [❌ 🌐 🖥️CLI] - Get torrents from the Terminal.

## 📁 TorrentClientTUI
_... description of the subcategory ..._

* [Stig](nan) [❌ 🌐 🖥️TUI] - Stig is a client application to connect and control the BitTorrent Transmission client app.

## 📁 terminal sharing
_... description of the subcategory ..._

* [Mabel](nan) [❌ 🌐 🖥️TUI] - A fancy BitTorrent client for the terminal built with Go and the Bubbletea library.

## 📁 torrent streamer
_... description of the subcategory ..._

* [toru](nan) [❌ 🌐 🖥️CLI] - BitTorrent streaming CLI tool to stream anime torrents in real-time with no waiting for downloads.

# transfer
[Back to TOC](#📚-contents)

Programs for transferring files and data between different machines
## 📁 ClipboardManagerCLI
_... description of the subcategory ..._

* [shcopy](nan) [❌ ❌ 🖥️CLI] - Copy text to your system clipboard locally and remotely using ANSI OSC52 sequence.

## 📁 CloudFileDownloaderCLI
_... description of the subcategory ..._

* [Nextcloud share URL downloader](nan) [❌ 🌐 🖥️CLI] - Download files from and list content of NextCloud (password protected) share directly from the command line without needing a web browser.

## 📁 CloudSyncManager
_... description of the subcategory ..._

* [rclone](https://rclone.org/) [❌ 🌐 🖥️CLI] - Manage file synchronization on cloud storage.

## 📁 DownloadManagerCLI
_... description of the subcategory ..._

* [aria2](nan) [❌ 🌐 🖥️CLI] - Lightweight and easy-to-use download utility; it supports HTTP/HTTPS, FTP, SFTP, BitTorrent, Metalink and multiple sources; cross-platform.

## 📁 FTPClient
_... description of the subcategory ..._

* [stftp](http://stftp.sourceforge.net/) [❌ 🌐 🖥️CLI] - (simple terminal FTP) aims to be an "easy-to-use and unbloated client for the UNIX (and UNIX-like) console".

## 📁 FileSharingCLI
_... description of the subcategory ..._

* [sharing](nan) [❌ 🌐 🖥️CLI] - Sharing is a command-line tool to share directories and files from the CLI to iOS and Android devices without the need of an extra client app.

## 📁 FileSharingOverTor
_... description of the subcategory ..._

* [OnionShare](https://onionshare.org/) [❌ 🌐 🖥️CLI] - "An open source tool that lets you securely and anonymously share a file of any size." 

## 📁 FileSynchronizer
_... description of the subcategory ..._

* [Unison](https://www.cis.upenn.edu/~bcpierce/unison/) [❌ ❌ 🖥️CLI] - File synchronizer. It allows two replicas of a collection of files and directories to be stored on different hosts (or different disks on the same host), modified separately, and then brought up to date by propagating the changes in each replica to the other.

## 📁 FileTransferCLI
_... description of the subcategory ..._

* [croc](nan) [❌ ❌ 🖥️CLI] - Easily and securely send things from one computer to another.
* [lftp](https://lftp.yar.ru/) [❌ 🌐 🖥️CLI] - "Sophisticated FTP/HTTP client, and a file transfer program supporting a number of network protocols"; support for bookmarks and mirroring features.
* [Magic Wormhole](nan) [❌ 🌐 🖥️CLI] - The program allows transfer arbitrary-sized files and directories (or short pieces of text) from one computer to another The two endpoints are identified by using identical human-readable codes.
* [qrcp](https://www.linuxuprising.com/2020/07/qrcp-transfer-files-between-desktop-and.html) [❌ ❌ 🖥️CLI] - Transfer Files Between Desktop And Mobile Devices Over Wi-Fi By Scanning A QR Code.

## 📁 FileTransferP2PCLI
_... description of the subcategory ..._

* [portal](nan) [❌ 🌐 🖥️CLI] - A quick and easy command-line file transfer utility from any computer to another.

## 📁 HTTPIEAlternative
_... description of the subcategory ..._

* [xh](nan) [❌ 🌐 🖥️CLI] - xh is a friendly and fast tool for sending HTTP requests. It reimplements as much as possible of HTTPie's excellent design.

## 📁 LocalHTTPFileServer
_... description of the subcategory ..._

* [Woof](http://www.home.unix-ag.org/simon/woof.html) [❌ 🌐 🖥️CLI] - (Web Offer One File) sets up an HTTP webserver to serve files from a given local directory all the users connected to the network can see and download the files.

## 📁 NetworkDataFetcherCLI
_... description of the subcategory ..._

* [curl](https://curl.haxx.se/) [❌ ❌ 🖥️CLI] - A tool and library for transferring data with URL syntax, supports a lot of protocols.

## 📁 ShellSyncBackup
_... description of the subcategory ..._

* [rsync](https://download.samba.org/pub/rsync/rsync.html) [❌ ❌ 🖥️CLI] - A tool that mirrors directories across networked machines, handling changes to files, working across SSH, with plenty of parameters for configuration.

## 📁 SiteSyncOverFTP
_... description of the subcategory ..._

* [sitecopy](http://www.manyfish.co.uk/sitecopy/) [❌ 🌐 🖥️CLI] - Synchronizes a local copy of a website with a remote copy on a server, does not use SSH/`scp` but FTP for file copy, useful when the remote server does not support secure copy.

## 📁 TranslatorCLI
_... description of the subcategory ..._

* [tran](nan) [❌ 🌐 🖥️CLI] - Securely transfer and send anything between computers with TUI.

## 📁 VideoDownloaderCLI
_... description of the subcategory ..._

* [youtube-dl](nan) [❌ 🌐 🖥️CLI] - Downloads videos from [YouTube](https://www.youtube.com/) and some other sites useful for automated bulk downloads.

## 📁 YouTubeSearchPlayerCLI
_... description of the subcategory ..._

* [ytfzf](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A POSIX script that helps you find YouTube videos (without API) and opens/downloads them using mpv/youtube-dl.

## 📁 YouTubeToMP3Downloader
_... description of the subcategory ..._

* [ytmdl](nan) [❌ 🌐 🖥️CLI] - Get songs from YouTube in mp3 format.

## 📁 clipboard sync
_... description of the subcategory ..._

* [Clipsync](nan) [❌ ❌ 🖥️CLI] - Share your clipboard across multiple machines using an MQTT service.
* [pbproxy](nan) [❌ ❌ 🖥️CLI] - Send your clipboard anywhere you can ssh to.

## 📁 code sharing
_... description of the subcategory ..._

* [shbin](nan) [❌ 🌐 🖥️CLI] - Upload code snippets, notebooks, images or any other content to a GitHub repository that acts as your internal pastebin, and returns the URL to share it with your team.

## 📁 downloader
_... description of the subcategory ..._

* [downloader-cli](nan) [❌ 🌐 🖥️CLI] - A simple downloader written in Python with an awesome customizable progress bar.

## 📁 enhanced cat
_... description of the subcategory ..._

* [pbgopy](nan) [❌ 🌐 🖥️CLI] - Copy and paste between devices.

## 📁 file sharing
_... description of the subcategory ..._

* [ffsend](nan) [❌ 🌐 🖥️CLI] - Easily and securely share files from the command line. A fully featured Firefox Send client.
* [tshare](nan) [❌ 🌐 🖥️CLI] - The fastest way to share your files on the web, for free.
* [zrok](nan) [❌ 🌐 🖥️CLI] - Geo-scale, next-generation peer-to-peer sharing platform built on top of OpenZiti.

## 📁 file sharing tool
_... description of the subcategory ..._

* [Froop](nan) [❌ 🌐 🖥️CLI] - Share file across network seamlessly and securely.

## 📁 file sync
_... description of the subcategory ..._

* [osync](http://www.netpower.fr/osync) [❌ ❌ 🖥️CLI] - A robust two-way (bidirectional) file sync script based on rsync with fault tolerance, POSIX ACL support, time control and near real-time sync.

## 📁 github file downloader
_... description of the subcategory ..._

* [github-dlr](nan) [❌ 🌐 🖥️CLI] - Download individual files and folders from Github recursively.

## 📁 knowledge base
_... description of the subcategory ..._

* [Jitter](nan) [❌ 🌐 🖥️CLI] - A repository-oriented binary manager for Linux, Jitter searches through online repository (currently only on GitHub) for releases with .tar.gz, .tgz, .zip or .AppImage assets.

## 📁 media downloader
_... description of the subcategory ..._

* [gallery-dl](nan) [❌ 🌐 🖥️CLI] - Gallery-dl is a command-line program to download image galleries and collections from several image hosting sites.

## 📁 rclone frontend
_... description of the subcategory ..._

* [rclone-tui](nan) [❌ 🌐 🖥️TUI] - Cross-platform manager for rclone, which aims to be on-par with the web GUI.

## 📁 rss tools
_... description of the subcategory ..._

* [newsboat_video_downloader](nan) [❌ 🌐 🖥️CLI] - Downloads content from YouTube and have them sorted into different folders depending on the channel.

## 📁 scp alternative
_... description of the subcategory ..._

* [smartscp](nan) [❌ ❌ 🖥️CLI] - A replacement of scp, but auto skip git-ignored files; it's just a wrapper of sshfs and xcp.

## 📁 shell
_... description of the subcategory ..._

* [curlie](nan) [❌ 🌐 🖥️CLI] - The power of curl, the ease of use of httpie.

## 📁 telegram tools
_... description of the subcategory ..._

* [tdl](nan) [❌ ❌ 🖥️CLI] - Beautiful and feature-rich Telegram downloader, written in Go.

## 📁 terminal sharing
_... description of the subcategory ..._

* [qr-filetransfer](nan) [❌ 🌐 🖥️CLI] - Transfer files over Wi-Fi between your computer and your smartphone from the terminal.

## 📁 video downloader
_... description of the subcategory ..._

* [lux](nan) [❌ ❌ 🖥️CLI] - Lux is a fast and simple video downloader built with Go.
* [yt-dlp](nan) [❌ 🌐 🖥️CLI] - A youtube-dl fork with additional features and fixes.

## 📁 youtube downloader
_... description of the subcategory ..._

* [Yark](nan) [❌ 🌐 🖥️CLI] - YouTube archiving made simple.

# typing
[Back to TOC](#📚-contents)

Games and utilities to measure and/or improve the typing ability
## 📁 HotkeyManager
_... description of the subcategory ..._

* [kboard](nan) [❌ ❌ 🖥️CLI] - Terminal game to practice keyboard typing.

## 📁 TerminalGame(TypingTrainer)
_... description of the subcategory ..._

* [Typespeed](http://typespeed.sourceforge.net/) [❌ ❌ 🖥️TUI] - Type words that are flying by from left to right as fast as you can; features different word sets, e.g., UNIX commands, English words, Non-English words.

## 📁 typing game
_... description of the subcategory ..._

* [neotype](nan) [❌ ❌ 🖥️TUI] - A terminal-based typing game powered by classic ANSI escape codes.
* [typetype](nan) [❌ ❌ 🖥️CLI] - Minimalistic command line typing game.
* [typing-game-cli](nan) [❌ ❌ 🖥️CLI] - Command line game to practice your typing speed.

## 📁 typing practice
_... description of the subcategory ..._

* [fasttyper](nan) [❌ ❌ 🖥️TUI] - Fasttyper is minimalistic typing test based on user provided exercising text.
* [thokr](nan) [❌ ❌ 🖥️TUI] - Sleek typing TUI with visualized results and historical logging.
* [Typon](nan) [❌ ❌ 🖥️TUI] - A multi-featured typing practice tool which can turn any text file into a typing game.

## 📁 typing practice 
_... description of the subcategory ..._

* [toipe](nan) [❌ ❌ 🖥️CLI] - Yet another typing test, but crab flavored.

## 📁 typing speed test
_... description of the subcategory ..._

* [typeinc](nan) [❌ ❌ 🖥️TUI] - An ncurses based terminal typing speed test with different difficulty levels and cool typing UI.

## 📁 typing test
_... description of the subcategory ..._

* [chimp-type](nan) [❌ ❌ 🖥️TUI] - A minimal typing test for terminal written in go.
* [Smassh](nan) [❌ ❌ 🖥️TUI] - A TUI based typing test app inspired by MonkeyType.
* [tt](nan) [❌ ❌ 🖥️TUI] - A terminal based typing test.
* [ttyper](nan) [❌ ❌ 🖥️CLI] - Terminal-based typing test.
* [typist](nan) [❌ ❌ 🖥️CLI] - A stupid simple type test written in pure Bash v5.1+.

## 📁 typing tutor
_... description of the subcategory ..._

* [Typr](nan) [❌ ❌ 🖥️TUI] - `typr` is a Python-based application that utilizes the 'rich' module to provide you with a simple yet satisfying TUI when typing, `typr` is designed to be simple and easy to use.

# utility
[Back to TOC](#📚-contents)

Miscellaneous utilities that are not do not fit in other categories and they are not numerous enough that they do not require a dedicated category
## 📁 ClipboardHelperCLI
_... description of the subcategory ..._

* [yank](nan) [❌ ❌ 🖥️TUI] - Reads input from stdin and display a selection interface that allows a field to be selected and copied to the clipboard.

## 📁 DesktopEntryGenerator
_... description of the subcategory ..._

* [mkdesk](nan) [❌ ❌ 🖥️CLI] - A program/command to create .desktop files (program launchers) using the terminal.

## 📁 alerting
_... description of the subcategory ..._

* [Keep](nan) [❌ ❌ 🖥️CLI] - Simple alerting tool, with declarative syntax and builtin providers.

## 📁 bash learning tool
_... description of the subcategory ..._

* [bashtutor](nan) [❌ ❌ 🖥️TUI] - Easily extendable utility to interactively showcase or teach CLIs, command line tasks, workflows and Bash itself.

## 📁 bash utils
_... description of the subcategory ..._

* [bash-cache](nan) [❌ ❌ 🖥️CLI] - A function memoization / caching library for bash scripts and shells

## 📁 caching
_... description of the subcategory ..._

* [bkt](https://bkt.rs) [❌ ❌ 🖥️CLI] - bkt is a subprocess caching utility that makes it easy to reuse past invocations of slow commands

## 📁 checksum tool
_... description of the subcategory ..._

* [ccsum](nan) [❌ ❌ 🖥️CLI] - Convenient sha256sum (md5sum, sha1sum, and sha512sum) checksum with improved usability.

## 📁 colorizer
_... description of the subcategory ..._

* [sprinkles](nan) [❌ ❌ 🖥️CLI] - Randomly colors input text and outputs it to the terminal.

## 📁 command launcher
_... description of the subcategory ..._

* [Skylab](nan) [❌ ❌ 🖥️TUI] - A text user interface (TUI) tool that displays upcoming space launches in a user-friendly way.

## 📁 command watcher
_... description of the subcategory ..._

* [watch](http://www.linfo.org/watch.html) [❌ ❌ 🖥️CLI] - Periodically runs a command in the console while temporarily clearing the screen content; it makes it easy to check differences between the output of two subsequent commands; it provides "diff" functionality to highlight the changing characters between outputs.

## 📁 config validator
_... description of the subcategory ..._

* [config-file-validator](nan) [❌ ❌ 🖥️CLI] - Cross Platform tool to validate configuration files.

## 📁 developer automation
_... description of the subcategory ..._

* [plzz](nan) [❌ ❌ 🖥️CLI] - A Python CLI to automate daily tasks of both common and advanced users. It allows easily launching common and different types of operations such as creating random files or check hashes.

## 📁 devtools
_... description of the subcategory ..._

* [sizeof](nan) [❌ ❌ 🖥️CLI] - Experimental CLI, written alongside ChatGPT4 and GitHub Copilot.

## 📁 emoji generators
_... description of the subcategory ..._

* [oji](nan) [❌ ❌ 🖥️TUI] - Interactive text emoji creator.

## 📁 enhanced cat
_... description of the subcategory ..._

* [guesswidth](nan) [❌ ❌ 🖥️CLI] - Guess the width output without delimiters in commands that output to the terminal.

## 📁 env manager
_... description of the subcategory ..._

* [envio](nan) [❌ ❌ 🖥️CLI] - Envio is a command-line tool that simplifies the management of environment variables across multiple profiles. It allows users to easily switch between different configurations and apply them to their current environment.

## 📁 file remover
_... description of the subcategory ..._

* [Polykill](nan) [❌ ❌ 🖥️CLI] - Lightweight command line utility for removing dependencies and build artifacts from unused local projects.

## 📁 file utilities
_... description of the subcategory ..._

* [teetail](nan) [❌ ❌ 🖥️CLI] - Like tee, but only the tail goes in the file.

## 📁 fzf tools
_... description of the subcategory ..._

* [fzf-tab-completion](nan) [❌ ❌ 🖥️CLI] - Tab completion using fzf.

## 📁 image recognition
_... description of the subcategory ..._

* [sauce](nan) [🤖 🌐 🖥️CLI 🖥️TUI] - A novelty CLI tool that identifies an anime from an image and yields key data about it.

## 📁 installer
_... description of the subcategory ..._

* [gentoo-install](nan) [❌ ❌ 🖥️CLI] - This project aspires to be your favorite way to install gentoo. It aims to provide a smooth installation experience, both for beginners and experts. You may configure it by using a menuconfig-inspired interface or simply via a config file.

## 📁 language learning
_... description of the subcategory ..._

* [minicloze](nan) [❌ ❌ 🖥️CLI] - Rust-based command-line language-learning game using the Tatoeba database.

## 📁 log generators
_... description of the subcategory ..._

* [flog](nan) [❌ ❌ 🖥️CLI] - A fake log generator for log formats such as apache-common, apache error and RFC3164 syslog.

## 📁 movie info tools
_... description of the subcategory ..._

* [movie](nan) [❌ ❌ 🖥️CLI] - A CLI for getting information about a movie and comparing two movies.

## 📁 performance tools
_... description of the subcategory ..._

* [chet-client](nan) [❌ ❌ 🖥️CLI] - Measure your commands to speed up your development.

## 📁 process monitor
_... description of the subcategory ..._

* [sasqwatch](nan) [❌ ❌ 🖥️TUI] - A modern take on the classic watch command.

## 📁 progress viewer
_... description of the subcategory ..._

* [ProgressLine](nan) [❌ ❌ 🖥️TUI] - Track commands progress in a compact one-line format.

## 📁 regex practice
_... description of the subcategory ..._

* [Python re(gex)? exercises](nan) [❌ ❌ 🖥️TUI] - TUI application intended to help you practice Python regular expressions there are more than 100 exercises covering both the builtin re and third-party regex module.

## 📁 semantic search
_... description of the subcategory ..._

* [sisi](nan) [🤖 ❌ 🖥️CLI] - Semantic image search CLI tool.

## 📁 shell
_... description of the subcategory ..._

* [Various Scripts](nan) [❌ ❌ 🖥️CLI] - Various script, mainly in shell and Perl, to perform tasks such as combining head and tail, or other common tools accessed using fzf.
* [Zsh Angel IQ System](nan) [❌ 🌐 🖥️CLI] - A bunch of intelligent extensions to Zsh, including an in-shell Ctags browser, an extension to Zinit plugin manager and Angel Swiss Knife.

## 📁 shell customization
_... description of the subcategory ..._

* [ps1palette](nan) [❌ ❌ 🖥️CLI] - Streamline Bash PS1 customization through script automation for prompt color coding and .bashrc integration.

## 📁 shell enhancements
_... description of the subcategory ..._

* [Autocomplete](nan) [❌ ❌ 🖥️CLI] - IDE-style autocomplete for your existing terminal & shell.

## 📁 spell checker
_... description of the subcategory ..._

* [pangran](nan) [❌ ❌ 🖥️TUI] - A simple TUI program that checks if you've typed a pangram.

## 📁 stock tracker
_... description of the subcategory ..._

* [tickrs](nan) [❌ 🌐 🖥️TUI] - Real-time ticker data in your terminal.

## 📁 table generator
_... description of the subcategory ..._

* [tab-pal](nan) [❌ ❌ 🖥️TUI] - A command-line app that makes it easier to add and edit custom colour palettes in Tableau.

## 📁 terminal games
_... description of the subcategory ..._

* [moviemon](nan) [❌ ❌ 🖥️TUI] - A Python program that displays all the information about all your movies in the command line.

## 📁 terminal navigation
_... description of the subcategory ..._

* [tmux-fingers](nan) [❌ ❌ 🖥️CLI] - Copy-pasting in terminal with vimium/vimperator like hints.

## 📁 terminal sharing
_... description of the subcategory ..._

* [volgo](nan) [❌ 🌐 🖥️CLI] - A cross-platform CLI app written in Go for controlling system volume from the terminal. Use simple commands or a beautiful interactive TUI—even over SSH.
* [weather-cli](nan) [❌ ❌ ❌] - Check the weather for your city from the terminal.

## 📁 terminal testing
_... description of the subcategory ..._

* [play](nan) [❌ ❌ 🖥️TUI] - TUI playground for your favorite programs, such as grep, sed and awk.

## 📁 terminal themes
_... description of the subcategory ..._

* [ttyscheme](nan) [❌ ❌ 🖥️TUI] - Collection of Color Schemes for the TTY.

## 📁 unicode tools
_... description of the subcategory ..._

* [glyphs](nan) [❌ ❌ 🖥️CLI] - Unicode symbols on the command line.

## 📁 weather
_... description of the subcategory ..._

* [Aniweather](nan) [❌ 🌐 🖥️TUI] - Aniweather is a simple console weather app featuring cute ASCII art of an anime girl.
* [tempy](nan) [❌ 🌐 🖥️TUI] - A simple, visually pleasing weather report in your terminal.

## 📁 wellness
_... description of the subcategory ..._

* [calm-garden-cli](nan) [❌ ❌ 🖥️TUI] - A small, discreet terminal tool for breath exercises with progression: earn coins, buy plants, and upgrade your garden.

# versioning
[Back to TOC](#📚-contents)

Tools for file versioning that are not related to git
## 📁 AlternativeVCS
_... description of the subcategory ..._

* [Bazaar](http://bazaar.canonical.com/en/) [❌ ❌ 🖥️CLI] - Multiplatform version control system supporting different workflows; it is part of the GNU Project, and it is free software sponsored by Canonical.
* [fossil](https://fossil-scm.org/) [❌ 🌐 🖥️CLI] - A simple, high-reliability, distributed software configuration management system with these advanced features: project management, built-in web interface, friendly self-hosting, simple networking, all-in-one standalone executable, and much more.
* [Mercurial](https://www.mercurial-scm.org/) [❌ ❌ 🖥️CLI] - Free, distributed source control management tool.

## 📁 RepoManagerCLI
_... description of the subcategory ..._

* [gee](nan) [❌ ❌ 🖥️CLI] - CLI repository manager and automation tool written in rust.

## 📁 fossil interface
_... description of the subcategory ..._

* [fnc](https://fnc.bsdbox.org/index) [❌ ❌ 🖥️TUI] - Interactive text-based user interface for Fossil.

## 📁 git manage
_... description of the subcategory ..._

* [myrepo](nan) [❌ ❌ 🖥️CLI] - A repository management tool.

## 📁 git translator
_... description of the subcategory ..._

* [cocommit](nan) [❌ ❌ 🖥️CLI] - Cocommit is a command-line tool that works with your HEAD commit and leverages an LLM of your choice to enhance commit quality.

## 📁 terminal sharing
_... description of the subcategory ..._

* [Gistup](nan) [❌ 🌐 🖥️CLI] - Create a gist from terminal, then use git to update it.

## 📁 version control
_... description of the subcategory ..._

* [Jujutsu](nan) [❌ ❌ 🖥️CLI] - A Git-compatible VCS that is both simple and powerful.

# video
[Back to TOC](#📚-contents)

Programs to process and manage video files (downloader, editing, players, etc.)
## 📁 LightweightAudioPlayer
_... description of the subcategory ..._

* [invidtui](nan) [❌ ❌ 🖥️TUI] - Invidious TUI client, which fetches data from invidious instances and displays a user interface in the terminal, and allows for selecting and playing YouTube audio and video.

## 📁 MediaConverterCLI
_... description of the subcategory ..._

* [ffmpeg](https://ffmpeg.org/) [❌ ❌ 🖥️CLI] - The Swiss knife of video editing from the command line.

## 📁 VideoEditorCLI
_... description of the subcategory ..._

* [Editly](nan) [❌ ❌ 🖥️CLI] - A tool and framework for declarative NLE (non-linear video editing) using Node.js and FFmpeg.

## 📁 YouTubeAudioSplitter
_... description of the subcategory ..._

* [yt-splitter](nan) [❌ 🌐 🖥️CLI] - Downloads and splits audio tracks from a YouTube video according to the chapters/tracks. Useful for compilations or full album uploads.

## 📁 ascii video
_... description of the subcategory ..._

* [lotc](nan) [❌ ❌ 🖥️CLI] - (Lord Of The Clips) Video downloader, trimmer, and merger using the terminal. Supports YouTube, Facebook, Reddit, Twitter, etc. Downloads/trims at multiple points. Merges multiple clips.

## 📁 audio translator
_... description of the subcategory ..._

* [subauto](nan) [🤖 🌐 🖥️CLI] - CLI tool for transcribing, translating, and embedding subtitles in videos using Gemini AI.

## 📁 downloader
_... description of the subcategory ..._

* [Pyutube](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - A simple tool to download YouTube video shorts and playlist in just one click.

## 📁 screen recording
_... description of the subcategory ..._

* [ffscreencast](nan) [❌ ❌ 🖥️CLI] - A FFmpeg screencast with video overlay and multi monitor support.

## 📁 video converter
_... description of the subcategory ..._

* [FFMPerative](nan) [❌ 🌐 🖥️TUI] - Powered by Large Language Models (LLMs) through an intuitive chat interface, now you can compose video edits in natural language.

## 📁 video info
_... description of the subcategory ..._

* [videoinfox](nan) [❌ 🌐 🖥️CLI] - Find videos fast. Powerful playlist building and editing. A play queue to load up unlimited playlists. Index unlimited video libraries and find videos by keyword. Download list building without leaving the browser and a Download Queue.

## 📁 video meme
_... description of the subcategory ..._

* [CreateVideoMeme](nan) [❌ ❌ 🖥️CLI] - Bash tool to add captions to the top of videos.

## 📁 video streaming
_... description of the subcategory ..._

* [Streamlink](nan) [❌ 🌐 🖥️CLI] - Streamlink is a CLI utility which pipes video streams from various services into a video player.

## 📁 youtube browser
_... description of the subcategory ..._

* [YouTube TUI](https://siriusmart.github.io/youtube-tui/) [❌ 🌐 🖥️TUI] - A lightweight and user-friendly TUI for browsing YouTube content from the terminal.

## 📁 youtube client
_... description of the subcategory ..._

* [yt-x](nan) [❌ 🌐 🖥️TUI] - Browse youtube from your terminal, with text-based UI using `fzf` or `rofi` for seamless navigation.

# viewers
[Back to TOC](#📚-contents)

File viewers for images and other formats (e.g., e-books)
## 📁 ImageViewer(ASCII)
_... description of the subcategory ..._

* [cacaview](http://caca.zoy.org/wiki/libcaca) [❌ ❌ 🖥️TUI] - A library and a program to display JPG, PNG, GIF or BMP images in the terminal using ASCII characters.
* [TerminalImageViewer](nan) [❌ ❌ 🖥️CLI] - Small C++ program to display images in a (modern) terminal using RGB ANSI codes and Unicode block graphics characters.

## 📁 MarkdownViewer(GUI/CLI)
_... description of the subcategory ..._

* [ov](nan) [❌ ❌ 🖥️TUI] - Feature-rich terminal-based text viewer.

## 📁 TerminalIPTVPlayer
_... description of the subcategory ..._

* [termv](nan) [❌ 🌐 🖥️TUI] - A terminal IPTV player written in bash.

## 📁 TerminalImageViewer
_... description of the subcategory ..._

* [viu](nan) [❌ ❌ 🖥️CLI] - Command-line application to view images from the terminal written in Rust.

## 📁 VideoAudioPlayer(GUI/CLI)
_... description of the subcategory ..._

* [mplayer](http://www.mplayerhq.hu/design7/news.html) [❌ ❌ 🖥️CLI] - One of the most popular video/audio players around, plays most audio and video formats (using ASCII characters) in the shell, provides a GUI for graphical visualization.
* [mpv](https://mpv.io/) [❌ ❌ 🖥️CLI] - A cross-platform media player with many features such as frame timing, MKV chapters and subtitles. It is a responsive video player with minimal layout customizable with themes. A good alternative media player to VLC since it can handle almost all the media formats as VLC, but using much less resources.

## 📁 YouTubeVideoSearcher
_... description of the subcategory ..._

* [youtube-viewer](nan) [❌ ❌ 🖥️CLI] - Lightweight application that searches and streams videos from YouTube.

## 📁 article readers
_... description of the subcategory ..._

* [medium-cli](nan) [❌ 🌐 🖥️CLI] - Medium for Hackers - Read [medium.com](https://medium.com/) stories in the terminal.

## 📁 audio visualizer
_... description of the subcategory ..._

* [CAVA](nan) [❌ ❌ 🖥️TUI] - Cross-platform Audio Visualizer.

## 📁 cli reader
_... description of the subcategory ..._

* [reader](nan) [❌ 🌐 🖥️TUI] - Reader parses a web page for its actual content and displays it in nicely highlighted text on the command line

## 📁 comic reader
_... description of the subcategory ..._

* [Oyomu](nan) [❌ ❌ 🖥️TUI] - A command line comic reader and collection manager.

## 📁 command-line translator
_... description of the subcategory ..._

* [haxor-news](nan) [❌ 🌐 🖥️CLI] - Browse Hacker News like a haxor: A Hacker News command line interface (CLI).
* [hexyl](nan) [❌ ❌ 🖥️CLI] - Command-line hex viewer.
* [texel](nan) [❌ ❌ 🖥️CLI] - Command line interface for reading spreadsheets inside terminal.
* [ucollage](nan) [❌ ❌ ❌] - An extensible command line image viewer inspired by vim.

## 📁 ebook reader
_... description of the subcategory ..._

* [baca](nan) [❌ ❌ 🖥️TUI] - Lets you indulge in your favorite e-books in the comfort of your terminal.
* [epy](nan) [❌ ❌ 🖥️TUI] - CLI Ebook (epub2, epub3, fb2, mobi) Reader.

## 📁 enhanced cat
_... description of the subcategory ..._

* [bat](nan) [❌ ❌ 🖥️CLI] - A cat clone with syntax highlighting and Git integration.
* [ccat](nan) [❌ ❌ 🖥️CLI] - `cat` with colorized output.

## 📁 github tools
_... description of the subcategory ..._

* [brows](nan) [❌ 🌐 🖥️CLI] - CLI GitHub release browser.

## 📁 interactive tail viewer
_... description of the subcategory ..._

* [btail](nan) [❌ ❌ 🖥️TUI] - Interactive file tail viewer.

## 📁 ipynb viewer
_... description of the subcategory ..._

* [nbcat](https://github.com/akopdev/nbcat) [❌ ❌ 🖥️TUI] - Preview Jupyter notebooks (ipynb) in terminal.

## 📁 jupyter notebook viewer
_... description of the subcategory ..._

* [nbpreview](https://github.com/paw-lu/nbpreview) [❌ ❌ 🖥️TUI] - A terminal viewer for Jupyter notebooks. It's like cat for ipynb files.

## 📁 kafka viewer
_... description of the subcategory ..._

* [kplay](nan) [❌ ❌ 🖥️TUI] - Inspect messages in a Kafka topic in a simple and deliberate manner.

## 📁 markdown viewer
_... description of the subcategory ..._

* [see](nan) [❌ ❌ 🖥️TUI] - A cute cat for the terminal with advanced code viewing, Markdown rendering, tree-sitter syntax highlighting, images view and more.

## 📁 media viewer
_... description of the subcategory ..._

* [timg](nan) [❌ ❌ 🖥️CLI] - A terminal image and video viewer.

## 📁 news reader
_... description of the subcategory ..._

* [bbcli](nan) [❌ 🌐 🖥️CLI] - Browse BBC News like a hacker.
* [hackernews-TUI](nan) [❌ 🌐 🖥️TUI] - A Terminal UI to browse Hacker News.
* [hnterm](nan) [❌ 🌐 🖥️TUI] - Hacker News in the terminal.

## 📁 rss reader
_... description of the subcategory ..._

* [Lob TUI](nan) [❌ 🌐 🖥️TUI] - TUI for lobste.rs website.

## 📁 terminal process viewer
_... description of the subcategory ..._

* [moulti](nan) [❌ ❌ 🖥️CLI 🖥️TUI] - Moulti is a CLI-driven Terminal User Interface (TUI) displaying arbitrary outputs inside visual, collapsible blocks called steps.

## 📁 vcs viewer
_... description of the subcategory ..._

* [krafna](nan) [❌ ❌ 🖥️CLI] - Obsidion dataview plugin-like tool for command line.

## 📁 youtube client
_... description of the subcategory ..._

* [TubiTui](nan) [❌ 🌐 🖥️TUI] - A lightweight, libre, TUI-based YouTube client

# vm
[Back to TOC](#📚-contents)

Tools to manage virtual machines and/or containers and related utilities
## 📁 QEMU UI
_... description of the subcategory ..._

* [nemu](nan) [❌ ❌ 🖥️TUI] - Ncurses UI for QEMU.

## 📁 android emulation
_... description of the subcategory ..._

* [Waydroid](https://waydro.id) [❌ ❌ 🖥️CLI] - A container-based approach to boot a full Android system on a regular Linux distribution.

## 📁 container
_... description of the subcategory ..._

* [bocker](nan) [❌ ❌ 🖥️CLI] - Docker implemented in around 100 lines of bash.
* [ContainerSSH](nan) [❌ 🌐 🖥️CLI] - An SSH Server that Launches Containers in Kubernetes and Docker on demand.
* [docker](https://docs.docker.com/) [❌ 🌐 🖥️CLI] - Self-sufficient runtime for containers.
* [lxc](https://linuxcontainers.org/lxc) [❌ ❌ 🖥️CLI] - A userspace interface for the Linux kernel containment features.
* [podman](https://podman.io/) [❌ 🌐 🖥️CLI] - Podman is a daemonless, open source, Linux native tool designed to make it easy to find, run, build, share and deploy applications using OCI Containers and Container Images.

## 📁 container inspector
_... description of the subcategory ..._

* [dive](nan) [❌ ❌ 🖥️TUI] - A tool for exploring each layer in a docker image.

## 📁 container manager
_... description of the subcategory ..._

* [Incus](https://linuxcontainers.org/lxc) [❌ ❌ 🖥️CLI] - A manager/hypervisor for containers (via LXC) and virtual-machines (via QEMU).
* [ocui](nan) [❌ ❌ 🖥️TUI] - Simple text based UI for managing containers.

## 📁 container tools
_... description of the subcategory ..._

* [distrobox](nan) [❌ ❌ 🖥️CLI] - Use any Linux distribution inside your terminal as docker or podman containers.

## 📁 dev environment
_... description of the subcategory ..._

* [toolbox](https://containertoolbx.org) [❌ ❌ 🖥️CLI] - Use containerized environments where development tools and libraries can be easily installed and used.

## 📁 docker analysis
_... description of the subcategory ..._

* [decompose](nan) [❌ ❌ 🖥️CLI] - Reverse-engineering tool for docker environments.

## 📁 docker management
_... description of the subcategory ..._

* [Dockly](nan) [❌ 🌐 🖥️TUI] - Immersive terminal interface for managing docker containers, services, and images.
* [lazydocker](nan) [❌ 🌐 🖥️TUI] - The lazier way to manage everything docker. A simple terminal UI for both docker and docker-compose, written in Go with the gocui library.

## 📁 docker manager
_... description of the subcategory ..._

* [Pocker](nan) [❌ ❌ 🖥️TUI] - Pocker is a TUI tool to help with docker related tasks, such as view containers/images, manage status of containers, see logs, attributes, environment variables and container statistics, filter logs based on keywords, start shell inside a container.

## 📁 docker tool
_... description of the subcategory ..._

* [oxker](nan) [❌ ❌ 🖥️TUI] - A simple TUI to view & control docker containers.

## 📁 docker tools
_... description of the subcategory ..._

* [docker-shell](nan) [❌ ❌ 🖥️CLI] - A simple interactive prompt for Docker.

## 📁 docker tui
_... description of the subcategory ..._

* [dry](nan) [❌ ❌ 🖥️TUI] - A Docker manager for the terminal.

## 📁 emulator
_... description of the subcategory ..._

* [quickemu](nan) [❌ ❌ 🖥️CLI] - Quickly create and run optimized Windows, macOS and Linux desktop virtual machines.

## 📁 resource monitor
_... description of the subcategory ..._

* [ctop](nan) [❌ ❌ 🖥️TUI] - Top-like interface for container metrics.

## 📁 shell
_... description of the subcategory ..._

* [virsh](https://libvirt.org/index.html) [❌ ❌ 🖥️CLI] - An interactive shell, and batch scriptable tool for performing management tasks on all libvirt managed domains, networks, and storage. A part of the libvirt core distribution.

## 📁 virtualization
_... description of the subcategory ..._

* [QEMU](https://qemu.org) [❌ ❌ 🖥️CLI] - A generic machine & userspace emulator and virtualizer.

# webdev
[Back to TOC](#📚-contents)

Web development tools, including load test tools, API clients and managers, link checkers and extractors, etc.
## 📁 APIClientCLI
_... description of the subcategory ..._

* [http-tanker](nan) [❌ 🌐 🖥️CLI] - Terminal application used for API testing; easily create, manage and execute HTTP requests from the terminal.

## 📁 AlternativeVCS
_... description of the subcategory ..._

* [snallygaster](nan) [❌ 🌐 🖥️CLI] - Tool to scan for secret files on HTTP servers.

## 📁 GitBackedWikiEngine
_... description of the subcategory ..._

* [Mycorrhiza Wiki](https://mycorrhiza.wiki/) [❌ 🌐 🖥️CLI] - A lightweight file-system wiki engine that uses Git for keeping history.

## 📁 LinkCheckerCLI
_... description of the subcategory ..._

* [lychee](nan) [❌ 🌐 🖥️CLI] - Fast, async, resource-friendly link checker written in Rust.

## 📁 LoadTestingTool
_... description of the subcategory ..._

* [Tsung](http://tsung.erlang-projects.org/) [❌ 🌐 🖥️CLI] - A multi-protocol distributed load testing tool that can be used to stress HTTP, WebDAV, SOAP, PostgreSQL, MySQL, LDAP and Jabber/XMPP servers.

## 📁 Network tools
_... description of the subcategory ..._

* [Reachable](nan) [❌ ❌ 🖥️CLI] - Check if a domain is up.

## 📁 ReconToolCLI
_... description of the subcategory ..._

* [urlhunter](nan) [❌ 🌐 🖥️CLI] - Recon tool that allows searching on URLs that are exposed via shortener services.

## 📁 StaticSiteGenerator
_... description of the subcategory ..._

* [Hugo](https://gohugo.io/) [❌ 🌐 🖥️CLI] - The world's fastest framework for building websites.
* [Metalsmith](http://www.metalsmith.io/) [❌ ❌ 🖥️CLI] - An extremely simple static site generator, all functionalities are provided by plugins that can be combined and chained, written and extendable in JavaScript.
* [nanoc](http://nanoc.ws/) [❌ ❌ 🖥️CLI] - Static site generator written in Ruby, extremely powerful and customizable, support many formats to generate HTML content.

## 📁 TextToMorseCLI
_... description of the subcategory ..._

* [iola](nan) [❌ ❌ 🖥️CLI] - A command-line socket client with REST API. It helps to work with socket servers using your favorite REST client.

## 📁 api client
_... description of the subcategory ..._

* [posting](nan) [❌ 🌐 🖥️CLI 🖥️TUI] - The modern API client that lives in your terminal, not unlike Postman and Insomnia.

## 📁 api tool
_... description of the subcategory ..._

* [qwicket](nan) [❌ ❌ 🖥️TUI] - Commandline API development ecosystem.

## 📁 cleanup tools
_... description of the subcategory ..._

* [beachpatrol](nan) [❌ 🌐 🖥️CLI] - A CLI tool to replace and automate your everyday web browser.

## 📁 cloud storage clients
_... description of the subcategory ..._

* [s3cmd](nan) [❌ 🌐 🖥️CLI] - Command line tool for managing Amazon S3 and CloudFront services.

## 📁 deployment tools
_... description of the subcategory ..._

* [Discharge](nan) [❌ 🌐 🖥️CLI] - Deploy static websites to Amazon S3.

## 📁 django tools
_... description of the subcategory ..._

* [django-tui](nan) [❌ ❌ 🖥️TUI] - Inspect and run Django Commands in a text-based user interface (TUI).

## 📁 enhanced cat
_... description of the subcategory ..._

* [linkchecker](nan) [❌ 🌐 🖥️CLI] - Check links in web documents or full websites.

## 📁 file generator
_... description of the subcategory ..._

* [dummy](nan) [❌ ❌ 🖥️CLI] - Generator of static files for testing file upload. It can generate the PNG file of any number of bytes!

## 📁 html/xml tools
_... description of the subcategory ..._

* [xpe](nan) [❌ ❌ 🖥️CLI] - A command-line xpath tool that is easy to use.

## 📁 http clients
_... description of the subcategory ..._

* [HTTPie](nan) [❌ 🌐 🖥️CLI] - HTTPie for Terminal: human-friendly CLI HTTP client for the API era.

## 📁 load testing
_... description of the subcategory ..._

* [Ballast](nan) [❌ ❌ 🖥️CLI] - A simple API load testing tool that lets you compare performance snapshots of your API.
* [maelstrom](nan) [❌ ❌ 🖥️CLI] - stress-test your API reliability on concurrent threads, with latency metrics.

## 📁 pentest suite
_... description of the subcategory ..._

* [kanha](nan) [❌ 🌐 🖥️CLI] - A web-app pentesting suite written in Rust.

## 📁 screenshot tools
_... description of the subcategory ..._

* [pageres-cli](nan) [❌ 🌐 🖥️CLI] - Capture screenshots of websites in various resolutions. A good way to make sure your websites are responsive.

## 📁 shopify dev
_... description of the subcategory ..._

* [Shopify Development Tools](nan) [❌ ❌ 🖥️CLI] - Tools to assist with the development and/or maintenance of Shopify apps and stores.

## 📁 static site deployers
_... description of the subcategory ..._

* [surge](https://surge.sh) [❌ 🌐 🖥️CLI] - Static web publishing on surge.sh CDN.

## 📁 terminal sharing
_... description of the subcategory ..._

* [ain](nan) [❌ 🌐 🖥️CLI] - An HTTP API client for the terminal.

## 📁 uptime checkers
_... description of the subcategory ..._

* [is-up-cli](nan) [❌ 🌐 🖥️CLI] - Check whether a website is up or down using the [isitup.org](https://isitup.org/) API.

## 📁 web crawlers
_... description of the subcategory ..._

* [crawley](nan) [❌ 🌐 🖥️CLI] - Unix-way web crawler: crawls web pages and prints any link it can find.

# writing
[Back to TOC](#📚-contents)

Tools to assist the writing of text and documents, including translation, spell checking, etc.
## 📁 Translation
_... description of the subcategory ..._

* [Translate Shell](https://www.soimort.org/translate-shell/) [❌ 🌐 🖥️CLI] - Translator using Google Translate, Bing Translator, Yandex.Translate, etc.

## 📁 command-line translator
_... description of the subcategory ..._

* [trino](nan) [❌ ❌ 🖥️CLI] - Quick and easy translation of words and phrases entered in the command line.

## 📁 dictionary
_... description of the subcategory ..._

* [gdict](nan) [❌ ❌ 🖥️CLI] - An offline CLI dictionary written in go, using data from wiktionary.
* [rdict](nan) [❌ ❌ 🖥️CLI] - Offline dictionary using data from wiktionary written in Rust.

## 📁 grammar checker
_... description of the subcategory ..._

* [Grammatical](nan) [🤖 ❌ 🖥️CLI] - Corrects the spelling and grammar of your text using ChatGPT.

## 📁 markdown tools
_... description of the subcategory ..._

* [cambd-cli](nan) [❌ ❌ 🖥️CLI] - A CLI tool to automate the process to access the Cambridge dictionary.

## 📁 story generator
_... description of the subcategory ..._

* [storycraftr](nan) [🤖 ❌ 🖥️CLI 🖥️TUI] - StoryCraftr is an open-source AI-powered tool that helps writers craft stories, generate worldbuilding details, and create book outlines and chapters seamlessly through a simple CLI. Empower your creativity with AI.

## 📁 terminal sharing
_... description of the subcategory ..._

* [GTT - Google Translate TUI](nan) [🤖 🌐 🖥️TUI] - A TUI interface to bring Google Translation in the terminal.

## 📁 text linting
_... description of the subcategory ..._

* [alex](nan) [❌ ❌ 🖥️CLI] - Catch insensitive, inconsiderate writing, by finding gender favoring, polarizing, race related, or other unequal phrasing in text.

## 📁 vocabulary builder
_... description of the subcategory ..._

* [VocabCLI](nan) [❌ ❌ 🖥️CLI] - Lightweight CLI that allows users to look up word definitions, examples, synonyms, and antonyms directly via the command line; it also offers advanced Text Classification and Processing via the use of Natural Language Processing and Machine Learning algorithms.

## 📁 writing linter
_... description of the subcategory ..._

* [write good](nan) [❌ ❌ 🖥️CLI] - Naive linter for English prose.



# <a name="resources"></a>Related resources

A list of some online resources that contribute interesting links to apps and info.

[Toolleeo’s CLIpedia](https://robot.unipv.it/clipedia/) - Blog with information on CLI apps, screenshots and other details (license, author, etc.).

[The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) - A wonderful summary from Joshua Levy regarding command line (Bash in particular) tools, programs, tips, and tricks; contains many pointers to resources and repositories, in the form of "to do this you must know that", which gives great pointers but requires further investigation from different sources; translated in many languages.

[Inconsolation blog](https://inconsolation.wordpress.com/) - "Adventures with lightweight and minimalist software for Linux": reviews of many command-line programs; many programs reviewed (400+, at least), with screenshots and animated GIFs; the style of presentation is ironic and funny, but requires some effort to figure out the real contribution of a program.

[A little collection of cool unix terminal/console/curses tools](https://kkovacs.eu/cool-but-obscure-unix-tools) - "Some are little-known, some are just too useful to miss, some are pure obscure..." from Kristof Kovacs; nice list with screenshot; mostly oriented to system administration; unfortunately there are no clickable links.

[Caleb Xu shell awesome](https://github.com/alebcay/awesome-shell) - Focused on UNIX shell tools.

[Adam Harris awesome CLI apps](https://github.com/aharris88/awesome-cli-apps) - Nice list of tools; somehow too much JavaScript/Node.js-centered for my tastes.

[Marcel Bischoff awesome commandd line apps](https://github.com/herrbischoff/awesome-command-line-apps) - Nice up-to-date list of useful tools.

[Awesome CLI by sintaxi](https://github.com/sintaxi/awesome-cli) - Relatively short list with short descriptions; with some original entries.

[awesome-ttygames](https://ligurio.github.io/awesome-ttygames/) - Large awesome list of terminal games. The collection is maintained in a YAML format. Each item contains a description and an optional screencast.

[Site Generators](https://jamstack.org/generators/) - A comprehensive list of Static Site Generators.

[Awesome git addons](https://github.com/stevemao/awesome-git-addons) - A curated list of add-ons that extend/enhance the git CLI.

[Terminals Are Sexy](https://github.com/k4m4/terminals-are-sexy) - A curated list of Terminal frameworks, plugins & resources for CLI lovers.

[Awesome Terminal Recorder](https://github.com/orangekame3/awesome-terminal-recorder) - Curated list of outstanding terminal Recorder that make your day brighter! Each item is associated with an animated GIF that shows some examples of usage.

[commandlinefu.com](https://www.commandlinefu.com/commands/browse) - The place to record those command-line gems that you return to again and again. That way others can gain from your CLI wisdom and you from theirs too.

[cli.club](https://cli.club/) - A collection of the best CLI/ncurses software covering a wide range of categories from messaging, music, text editing and more.

[texteditors.org](https://texteditors.org/cgi-bin/wiki.pl?search=HomePage) - A huge collection of links to resources on text editor. It contains references to non-CLI programs.

[Terminal Trove](https://terminaltrove.com/) - Collection of terminal CLI/TUI programs, with one page per program, nice screenshots and animated GIFs.

[Terminal Directory](https://termui.sh/) - List of all (known) terminals.

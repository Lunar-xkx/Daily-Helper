<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="theme-color" content="#07182f" />
  <title>Tide — Tasks & Focus</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <main class="app-shell">
    <header class="topbar">
      <a class="brand" href="#top" aria-label="Tide home"><span class="brand-mark">✓</span><span>Tide</span></a>
      <p id="today" class="date-label"></p>
      <button class="icon-button" id="theme-toggle" aria-label="Toggle night contrast" title="Toggle night contrast">☼</button>
    </header>

    <section class="welcome" id="top" aria-labelledby="greeting">
      <div>
        <p class="eyebrow">YOUR CALM CORNER</p>
        <h1 id="greeting">Make today count.</h1>
        <p class="subtle">A little progress is still progress. Pick one thing and begin.</p>
      </div>
      <div class="progress-card" aria-label="Daily task progress">
        <span id="progress-text">0 of 0 complete</span>
        <div class="progress-track"><div class="progress-fill" id="progress-fill"></div></div>
      </div>
    </section>

    <div class="dashboard">
      <section class="tasks-panel panel" aria-labelledby="tasks-heading">
        <div class="section-heading">
          <div><p class="eyebrow">TODAY'S LIST</p><h2 id="tasks-heading">Your tasks</h2></div>
          <button class="text-button" id="clear-completed">Clear completed</button>
        </div>
        <form class="add-task" id="task-form">
          <label class="sr-only" for="task-input">Add a task</label>
          <input id="task-input" type="text" maxlength="100" placeholder="What would you like to do?" autocomplete="off" required />
          <button type="submit" aria-label="Add task">Add <span aria-hidden="true">+</span></button>
        </form>
        <div class="filters" role="group" aria-label="Filter tasks">
          <button class="filter active" data-filter="all">All <span id="all-count">0</span></button>
          <button class="filter" data-filter="active">Active <span id="active-count">0</span></button>
          <button class="filter" data-filter="done">Done <span id="done-count">0</span></button>
        </div>
        <ul id="task-list" class="task-list" aria-live="polite"></ul>
        <p id="empty-state" class="empty-state">Your list is clear. Add a gentle next step above.</p>
      </section>

      <aside class="focus-panel panel" aria-labelledby="focus-heading">
        <p class="eyebrow">FOCUS TIME</p>
        <h2 id="focus-heading">Give it your attention.</h2>
        <p class="subtle focus-copy">One focused session at a time. You’ve got this.</p>
        <div class="timer-wrap" role="timer" aria-live="polite" aria-atomic="true">
          <svg class="timer-ring" viewBox="0 0 180 180" aria-hidden="true">
            <circle class="ring-bg" cx="90" cy="90" r="76" />
            <circle class="ring-progress" id="ring-progress" cx="90" cy="90" r="76" />
          </svg>
          <div class="timer-content"><span id="timer-mode">FOCUS</span><strong id="timer-display">25:00</strong></div>
        </div>
        <div class="timer-controls">
          <button class="round-button" id="reset-timer" aria-label="Reset timer">↺</button>
          <button class="start-button" id="start-timer">Start focus</button>
          <button class="round-button" id="skip-timer" aria-label="Skip to next timer mode">⇥</button>
        </div>
        <div class="timer-presets" role="group" aria-label="Timer duration">
          <button data-minutes="25" class="preset active">25 min</button>
          <button data-minutes="15" class="preset">15 min</button>
          <button data-minutes="5" class="preset">5 min</button>
        </div>
        <p class="tip"><span aria-hidden="true">✦</span> Tip: put your phone face down and make this a tiny promise to yourself.</p>
      </aside>
    </div>
  </main>
  <div id="toast" class="toast" role="status" aria-live="polite"></div>
  <script src="app.js"></script>
</body>
</html>

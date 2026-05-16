'use strict';

// ── 状態 ──────────────────────────────────────────
let allWords      = [];
let sessionWords  = [];
let currentIndex  = 0;
let correctCount  = 0;
let currentLevel  = '';
let progress      = {};   // { uuid: { isLearned, reviewCount } }

const PROGRESS_KEY = 'englishword_progress';
const THEME_KEY    = 'englishword_theme';

// ── 初期化 ────────────────────────────────────────
document.addEventListener('DOMContentLoaded', async () => {
  loadTheme();
  progress = loadProgress();
  try {
    const res = await fetch('words.json');
    allWords = await res.json();
  } catch (e) {
    console.error('words.json の読み込みに失敗しました', e);
  }
});

// ── 画面遷移 ──────────────────────────────────────
function showScreen(name) {
  document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
  document.getElementById(`screen-${name}`).classList.add('active');
  window.scrollTo(0, 0);
}

function goHome() {
  showScreen('home');
}

// ── セッション開始 ────────────────────────────────
function startSession(level) {
  currentLevel = level;
  const base = allWords.filter(w => w.level === level);

  if (base.length === 0) {
    alert(`${level} の単語データがありません`);
    return;
  }

  // シャッフルして最大30語に絞る
  const shuffled = [...base].sort(() => Math.random() - 0.5).slice(0, 30);
  sessionWords = shuffled.map(w => ({
    ...w,
    isLearned:   progress[w.id]?.isLearned   ?? false,
    reviewCount: progress[w.id]?.reviewCount ?? 0,
  }));

  currentIndex = 0;
  correctCount = 0;
  showScreen('flashcard');
  document.getElementById('fc-level-title').textContent = level;
  renderCard();
}

function retrySession() {
  startSession(currentLevel);
}

// ── カード描画 ────────────────────────────────────
function renderCard() {
  const word = sessionWords[currentIndex];

  document.getElementById('fc-english').textContent  = word.english;
  document.getElementById('fc-japanese').textContent = word.japanese;

  // 品詞バッジ
  const badge = document.getElementById('fc-pos');
  badge.textContent = word.category;
  badge.className   = 'pos-badge ' + posClass(word.category);

  // 答え非表示に戻す
  document.getElementById('fc-answer-section').classList.add('hidden');
  document.getElementById('fc-action-show').classList.remove('hidden');
  document.getElementById('fc-action-judge').classList.add('hidden');

  updateProgress();
}

function posClass(cat) {
  const map = { '動詞': 'pos-動詞', '名詞': 'pos-名詞', '形容詞': 'pos-形容詞', '副詞': 'pos-副詞' };
  return map[cat] ?? 'pos-default';
}

// ── 答えを見る ────────────────────────────────────
function showAnswer() {
  document.getElementById('fc-answer-section').classList.remove('hidden');
  document.getElementById('fc-action-show').classList.add('hidden');
  document.getElementById('fc-action-judge').classList.remove('hidden');
}

// ── 正解 / 不正解 ──────────────────────────────────
function markCorrect() {
  sessionWords[currentIndex].isLearned   = true;
  sessionWords[currentIndex].reviewCount += 1;
  correctCount++;
  advance();
}

function markIncorrect() {
  sessionWords[currentIndex].reviewCount += 1;
  advance();
}

function advance() {
  saveProgressForSession();
  if (currentIndex + 1 >= sessionWords.length) {
    showResult();
  } else {
    currentIndex++;
    renderCard();
  }
}

// ── 進捗バー ──────────────────────────────────────
function updateProgress() {
  const pct = sessionWords.length === 0
    ? 0
    : (currentIndex / sessionWords.length) * 100;
  document.getElementById('fc-progress').style.width = `${pct}%`;
  document.getElementById('fc-progress-label').textContent =
    `${currentIndex + 1} / ${sessionWords.length}`;
}

// ── 結果画面 ──────────────────────────────────────
function showResult() {
  document.getElementById('result-score').textContent =
    `${correctCount} / ${sessionWords.length} 正解`;
  showScreen('result');
}

// ── 進捗の保存・読み込み ──────────────────────────
function saveProgressForSession() {
  sessionWords.forEach(w => {
    progress[w.id] = { isLearned: w.isLearned, reviewCount: w.reviewCount };
  });
  localStorage.setItem(PROGRESS_KEY, JSON.stringify(progress));
}

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(PROGRESS_KEY)) ?? {};
  } catch { return {}; }
}

// ── テーマ ────────────────────────────────────────
function setTheme(theme) {
  document.body.className = theme;
  localStorage.setItem(THEME_KEY, theme);
  document.getElementById('btn-dark').classList.toggle('active',  theme === 'dark');
  document.getElementById('btn-light').classList.toggle('active', theme === 'light');
}

function loadTheme() {
  const saved = localStorage.getItem(THEME_KEY) ?? 'dark';
  setTheme(saved);
}

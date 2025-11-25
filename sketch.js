// =============================================
//  ASSETS (SEMPRE FUNCIONA - SEM PNGS)
// =============================================
let musica;
let somScore;   // <-- SOM DE COLETAR ORBE
let imgPlayer, imgEnemy;

// =============================================
//  PARTICULAS
// =============================================
class Particula {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.r = random(2, 5);
    this.alpha = 255;
  }
  update() {
    this.x += random(-1, 1);
    this.y += random(-1, 1);
    this.alpha -= 4;
  }
  draw() {
    noStroke();
    fill(0, 200, 255, this.alpha);
    circle(this.x, this.y, this.r);
  }
  acabou() {
    return this.alpha <= 0;
  }
}

// =============================================
//  VARIAVEIS
// =============================================
let playerX, playerY;
let playerSpeed = 4;

let enemyX, enemyY;
let enemySpeed = 1.4;

let energia = 100;
let pontos = 0;

let particulas = [];
let orbes = [];

let tempoDeJogo = 0;
let estado = "menu";
let dificuldade = "normal";

// =============================================
//  RECORDE
// =============================================
let recorde = 0;
if (localStorage.getItem("recordeNeonRescue")) {
  recorde = Number(localStorage.getItem("recordeNeonRescue"));
}

// =============================================
//  PRELOAD
// =============================================
function preload() {

  // ---- SOM BASE ----
  try { musica = loadSound("musica.mp3"); }
  catch(e) { musica = { setVolume:()=>{}, loop:()=>{} }; }

  // ---- SOM DE PEGAR ORBE ----
  try { somScore = loadSound("score.mp3"); }     // <---------
  catch(e) { somScore = { play:()=>{} }; }

  try { imgPlayer = loadImage("jogador.png"); }
  catch(e) {
    imgPlayer = createGraphics(50, 50);
    imgPlayer.fill(0,255,0);
    imgPlayer.circle(25,25,50);
  }

  try { imgEnemy = loadImage("inimigo.png"); }
  catch(e) {
    imgEnemy = createGraphics(60, 60);
    imgEnemy.fill(255,0,0);
    imgEnemy.rect(5,5,50,50,10);
  }
}

// =============================================
//  SETUP
// =============================================
function setup() {
  createCanvas(700, 600);

  playerX = width/2;
  playerY = height/2;

  enemyX = 60;
  enemyY = 60;

  musica.setVolume(0.12);
  musica.loop();
}

// =============================================
//  DRAW
// =============================================
function draw() {
  background(10,12,30);

  desenharParticulasDeFundo();

  if (estado === "menu") return desenharMenu();
  if (estado === "perdeu") return desenharGameOver();

  tempoDeJogo += 0.016;

  aumentarDificuldade();
  atualizarPlayer();
  atualizarEnemy();
  atualizarEnergia();
  atualizarOrbes();
  atualizarParticulas();

  desenharPlayer();
  desenharEnemy();
  desenharOrbes();
  desenharPainel();
}

// =============================================
//  FUNDO
// =============================================
function desenharParticulasDeFundo() {
  noStroke();
  fill(0, 200, 255, 60);

  for (let i = 0; i < 90; i++) {
    let x = noise(i, frameCount * 0.01) * width;
    let y = noise(i * 2, frameCount * 0.01) * height;
    circle(x, y, 2);
  }
}

// =============================================
//  MENU
// =============================================
function desenharMenu() {
  fill(0,200,255);
  textAlign(CENTER);
  textSize(48);
  text("NEON RESCUE", width/2,120);

  textSize(22);
  fill(180);
  text("Fuja do perseguidor e colete orbes!", width/2, 180);
  text("Tente fazer a maior pontuação!", width/2, 210);

  textSize(18);
  fill(0,255,0);
  text("Trabalho feito por Eduardo Dettmer", width/2, 260);

  textSize(26);
  fill(200);
  text("Clique para começar", width/2, 360);
}

function mousePressed() {
  if (estado === "menu") {
    resetarJogo();
    estado = "jogo";
  } else if (estado === "perdeu") {
    estado = "menu";
  }
}

// =============================================
//  RESET
// =============================================
function resetarJogo() {
  energia = 100;
  pontos = 0;
  tempoDeJogo = 0;

  playerX = width/2;
  playerY = height/2;

  enemyX = 60;
  enemyY = 60;

  enemySpeed = 1.4;
}

// =============================================
//  PLAYER
// =============================================
function atualizarPlayer() {
  if (keyIsDown(65)) playerX -= playerSpeed;
  if (keyIsDown(68)) playerX += playerSpeed;
  if (keyIsDown(87)) playerY -= playerSpeed;
  if (keyIsDown(83)) playerY += playerSpeed;

  playerX = constrain(playerX, 20, width-20);
  playerY = constrain(playerY, 20, height-20);

  particulas.push(new Particula(playerX, playerY));
}

function desenharPlayer() {
  image(imgPlayer, playerX-25, playerY-25, 50, 50);
}

// =============================================
//  INIMIGO
// =============================================
function atualizarEnemy() {
  let dx = playerX - enemyX;
  let dy = playerY - enemyY;
  let d = sqrt(dx*dx + dy*dy);

  enemyX += (dx/d) * enemySpeed;
  enemyY += (dy/d) * enemySpeed;

  if (dist(playerX, playerY, enemyX, enemyY) < 35) {
    estado = "perdeu";
  }
}

function desenharEnemy() {
  push();
  translate(enemyX, enemyY);
  rotate(frameCount*0.02);
  image(imgEnemy, -30, -30, 60, 60);
  pop();
}

// =============================================
//  ORBES
// =============================================
function atualizarOrbes() {
  if (orbes.length < 3 && random() < 0.02) {
    orbes.push({ x: random(40,width-40), y: random(40,height-40), r: 20 });
  }
}

function desenharOrbes() {
  for (let i = orbes.length-1; i >= 0; i--) {
    let o = orbes[i];

    fill(0,200,255);
    circle(o.x,o.y,o.r*2);

    if (dist(playerX,playerY,o.x,o.y) < 35) {

      // 🎵 TOCA O SOM AO PEGAR ORBE (ÚNICA MUDANÇA)
      somScore.play();  

      energia = min(100, energia+25);
      pontos += 10;
      orbes.splice(i,1);
    }
  }
}

// =============================================
//  DIFICULDADE
// =============================================
function aumentarDificuldade() {
  enemySpeed += 0.001;
  enemySpeed = min(enemySpeed, 4.5);
}

// =============================================
//  ENERGIA
// =============================================
function atualizarEnergia() {
  energia -= map(tempoDeJogo, 0, 120, 0.18, 0.35);

  if (energia <= 0) estado = "perdeu";
}

// =============================================
//  PARTICULAS
// =============================================
function atualizarParticulas() {
  for (let i = particulas.length-1; i >= 0; i--) {
    particulas[i].update();
    particulas[i].draw();
    if (particulas[i].acabou()) particulas.splice(i,1);
  }
}

// =============================================
//  HUD
// =============================================
function desenharPainel() {
  push();
  textAlign(LEFT, TOP);

  fill(255);
  textSize(22);
  text("Pontos: "+pontos, 20,20);

  fill(0,200,255);
  rect(20, 55, 200, 12, 4);

  fill(255,80,80);
  rect(20, 55, energia*2, 12, 4);

  fill(0,200,255);
  textSize(16);
  text("Velocidade do macaco: "+nf(enemySpeed,1,2), 20, 75);

  pop();
}

// =============================================
//  GAME OVER
// =============================================
function desenharGameOver() {

  if (pontos > recorde) {
    recorde = pontos;
    localStorage.setItem("recordeNeonRescue", recorde);
  }

  background(100,0,0,200);
  textAlign(CENTER);
  fill(255);
  textSize(50);
  text("GAME OVER", width/2,200);

  textSize(28);
  text("Pontuação: " + pontos, width/2, 260);

  fill(255,255,0);
  text("Recorde: " + recorde, width/2, 300);

  textSize(22);
  fill(255);
  text("Clique para voltar", width/2,360);
}

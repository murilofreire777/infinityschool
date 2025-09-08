// ================================
// Arquivo: script.js
// Descrição: Funcionalidades reutilizáveis para páginas de aula.
// Recursos: tema, tamanho da fonte, TOC/scrollspy, copiar código, modal de imagem,
//           colapsar seções, quiz simples, atalho de busca, imprimir PDF.
// ================================

(function(){
  const root = document.documentElement;
  const toc = document.getElementById('toc');
  const readingBar = document.querySelector('.reading-progress span');

  // Preferência de tema
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme === 'light') root.classList.add('light');

  // Tamanho da fonte
  const savedFont = localStorage.getItem('fontSize');
  if (savedFont) root.style.setProperty('--font-size', savedFont);

  // Geração automática do Sumário (TOC)
  const sections = Array.from(document.querySelectorAll('[data-section-title]'));
  const makeId = (t) => t.toLowerCase().replace(/\s+/g,'-').replace(/[^\w\-]/g,'');
  sections.forEach(sec => {
    const title = sec.getAttribute('data-section-title');
    const id = makeId(title);
    sec.id = id;
    const a = document.createElement('a');
    a.href = `#${id}`;
    a.textContent = title;
    toc.appendChild(a);
  });

  // Scrollspy
  const observer = new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      const link = toc.querySelector(`a[href="#${e.target.id}"]`);
      if (!link) return;
      if (e.isIntersecting) {
        toc.querySelectorAll('a').forEach(l=>l.classList.remove('active'));
        link.classList.add('active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px', threshold: 0 });
  sections.forEach(s=>observer.observe(s));

  // Barra de leitura
  window.addEventListener('scroll', ()=>{
    const h = document.documentElement;
    const scrolled = (h.scrollTop)/(h.scrollHeight - h.clientHeight);
    readingBar.style.width = (scrolled*100).toFixed(2)+'%';
  }, {passive:true});

  // Filtro do TOC e atalho Ctrl+/
  const tocSearch = document.getElementById('tocSearch');
  window.addEventListener('keydown', (e)=>{
    if ((e.ctrlKey || e.metaKey) && e.key === '/') {
      e.preventDefault(); tocSearch.focus();
    }
  });
  tocSearch?.addEventListener('input', (e)=>{
    const q = e.target.value.toLowerCase();
    toc.querySelectorAll('a').forEach(a=>{
      a.hidden = !a.textContent.toLowerCase().includes(q);
    });
  });

  // Botões topo
  document.getElementById('btnToggleTheme')?.addEventListener('click', ()=>{
    root.classList.toggle('light');
    localStorage.setItem('theme', root.classList.contains('light') ? 'light':'dark');
  });
  const clampFont = (delta)=>{
    const cur = parseFloat(getComputedStyle(root).getPropertyValue('--font-size')) || 16;
    const next = Math.min(22, Math.max(12, cur + delta));
    root.style.setProperty('--font-size', next+'px');
    localStorage.setItem('fontSize', next+'px');
  };
  document.getElementById('btnIncreaseFont')?.addEventListener('click', ()=>clampFont(1));
  document.getElementById('btnDecreaseFont')?.addEventListener('click', ()=>clampFont(-1));
  document.getElementById('btnPrint')?.addEventListener('click', ()=>window.print());

  // Copiar código
  document.querySelectorAll('.btn-copy').forEach(btn=>{
    btn.addEventListener('click', async ()=>{
      const sel = btn.getAttribute('data-copy-target');
      const el = document.querySelector(sel);
      try { await navigator.clipboard.writeText(el?.innerText || '');
        btn.textContent = 'Copiado!';
        setTimeout(()=>btn.textContent='Copiar', 1200);
      } catch(err){ console.error(err); }
    });
  });

  // Colapsar seções
  document.querySelectorAll('[data-collapse]')?.forEach(btn=>{
    const target = document.querySelector(btn.getAttribute('data-collapse'));
    btn.addEventListener('click', ()=>{
      if (!target) return;
      const isHidden = target.hasAttribute('hidden');
      target.toggleAttribute('hidden', !isHidden);
      btn.textContent = isHidden ? 'Recolher' : 'Expandir';
    });
  });

  // Modal de imagem
  const modal = document.getElementById('imgModal');
  const modalImg = document.getElementById('imgModalSrc');
  const modalCaption = document.getElementById('imgModalCaption');
  document.querySelectorAll('[data-zoomable]')?.forEach(img=>{
    img.addEventListener('click', ()=>{
      modalImg.src = img.src; modalCaption.textContent = img.alt || '';
      modal.showModal();
    });
  });
  modal?.querySelector('[data-close]')?.addEventListener('click', ()=>modal.close());

  // Quiz simples
  const btnCorrigir = document.getElementById('btnCorrigir');
  btnCorrigir?.addEventListener('click', ()=>{
    let acertos = 0, total = 0;
    document.querySelectorAll('[data-quiz] .quiz-item').forEach(item=>{
      total++;
      const checked = item.querySelector('input[type="radio"]:checked');
      const isCorrect = checked && checked.hasAttribute('data-correct');
      item.style.borderColor = isCorrect ? 'var(--success)' : 'var(--danger)';
      if (isCorrect) acertos++;
    });
    const out = document.getElementById('quizResultado');
    out.textContent = `Resultado: ${acertos}/${total}`;
  });
})();

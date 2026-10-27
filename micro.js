const form = document.getElementById('microblogForm');
const input = document.getElementById('microblogInput');
const feed = document.getElementById('microblogFeed');

form.onsubmit = e => {
  e.preventDefault();
  const text = input.value.trim();
  if (!text) return;

  const post = document.createElement('div');
  post.className = 'microblog-post';
  post.innerHTML = `
    <p></p>
    <div class="post-actions">
      <i class="fa-regular fa-thumbs-up action-icon"></i>
      <i class="fa-solid fa-share-nodes action-icon"></i>
      <i class="fa-regular fa-comment action-icon"></i>
    </div>
    <div class="comment-section" hidden>
      <input class="comment-input" placeholder="Write a comment...">
      <i class="fa-solid fa-circle-plus action-icon"></i>
    </div>`;
  post.querySelector('p').textContent = text;

  const [like, share, comment, add] = post.querySelectorAll('i');
  const box = post.querySelector('.comment-section');
  const cInput = box.querySelector('input');

  like.onclick = () => ['fa-regular', 'fa-solid', 'liked'].forEach(c => like.classList.toggle(c));
  share.onclick = () => alert('Post shared!');
  comment.onclick = () => box.hidden = !box.hidden;
  add.onclick = () => {
    if (!cInput.value.trim()) return;
    const p = document.createElement('p');
    p.textContent = cInput.value;
    box.append(p);
    cInput.value = '';
  };

  feed.prepend(post);
  input.value = '';
};

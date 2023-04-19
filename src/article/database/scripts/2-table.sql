CREATE TABLE user_articles.articles(
  id integer PRIMARY KEY,
  author text,
  title text,
  description text,
  keywords text[],
  contents text
);

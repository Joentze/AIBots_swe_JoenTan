db.createUser({
  user: "root",
  pwd: "example",
  roles: [
    {
      role: "readWrite",
      db: "aibots",
    },
  ],
});
db.createCollection("conversations");
db.conversations.insertOne({
  name: "hello world",
  params: {},
  model: "",
});

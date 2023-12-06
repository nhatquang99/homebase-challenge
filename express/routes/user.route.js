const express = require("express");
const router = express.Router();
const User = require('../models/user.model');

router.post('/users', async (req, res) => {
  await User.create(req.body);
  res.send("success");
})

router.get('/users', async (req, res) => {
  const users = await User.findAll();
  res.send(users);
})

router.get('/users/:id', async (req, res) => {
  const id = req.params.id;
  const user = await User.findOne({where: {id: id}});
  res.send(user);
})

router.put('/users/:id', async (req, res) => {
  const id = req.params.id;
  const user = await User.findOne({where: {id: id}});
  user.username = req.body.username;
  await user.save();
  res.send('updated');
})

router.delete('/users/:id', async (req, res) => {
  const id = req.params.id;
  await User.destroy({where: {id: id}});
  res.send('removed');
})

module.exports = router
#!/bin/bash

echo "=> Setando configuracoes de ambiente iniciais..."
export FLASK_ENV=development
export FLASK_DEBUG=True
export FLASK_APP=./app
echo""

echo "=> Setando FLASK_CONFIG"
export FLASK_CONFIG=development
echo ""

echo "=> Iniciando Flask Application..."
flask run
echo ""

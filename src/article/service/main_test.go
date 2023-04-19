package main

import (
  "database/sql"
  "testing"
)

func TestConnectDB( t *testing.T ) {
  var database *sql.DB
  var err error

  var status int = connectDB( database, err )

  if ( status != 0 || err != nil ) {
    t.Fatalf( `connectDB() Failed with error message: %s`, err )
  }
}

func TestInsertDB( t *testing.T ) {
  var database *sql.DB
  var err error
  var status int

  var art Article = Article{ id: 1, author: "Mike", title: "TestTitle", description: "TestDesc", 
                             keywords: []string{ "One", "Two" }, contents: "TestContents" }

  status = insertDB( database, err, art )

  if ( status != 0 || err != nil ) {
    t.Fatalf( `connectDB() Failed with error message: %s`, err )
  }
}

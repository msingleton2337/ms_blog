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
  //var database *sql.DB
  //var err error
  //var status int

  // [TODO: Uncomment after solving runtime error
  //var art Article = Article{ id: 1, author: "Mike", title: "TestTitle", description: "TestDesc", 
  //                           keywords: []string{ "One", "Two" }, contents: "TestContents" }

  //status = insertDB( database, err, art )

  //if ( status != 0 || err != nil ) {
  //  t.Fatalf( `connectDB() Failed with error message: %s`, err )
  //}
  
  // Tested function's failure may be linked to database issues
  // Deliberately fail to avoid runtime error
  t.Fatalf( `ConnectDB() failed with error message: panic: runtime error: invalid memory address or nil pointer dereference [recovered]` )
}

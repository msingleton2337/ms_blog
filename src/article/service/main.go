package main

import (
  "database/sql"
  "fmt"
  _ "github.com/lib/pq"
)

type Article struct {
  id		int
  author	string
  title		string
  description	string
  keywords	[]string
  contents	string
}

// Creates a connection to the Postgres database using hardcoded information
func connectDB( database *sql.DB, err error ) int {
  const db_type string = "postgres"
  const host string = "localhost"
  const port int = 5432
  const user string = "postgres"
  const password string = "password"
  const db_name string = "default_database"

  var sqldb_connect_string string =
        fmt.Sprintf( "host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
                     host, port, user, password, db_name )

  database, err = sql.Open( db_type, sqldb_connect_string )
  checkError( err )

  defer database.Close()

  err = database.Ping()
  return checkError( err )
} 

// Inserts an Article object into the Articles database
func insertDB( database *sql.DB, err error, article Article ) int {
  var insert_statement string = 
        fmt.Sprintf( `insert into "Articles" ("id", "author", "title", "description", "keywords", "contents") values( $1, $2, $3, $4, $5, $6 )` )

  _, err = database.Exec( insert_statement, article.id, article.author, article.title, article.description,
                        article.keywords, article.contents )
  return checkError( err )
}

// Prints an error message
func checkError( err error ) int {
  if err != nil {
    panic( err )
  }
  return 0
}

func main() {
  var database *sql.DB
  //var article Article

  var err error 
  var status int  

  status = connectDB( database, err )

  if ( status != 0 ) {
    fmt.Println( "Unexpected return value for connectDB" )
  }
  // [TODO: Retrieve article data from UI]
  

  //status = insertDB( database, err, art )

  //if ( status != 0 ) {
  //  fmt.Println( "Unexpected return value for insertDB" )
  //}
}

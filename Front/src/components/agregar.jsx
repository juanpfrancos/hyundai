import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';


const useStyles = makeStyles((theme) => ({
  root: {
    '& > *': {
      margin: theme.spacing(1),
    },
  },
}));


function Add(){

    const classes = useStyles();
    return (
        <>
          <h1>Agregar Producto</h1>
          <form className={classes.root} noValidate autoComplete="off">
          <TextField id="outlined-basic" label="Producto" variant="outlined" />
          <TextField id="outlined-basic" label="Precio" variant="outlined" />
          <Button variant="contained" color="primary">
            Guardar
          </Button>
        </form>
        </>
    )
}

export default Add
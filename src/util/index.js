export const cookies = document.cookie.split(/ */).reduce((obj, str) => {
    if (str === ``) return obj
    const eq = str.indexOf('=')
  
    const key = eq > 0
      ? str.slice(0, eq)
      : str
  
    let val = eq > 0
      ? str.slice(eq + 1)
      : null
  
    if (val != null)
      try {
        val = decodeURIComponent(val)
      } catch(ex) {
        console.error(ex)
      }
  
    obj[key] = val
    return obj
  }, {})
  
  // Gets current date in proper format for Date Picker component
  export const getCurrentDate = () => {
    const date = new Date()
    return `${date.getFullYear()}-${leadingZero(date.getMonth() + 1)}-${leadingZero(date.getDate())}`
  }
  
  export const formatDate = date => {
    const d = new Date(date)
    return `${d.getFullYear()}-${leadingZero(d.getMonth() + 1)}-${leadingZero(d.getDate())}`
  }
  
  const leadingZero = number => {
    if (number < 0) throw new Error(`Number must be positive`)
    return number < 10
      ? `0${number}`
      : `${number}`
  }
  
  export const authenticated = () => new Promise(resolve => {
    fetch(`${process.env.VUE_APP_API_ORIGIN}/api/v1/user`, { credentials: 'include' })
      .then(({ ok }) => resolve(ok))
      .catch(err => {
        console.error(`Error in 'authenticated': `, err)
        resolve(false)
      })
  })
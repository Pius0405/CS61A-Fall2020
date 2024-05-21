(define (split-at lst n)
  (cond
      ((= 0 n) (cons nil lst))
      ((null? lst) (cons nil nil))
      (else (begin (define temp (split-at (cdr lst) (- n 1))) 
                   (cons (cons (car lst) (car temp)) (cdr temp)))
            )
      )
)


(define (compose-all funcs)
  (cond
      ((null? funcs) (lambda (x) x))
      ((null? (cdr funcs)) (lambda (x) ((car funcs) x)))
      (else (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x))))
      )
)


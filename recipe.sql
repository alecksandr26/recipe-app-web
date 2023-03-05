--
-- PostgreSQL database dump
--

-- Dumped from database version 14.3
-- Dumped by pg_dump version 14.3

-- Started on 2023-02-28 10:28:08

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 210 (class 1259 OID 57583)
-- Name: category; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.category (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    descr text NOT NULL
);


ALTER TABLE public.category OWNER TO postgres;

--
-- TOC entry 209 (class 1259 OID 57582)
-- Name: category_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.category_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_id_seq OWNER TO postgres;

--
-- TOC entry 3418 (class 0 OID 0)
-- Dependencies: 209
-- Name: category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.category_id_seq OWNED BY public.category.id;


--
-- TOC entry 224 (class 1259 OID 57650)
-- Name: cheff; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.cheff (
    id integer NOT NULL,
    iduser integer NOT NULL
);


ALTER TABLE public.cheff OWNER TO postgres;

--
-- TOC entry 222 (class 1259 OID 57648)
-- Name: cheff_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cheff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cheff_id_seq OWNER TO postgres;

--
-- TOC entry 3419 (class 0 OID 0)
-- Dependencies: 222
-- Name: cheff_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cheff_id_seq OWNED BY public.cheff.id;


--
-- TOC entry 223 (class 1259 OID 57649)
-- Name: cheff_iduser_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.cheff_iduser_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.cheff_iduser_seq OWNER TO postgres;

--
-- TOC entry 3420 (class 0 OID 0)
-- Dependencies: 223
-- Name: cheff_iduser_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.cheff_iduser_seq OWNED BY public.cheff.iduser;


--
-- TOC entry 231 (class 1259 OID 57699)
-- Name: lists_recipes; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.lists_recipes (
    id integer NOT NULL,
    idrecipe integer NOT NULL,
    idrecipelist integer NOT NULL
);


ALTER TABLE public.lists_recipes OWNER TO postgres;

--
-- TOC entry 228 (class 1259 OID 57696)
-- Name: lists_recipes_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lists_recipes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lists_recipes_id_seq OWNER TO postgres;

--
-- TOC entry 3421 (class 0 OID 0)
-- Dependencies: 228
-- Name: lists_recipes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lists_recipes_id_seq OWNED BY public.lists_recipes.id;


--
-- TOC entry 229 (class 1259 OID 57697)
-- Name: lists_recipes_idrecipe_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lists_recipes_idrecipe_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lists_recipes_idrecipe_seq OWNER TO postgres;

--
-- TOC entry 3422 (class 0 OID 0)
-- Dependencies: 229
-- Name: lists_recipes_idrecipe_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lists_recipes_idrecipe_seq OWNED BY public.lists_recipes.idrecipe;


--
-- TOC entry 230 (class 1259 OID 57698)
-- Name: lists_recipes_idrecipelist_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.lists_recipes_idrecipelist_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.lists_recipes_idrecipelist_seq OWNER TO postgres;

--
-- TOC entry 3423 (class 0 OID 0)
-- Dependencies: 230
-- Name: lists_recipes_idrecipelist_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.lists_recipes_idrecipelist_seq OWNED BY public.lists_recipes.idrecipelist;


--
-- TOC entry 219 (class 1259 OID 57628)
-- Name: nutritional_ele; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nutritional_ele (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    amount double precision NOT NULL,
    unit character varying(10) NOT NULL,
    idrecipe integer NOT NULL,
    CONSTRAINT nutritional_ele_amount_check CHECK ((amount > (0.0)::double precision))
);


ALTER TABLE public.nutritional_ele OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 57626)
-- Name: nutritional_ele_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.nutritional_ele_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.nutritional_ele_id_seq OWNER TO postgres;

--
-- TOC entry 3424 (class 0 OID 0)
-- Dependencies: 217
-- Name: nutritional_ele_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.nutritional_ele_id_seq OWNED BY public.nutritional_ele.id;


--
-- TOC entry 218 (class 1259 OID 57627)
-- Name: nutritional_ele_idrecipe_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.nutritional_ele_idrecipe_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.nutritional_ele_idrecipe_seq OWNER TO postgres;

--
-- TOC entry 3425 (class 0 OID 0)
-- Dependencies: 218
-- Name: nutritional_ele_idrecipe_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.nutritional_ele_idrecipe_seq OWNED BY public.nutritional_ele.idrecipe;


--
-- TOC entry 216 (class 1259 OID 57613)
-- Name: ratings; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.ratings (
    id integer NOT NULL,
    comment character varying(250),
    rating double precision NOT NULL,
    idrecipe integer NOT NULL,
    CONSTRAINT ratings_rating_check CHECK (((rating >= (0.0)::double precision) AND (rating <= (5.0)::double precision)))
);


ALTER TABLE public.ratings OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 57611)
-- Name: ratings_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ratings_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ratings_id_seq OWNER TO postgres;

--
-- TOC entry 3426 (class 0 OID 0)
-- Dependencies: 214
-- Name: ratings_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ratings_id_seq OWNED BY public.ratings.id;


--
-- TOC entry 215 (class 1259 OID 57612)
-- Name: ratings_idrecipe_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.ratings_idrecipe_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ratings_idrecipe_seq OWNER TO postgres;

--
-- TOC entry 3427 (class 0 OID 0)
-- Dependencies: 215
-- Name: ratings_idrecipe_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.ratings_idrecipe_seq OWNED BY public.ratings.idrecipe;


--
-- TOC entry 213 (class 1259 OID 57593)
-- Name: recipe; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipe (
    id integer NOT NULL,
    preptime double precision NOT NULL,
    cooktime double precision,
    ingredients text NOT NULL,
    instructions text NOT NULL,
    portions integer DEFAULT 1,
    idcategory integer NOT NULL,
    CONSTRAINT recipe_cooktime_check CHECK ((cooktime >= (0.0)::double precision)),
    CONSTRAINT recipe_portions_check CHECK ((portions >= 1)),
    CONSTRAINT recipe_preptime_check CHECK ((preptime >= (0.0)::double precision))
);


ALTER TABLE public.recipe OWNER TO postgres;

--
-- TOC entry 211 (class 1259 OID 57591)
-- Name: recipe_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recipe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipe_id_seq OWNER TO postgres;

--
-- TOC entry 3428 (class 0 OID 0)
-- Dependencies: 211
-- Name: recipe_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recipe_id_seq OWNED BY public.recipe.id;


--
-- TOC entry 212 (class 1259 OID 57592)
-- Name: recipe_idcategory_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recipe_idcategory_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipe_idcategory_seq OWNER TO postgres;

--
-- TOC entry 3429 (class 0 OID 0)
-- Dependencies: 212
-- Name: recipe_idcategory_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recipe_idcategory_seq OWNED BY public.recipe.idcategory;


--
-- TOC entry 227 (class 1259 OID 57670)
-- Name: recipelists; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.recipelists (
    id integer NOT NULL,
    name character varying(50) NOT NULL,
    descr text,
    privarcystatus boolean DEFAULT false,
    iduser integer NOT NULL
);


ALTER TABLE public.recipelists OWNER TO postgres;

--
-- TOC entry 225 (class 1259 OID 57668)
-- Name: recipelists_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recipelists_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipelists_id_seq OWNER TO postgres;

--
-- TOC entry 3430 (class 0 OID 0)
-- Dependencies: 225
-- Name: recipelists_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recipelists_id_seq OWNED BY public.recipelists.id;


--
-- TOC entry 226 (class 1259 OID 57669)
-- Name: recipelists_iduser_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.recipelists_iduser_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.recipelists_iduser_seq OWNER TO postgres;

--
-- TOC entry 3431 (class 0 OID 0)
-- Dependencies: 226
-- Name: recipelists_iduser_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.recipelists_iduser_seq OWNED BY public.recipelists.iduser;


--
-- TOC entry 221 (class 1259 OID 57642)
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username character varying(50) NOT NULL,
    mail character varying(50),
    password character varying(50) NOT NULL
);


ALTER TABLE public.users OWNER TO postgres;

--
-- TOC entry 220 (class 1259 OID 57641)
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- TOC entry 3432 (class 0 OID 0)
-- Dependencies: 220
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- TOC entry 3206 (class 2604 OID 57586)
-- Name: category id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category ALTER COLUMN id SET DEFAULT nextval('public.category_id_seq'::regclass);


--
-- TOC entry 3220 (class 2604 OID 57653)
-- Name: cheff id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cheff ALTER COLUMN id SET DEFAULT nextval('public.cheff_id_seq'::regclass);


--
-- TOC entry 3221 (class 2604 OID 57654)
-- Name: cheff iduser; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cheff ALTER COLUMN iduser SET DEFAULT nextval('public.cheff_iduser_seq'::regclass);


--
-- TOC entry 3225 (class 2604 OID 57702)
-- Name: lists_recipes id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lists_recipes ALTER COLUMN id SET DEFAULT nextval('public.lists_recipes_id_seq'::regclass);


--
-- TOC entry 3226 (class 2604 OID 57703)
-- Name: lists_recipes idrecipe; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lists_recipes ALTER COLUMN idrecipe SET DEFAULT nextval('public.lists_recipes_idrecipe_seq'::regclass);


--
-- TOC entry 3227 (class 2604 OID 57704)
-- Name: lists_recipes idrecipelist; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lists_recipes ALTER COLUMN idrecipelist SET DEFAULT nextval('public.lists_recipes_idrecipelist_seq'::regclass);


--
-- TOC entry 3216 (class 2604 OID 57631)
-- Name: nutritional_ele id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nutritional_ele ALTER COLUMN id SET DEFAULT nextval('public.nutritional_ele_id_seq'::regclass);


--
-- TOC entry 3217 (class 2604 OID 57632)
-- Name: nutritional_ele idrecipe; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nutritional_ele ALTER COLUMN idrecipe SET DEFAULT nextval('public.nutritional_ele_idrecipe_seq'::regclass);


--
-- TOC entry 3213 (class 2604 OID 57616)
-- Name: ratings id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ratings ALTER COLUMN id SET DEFAULT nextval('public.ratings_id_seq'::regclass);


--
-- TOC entry 3214 (class 2604 OID 57617)
-- Name: ratings idrecipe; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ratings ALTER COLUMN idrecipe SET DEFAULT nextval('public.ratings_idrecipe_seq'::regclass);


--
-- TOC entry 3207 (class 2604 OID 57596)
-- Name: recipe id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe ALTER COLUMN id SET DEFAULT nextval('public.recipe_id_seq'::regclass);


--
-- TOC entry 3209 (class 2604 OID 57598)
-- Name: recipe idcategory; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe ALTER COLUMN idcategory SET DEFAULT nextval('public.recipe_idcategory_seq'::regclass);


--
-- TOC entry 3222 (class 2604 OID 57673)
-- Name: recipelists id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipelists ALTER COLUMN id SET DEFAULT nextval('public.recipelists_id_seq'::regclass);


--
-- TOC entry 3224 (class 2604 OID 57675)
-- Name: recipelists iduser; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipelists ALTER COLUMN iduser SET DEFAULT nextval('public.recipelists_iduser_seq'::regclass);


--
-- TOC entry 3219 (class 2604 OID 57645)
-- Name: users id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- TOC entry 3391 (class 0 OID 57583)
-- Dependencies: 210
-- Data for Name: category; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.category (id, name, descr) FROM stdin;
\.


--
-- TOC entry 3405 (class 0 OID 57650)
-- Dependencies: 224
-- Data for Name: cheff; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.cheff (id, iduser) FROM stdin;
\.


--
-- TOC entry 3412 (class 0 OID 57699)
-- Dependencies: 231
-- Data for Name: lists_recipes; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.lists_recipes (id, idrecipe, idrecipelist) FROM stdin;
\.


--
-- TOC entry 3400 (class 0 OID 57628)
-- Dependencies: 219
-- Data for Name: nutritional_ele; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nutritional_ele (id, name, amount, unit, idrecipe) FROM stdin;
\.


--
-- TOC entry 3397 (class 0 OID 57613)
-- Dependencies: 216
-- Data for Name: ratings; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.ratings (id, comment, rating, idrecipe) FROM stdin;
\.


--
-- TOC entry 3394 (class 0 OID 57593)
-- Dependencies: 213
-- Data for Name: recipe; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipe (id, preptime, cooktime, ingredients, instructions, portions, idcategory) FROM stdin;
\.


--
-- TOC entry 3408 (class 0 OID 57670)
-- Dependencies: 227
-- Data for Name: recipelists; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.recipelists (id, name, descr, privarcystatus, iduser) FROM stdin;
\.


--
-- TOC entry 3402 (class 0 OID 57642)
-- Dependencies: 221
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, username, mail, password) FROM stdin;
\.


--
-- TOC entry 3433 (class 0 OID 0)
-- Dependencies: 209
-- Name: category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.category_id_seq', 1, false);


--
-- TOC entry 3434 (class 0 OID 0)
-- Dependencies: 222
-- Name: cheff_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cheff_id_seq', 1, false);


--
-- TOC entry 3435 (class 0 OID 0)
-- Dependencies: 223
-- Name: cheff_iduser_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.cheff_iduser_seq', 1, false);


--
-- TOC entry 3436 (class 0 OID 0)
-- Dependencies: 228
-- Name: lists_recipes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lists_recipes_id_seq', 1, false);


--
-- TOC entry 3437 (class 0 OID 0)
-- Dependencies: 229
-- Name: lists_recipes_idrecipe_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lists_recipes_idrecipe_seq', 1, false);


--
-- TOC entry 3438 (class 0 OID 0)
-- Dependencies: 230
-- Name: lists_recipes_idrecipelist_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.lists_recipes_idrecipelist_seq', 1, false);


--
-- TOC entry 3439 (class 0 OID 0)
-- Dependencies: 217
-- Name: nutritional_ele_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.nutritional_ele_id_seq', 1, false);


--
-- TOC entry 3440 (class 0 OID 0)
-- Dependencies: 218
-- Name: nutritional_ele_idrecipe_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.nutritional_ele_idrecipe_seq', 1, false);


--
-- TOC entry 3441 (class 0 OID 0)
-- Dependencies: 214
-- Name: ratings_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ratings_id_seq', 1, false);


--
-- TOC entry 3442 (class 0 OID 0)
-- Dependencies: 215
-- Name: ratings_idrecipe_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.ratings_idrecipe_seq', 1, false);


--
-- TOC entry 3443 (class 0 OID 0)
-- Dependencies: 211
-- Name: recipe_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recipe_id_seq', 1, false);


--
-- TOC entry 3444 (class 0 OID 0)
-- Dependencies: 212
-- Name: recipe_idcategory_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recipe_idcategory_seq', 1, false);


--
-- TOC entry 3445 (class 0 OID 0)
-- Dependencies: 225
-- Name: recipelists_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recipelists_id_seq', 1, false);


--
-- TOC entry 3446 (class 0 OID 0)
-- Dependencies: 226
-- Name: recipelists_iduser_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.recipelists_iduser_seq', 1, false);


--
-- TOC entry 3447 (class 0 OID 0)
-- Dependencies: 220
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- TOC entry 3229 (class 2606 OID 57590)
-- Name: category category_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.category
    ADD CONSTRAINT category_pkey PRIMARY KEY (id);


--
-- TOC entry 3239 (class 2606 OID 57656)
-- Name: cheff cheff_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cheff
    ADD CONSTRAINT cheff_pkey PRIMARY KEY (id);


--
-- TOC entry 3243 (class 2606 OID 57706)
-- Name: lists_recipes lists_recipes_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lists_recipes
    ADD CONSTRAINT lists_recipes_pkey PRIMARY KEY (id);


--
-- TOC entry 3235 (class 2606 OID 57635)
-- Name: nutritional_ele nutritional_ele_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nutritional_ele
    ADD CONSTRAINT nutritional_ele_pkey PRIMARY KEY (id);


--
-- TOC entry 3233 (class 2606 OID 57620)
-- Name: ratings ratings_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_pkey PRIMARY KEY (id);


--
-- TOC entry 3231 (class 2606 OID 57605)
-- Name: recipe recipe_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe
    ADD CONSTRAINT recipe_pkey PRIMARY KEY (id);


--
-- TOC entry 3241 (class 2606 OID 57679)
-- Name: recipelists recipelists_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipelists
    ADD CONSTRAINT recipelists_pkey PRIMARY KEY (id);


--
-- TOC entry 3237 (class 2606 OID 57647)
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- TOC entry 3247 (class 2606 OID 57657)
-- Name: cheff cheff_iduser_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.cheff
    ADD CONSTRAINT cheff_iduser_fkey FOREIGN KEY (iduser) REFERENCES public.users(id);


--
-- TOC entry 3249 (class 2606 OID 57707)
-- Name: lists_recipes lists_recipes_idrecipe_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lists_recipes
    ADD CONSTRAINT lists_recipes_idrecipe_fkey FOREIGN KEY (idrecipe) REFERENCES public.recipe(id);


--
-- TOC entry 3250 (class 2606 OID 57712)
-- Name: lists_recipes lists_recipes_idrecipelist_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.lists_recipes
    ADD CONSTRAINT lists_recipes_idrecipelist_fkey FOREIGN KEY (idrecipelist) REFERENCES public.recipelists(id);


--
-- TOC entry 3246 (class 2606 OID 57636)
-- Name: nutritional_ele nutritional_ele_idrecipe_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nutritional_ele
    ADD CONSTRAINT nutritional_ele_idrecipe_fkey FOREIGN KEY (idrecipe) REFERENCES public.recipe(id);


--
-- TOC entry 3245 (class 2606 OID 57621)
-- Name: ratings ratings_idrecipe_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.ratings
    ADD CONSTRAINT ratings_idrecipe_fkey FOREIGN KEY (idrecipe) REFERENCES public.recipe(id);


--
-- TOC entry 3244 (class 2606 OID 57606)
-- Name: recipe recipe_idcategory_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipe
    ADD CONSTRAINT recipe_idcategory_fkey FOREIGN KEY (idcategory) REFERENCES public.category(id);


--
-- TOC entry 3248 (class 2606 OID 57680)
-- Name: recipelists recipelists_iduser_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.recipelists
    ADD CONSTRAINT recipelists_iduser_fkey FOREIGN KEY (iduser) REFERENCES public.users(id);


-- Completed on 2023-02-28 10:28:08

--
-- PostgreSQL database dump complete
--


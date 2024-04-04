--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

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
-- Name: AAPL_daily; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."AAPL_daily" (
    "Date" text,
    "Time" text,
    "Open" double precision,
    "High" double precision,
    "Low" double precision,
    "Close" double precision,
    "Volume" bigint
);


ALTER TABLE public."AAPL_daily" OWNER TO postgres;

--
-- Data for Name: AAPL_daily; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."AAPL_daily" ("Date", "Time", "Open", "High", "Low", "Close", "Volume") FROM 'E:\\CODE-learning\\Funny project\\data.txt';

--
-- PostgreSQL database dump complete
--


import express from "express";
import { PrismaClient } from "@prisma/client";

const app = express();
const prisma = new PrismaClient();

app.use(express.static(__dirname + "/static"));
app.use(express.json());

app.post(
  "/api/article",
  async (req: express.Request, res: express.Response) => {
    try {
      res.json({
        ok: true,
        results: await prisma.article.findMany({
          where: req.body,
          select: {
            id: true,
            title: true,
            body: true,
            clowns: {
              where: {},
              select: {
                clown: {
                  select: {
                    id: true,
                    name: true,
                  },
                },
              },
            },
          },
        }),
      });
    } catch (error) {
      res.json({ ok: false, error });
    }
  }
);

(async () => {
  await new Promise<void>((resolve) =>
    app.listen(Number(process.env.PORT || 5000), resolve)
  );
  console.log(`Listening on :${Number(process.env.PORT || 5000)}`);
})();
